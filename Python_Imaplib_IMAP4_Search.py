# Python Imaplib
# imaplib — IMAP4 protocol client.
# This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream, which encapsulate a connection to an IMAP4 server and implement a large subset of
# the IMAP4rev1 client protocol as defined in RFC 2060.
# It is backward compatible with IMAP4 (RFC 1730) servers, but note that the STATUS command is not supported in IMAP4.
#

#
# IMAP4.search(charset, criterion[, ...]): 
# Search mailbox for matching messages.
# charset may be None, in which case no CHARSET will be specified in the request to the server.
# The IMAP protocol requires that at least one criterion be specified; an exception will be raised when the server returns an error.
# charset must be None if the UTF8=ACCEPT capability was enabled using the enable() command.
#

# 
# Example:
# 

# M is a connected IMAP4 instance...

typ, msgnums = M.search(None, 'FROM', '"LDJ"')

# or:

typ, msgnums = M.search(None, '(FROM "LDJ")')
