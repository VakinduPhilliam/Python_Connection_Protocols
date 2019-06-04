# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

#
# Here are two small examples of how it can be used.
# To list some statistics about a newsgroup and print the subjects of the last 10 articles:
# 

s = nntplib.NNTP('news.gmane.org')
resp, count, first, last, name = s.group('gmane.comp.python.committers')

print('Group', name, 'has', count, 'articles, range', first, 'to', last)

# OUTPUT: 'Group gmane.comp.python.committers has 1096 articles, range 1 to 1096'

resp, overviews = s.over((last - 9, last))

for id, over in overviews:

            print(id, nntplib.decode_header(over['subject']))
