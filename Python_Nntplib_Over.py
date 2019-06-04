# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

#
# NNTP.over(message_spec, *, file=None): 
# Send an OVER command, or an XOVER command on legacy servers.
# message_spec can be either a string representing a message id, or a (first, last) tuple of numbers indicating a range of articles in the current group, or
# a (first, None) tuple indicating a range of articles starting from first to the last article in the current group, or None to select the current article
# in the current group.
#

#
# It is advisable to use the decode_header() function on header values when they may contain non-ASCII characters:
# 

_, _, first, last, _ = s.group('gmane.comp.python.devel')
resp, overviews = s.over((last, last))

art_num, over = overviews[0]

art_num

# OUTPUT: '117216'

list(over.keys())

# OUTPUT: '['xref', 'from', ':lines', ':bytes', 'references', 'date', 'message-id', 'subject']'

over['from']

# OUTPUT: '=?UTF-8?B?Ik1hcnRpbiB2LiBMw7Z3aXMi?= <martin@v.loewis.de>'

nntplib.decode_header(over['from'])

# OUTPUT: '"Martin v. Löwis" <martin@v.loewis.de>'
