# Python smtplib
# smtplib — SMTP protocol client
# The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
#

#
# This example prompts the user for addresses needed in the message envelope (‘To’ and ‘From’ addresses), and the message to be delivered.
# Note that the headers to be included with the message must be included in the message as entered; this example doesn’t do any processing of the RFC 822
# headers.
# In particular, the ‘To’ and ‘From’ addresses must be included in the message headers explicitly.
# 

import smtplib

def prompt(prompt):

           return input(prompt).strip()

fromaddr = prompt("From: ")

toaddrs  = prompt("To: ").split()

print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!

msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))

while True:

    try:
        line = input()

    except EOFError:
        break

    if not line:
        break

    msg = msg + line

print("Message length is", len(msg))

server = smtplib.SMTP('localhost')

server.set_debuglevel(1)

server.sendmail(fromaddr, toaddrs, msg)

server.quit()
