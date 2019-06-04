# Python Imaplib
# imaplib — IMAP4 protocol client.
# This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream, which encapsulate a connection to an IMAP4 server and implement a large subset of
# the IMAP4rev1 client protocol as defined in RFC 2060.
# It is backward compatible with IMAP4 (RFC 1730) servers, but note that the STATUS command is not supported in IMAP4.
#

#
# A minimal example (without error checking) that opens a mailbox and retrieves and prints all messages:
# 

import getpass, imaplib

M = imaplib.IMAP4()

M.login(getpass.getuser(), getpass.getpass())
M.select()

typ, data = M.search(None, 'ALL')

for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')

    print('Message %s\n%s\n' % (num, data[0][1]))

M.close()

M.logout()
