# Python Mailbox
# mailbox — Manipulate mailboxes in various formats.
# This module defines two classes, Mailbox and Message, for accessing and manipulating on-disk mailboxes and the messages they contain.
# Mailbox offers a dictionary-like mapping from keys to messages.
# Message extends the email.message module’s Message class with format-specific state and behavior.
# Supported mailbox formats are Maildir, mbox, MH, Babyl, and MMDF.

#
# Maildir
# class mailbox.Maildir(dirname, factory=None, create=True). 
# A subclass of Mailbox for mailboxes in Maildir format. Parameter factory is a callable object that accepts a file-like message representation
# (which behaves as if opened in binary mode) and returns a custom representation.
# If factory is None, MaildirMessage is used as the default message representation.
# If create is True, the mailbox is created if it does not exist.
#

#
# Note:
# The Maildir specification requires the use of a colon (':') in certain message file names.
# However, some operating systems do not permit this character in file names, If you wish to use a Maildir-like format on such an operating system, you
# should specify another character to use instead. The exclamation point ('!') is a popular choice.
#

#
# For example:
# 

import mailbox

mailbox.Maildir.colon = '!'
