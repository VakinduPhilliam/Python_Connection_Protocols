# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

#
# NNTP.descriptions(grouppattern): 
# Send a LIST NEWSGROUPS command, where grouppattern is a wildmat string as specified in RFC 3977 (it’s essentially the same as DOS or UNIX shell wildcard 
# strings).
# Return a pair (response, descriptions), where descriptions is a dictionary mapping group names to textual descriptions.
# 

resp, descs = s.descriptions('gmane.comp.python.*')

len(descs) # doctest: +SKIP

# OUTPUT: '295'

descs.popitem() # doctest: +SKIP

# OUTPUT: '('gmane.comp.python.bio.general', 'BioPython discussion list (Moderated)')'
