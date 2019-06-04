# Python Imaplib
# imaplib — IMAP4 protocol client.
# This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream, which encapsulate a connection to an IMAP4 server and implement a large subset of
# the IMAP4rev1 client protocol as defined in RFC 2060.
# It is backward compatible with IMAP4 (RFC 1730) servers, but note that the STATUS command is not supported in IMAP4.
#

#
# IMAP4.store(message_set, command, flag_list): 
# Alters flag dispositions for messages in mailbox.
# command is specified by section 6.4.6 of RFC 2060 as being one of “FLAGS”, “+FLAGS”, or “-FLAGS”, optionally with a suffix of “.SILENT”.
#
 
#
# For example, to set the delete flag on all messages:
# 

typ, data = M.search(None, 'ALL')

for num in data[0].split():

             M.store(num, '+FLAGS', '\\Deleted')

M.expunge()
