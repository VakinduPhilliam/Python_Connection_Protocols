# Python Nntplib
# nntplib � NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

#
# class nntplib.NNTP(host, port=119, user=None, password=None, readermode=None, usenetrc=False[, timeout]):
# Return a new NNTP object, representing a connection to the NNTP server running on host host, listening at port port.
# An optional timeout can be specified for the socket connection.
# If the optional user and password are provided, or if suitable credentials are present in /.netrc and the optional flag usenetrc is true, the AUTHINFO
# USER and AUTHINFO PASS commands are used to identify and authenticate the user to the server.
# If the optional flag readermode is true, then a mode reader command is sent before authentication is performed.
# Reader mode is sometimes necessary if you are connecting to an NNTP server on the local machine and intend to call reader-specific commands, such as group.
# If you get unexpected NNTPPermanentErrors, you might need to set readermode.
# The NNTP class supports the with statement to unconditionally consume OSError exceptions and to close the NNTP connection when done, e.g.:
# 

from nntplib import NNTP

with NNTP('news.gmane.org') as n:

           n.group('gmane.comp.python.committers')

# doctest: +SKIP

# OUTPUT: '('211 1755 1 1755 gmane.comp.python.committers', 1755, 1, 1755, 'gmane.comp.python.committers')'
