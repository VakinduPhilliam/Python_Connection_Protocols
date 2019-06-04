# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

#
# NNTP.stat(message_spec=None) 
# Send a STAT command, where message_spec is either a message id (enclosed in '<' and '>') or an article number in the current group.
# If message_spec is omitted or None, the current article in the current group is considered.
# Return a triple (response, number, id) where number is the article number and id is the message id.
# 

_, _, first, last, _ = s.group('gmane.comp.python.devel')
resp, number, message_id = s.stat(first)

number, message_id

# OUTPUT: '(9099, '<20030112190404.GE29873@epoch.metaslash.com>')'
