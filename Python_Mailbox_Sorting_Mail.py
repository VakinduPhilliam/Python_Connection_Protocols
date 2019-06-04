# Python Mailbox
# mailbox — Manipulate mailboxes in various formats.
# This module defines two classes, Mailbox and Message, for accessing and manipulating on-disk mailboxes and the messages they contain.
# Mailbox offers a dictionary-like mapping from keys to messages.
# Message extends the email.message module’s Message class with format-specific state and behavior.
# Supported mailbox formats are Maildir, mbox, MH, Babyl, and MMDF.

#
# This example sorts mail from several mailing lists into different mailboxes, being careful to avoid mail corruption due to concurrent modification by
# other programs, mail loss due to interruption of the program, or premature termination due to malformed messages in the mailbox:
# 

import mailbox
import email.errors

list_names = ('python-list', 'python-dev', 'python-bugs')

boxes = {name: mailbox.mbox('~/email/%s' % name) for name in list_names}

inbox = mailbox.Maildir('~/Maildir', factory=None)

for key in inbox.iterkeys():

    try:
        message = inbox[key]

    except email.errors.MessageParseError:
        continue                # The message is malformed. Just leave it.

    for name in list_names:
        list_id = message['list-id']

        if list_id and name in list_id:

            # Get mailbox to use

            box = boxes[name]

            # Write copy to disk before removing original.
            # If there's a crash, you might duplicate a message, but
            # that's better than losing a message completely.

            box.lock()
            box.add(message)

            box.flush()
            box.unlock()

            # Remove original message

            inbox.lock()
            inbox.discard(key)

            inbox.flush()
            inbox.unlock()

            break               # Found destination, so stop looking.

for box in boxes.itervalues():
    box.close()
