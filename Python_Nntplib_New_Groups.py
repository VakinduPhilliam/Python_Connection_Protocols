# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
#

#
# NNTP.newgroups(date, *, file=None): 
# Send a NEWGROUPS command.
# The date argument should be a datetime.date or datetime.datetime object.
# Return a pair (response, groups) where groups is a list representing the groups that are new since the given date.
# If file is supplied, though, then groups will be empty.
# 

from datetime import date, timedelta

resp, groups = s.newgroups(date.today() - timedelta(days=3))
len(groups) # doctest: +SKIP

# OUTPUT: '85'

groups[0] # doctest: +SKIP

# OUTPUT: 'GroupInfo(group='gmane.network.tor.devel', last='4', first='1', flag='m')'
