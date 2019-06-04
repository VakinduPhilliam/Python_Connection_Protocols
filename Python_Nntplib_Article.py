# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

#
# NNTP.article(message_spec=None, *, file=None): 
# Send an ARTICLE command, where message_spec has the same meaning as for stat().
# Return a tuple (response, info) where info is a namedtuple with three attributes number, message_id and lines (in that order).
# number is the article number in the group (or 0 if the information is not available), message_id the message id as a string, and lines a list of lines
# (without terminating newlines) comprising the raw message including headers and body.
# 

resp, info = s.article('<20030112190404.GE29873@epoch.metaslash.com>')
info.number

# OUTPUT: '0'

info.message_id

# OUTPUT: '<20030112190404.GE29873@epoch.metaslash.com>'

len(info.lines)

# OUTPUT: '65'

info.lines[0]

# OUTPUT: 'b'Path: main.gmane.org!not-for-mail''

info.lines[1]

# OUTPUT: 'b'From: Neal Norwitz <neal@metaslash.com>''

info.lines[-3:]

# OUTPUT: '[b'There is a patch for 2.3 as well as 2.2.', b'', b'Neal']'
