# Python Mailbox
# mailbox — Manipulate mailboxes in various formats.
# This module defines two classes, Mailbox and Message, for accessing and manipulating on-disk mailboxes and the messages they contain.
# Mailbox offers a dictionary-like mapping from keys to messages.
# Message extends the email.message module’s Message class with format-specific state and behavior.
# Supported mailbox formats are Maildir, mbox, MH, Babyl, and MMDF.
#

#
# A simple example of printing the subjects of all messages in a mailbox that seem interesting:
# 

import mailbox

for message in mailbox.mbox('~/mbox'):

    subject = message['subject']       # Could possibly be None.

    if subject and 'python' in subject.lower():

        print(subject)
