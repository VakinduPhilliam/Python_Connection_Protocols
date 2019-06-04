# Python Mailbox
# mailbox — Manipulate mailboxes in various formats.
# This module defines two classes, Mailbox and Message, for accessing and manipulating on-disk mailboxes and the messages they contain.
# Mailbox offers a dictionary-like mapping from keys to messages.
# Message extends the email.message module’s Message class with format-specific state and behavior.
# Supported mailbox formats are Maildir, mbox, MH, Babyl, and MMDF.
#

#
# To copy all mail from a Babyl mailbox to an MH mailbox, converting all of the format-specific information that can be converted:
# 

import mailbox

destination = mailbox.MH('~/Mail')
destination.lock()

for message in mailbox.Babyl('~/RMAIL'):
    destination.add(mailbox.MHMessage(message))

destination.flush()

destination.unlock()
