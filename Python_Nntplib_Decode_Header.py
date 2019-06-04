# Python Nntplib
# nntplib — NNTP protocol client.
# This module defines the class NNTP which implements the client side of the Network News Transfer Protocol.
# It can be used to implement a news reader or poster, or automated news processors.
# It is compatible with RFC 3977 as well as the older RFC 977 and RFC 2980.
# 

#
# nntplib.decode_header(header_str): 
# Decode a header value, un-escaping any escaped non-ASCII characters. header_str must be a str object.
# The unescaped value is returned.
#
# Using this function is recommended to display some headers in a human readable form:
# 

decode_header("Some subject")

# OUTPUT: 'Some subject'

decode_header("=?ISO-8859-15?Q?D=E9buter_en_Python?=")

# OUTPUT: 'Débuter en Python'

decode_header("Re: =?UTF-8?B?cHJvYmzDqG1lIGRlIG1hdHJpY2U=?=")

# OUTPUT: 'Re: problème de matrice'
