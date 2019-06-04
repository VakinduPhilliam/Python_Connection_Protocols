# Python Poplib
# poplib — POP3 protocol client.
# This module defines a class, POP3, which encapsulates a connection to a POP3 server and implements the protocol as defined in RFC 1939.
# The POP3 class supports both the minimal and optional command sets from RFC 1939.
# The POP3 class also supports the STLS command introduced in RFC 2595 to enable encrypted communication on an already established connection
# 
# Additionally, this module provides a class POP3_SSL, which provides support for connecting to POP3 servers that use SSL as an underlying protocol layer.
# 
# Note that POP3, though widely supported, is obsolescent.
# The implementation quality of POP3 servers varies widely, and too many are quite poor.
# If your mailserver supports IMAP, you would be better off using the imaplib.IMAP4 class, as IMAP servers tend to be better implemented.
#

#
# Here is a minimal example (without error checking) that opens a mailbox and retrieves and prints all messages:
# 

import getpass, poplib

M = poplib.POP3('localhost')

M.user(getpass.getuser())

M.pass_(getpass.getpass())

numMessages = len(M.list()[1])

for i in range(numMessages):

    for j in M.retr(i+1)[1]:

            print(j)
