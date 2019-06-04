# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

# 
# To post an article from a binary file (this assumes that the article has valid headers, and that you have right to post on the particular newsgroup):
# 

s = nntplib.NNTP('news.gmane.org')

f = open('article.txt', 'rb')

s.post(f)

# OUTPUT: '240 Article posted successfully.'

s.quit()

# OUTPUT: '205 Bye!'
