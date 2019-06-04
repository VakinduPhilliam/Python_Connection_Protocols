# Python smtplib
# smtplib — SMTP protocol client
# The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
#

#
# The SMTP class supports the 'with' statement. When used like this, the SMTP QUIT command is issued automatically when the 'with' statement exits. E.g.:
# 

from smtplib import SMTP

     with SMTP("domain.org") as smtp:

         smtp.noop()

# OUTPUT: '(250, b'Ok')'
