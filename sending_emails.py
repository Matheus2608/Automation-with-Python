# You could read the Simple Mail Transfer Protocol (SMTP) and Multipurpose Internet Mail Extensions (MIME) and create email messages all on your own, but you don't need to go to all that trouble. The email built-in Python module lets us easily construct email messages.https://docs.python.org/3/library/email.html
import getpass
import smtplib
import mimetypes
import os.path
from email.message import EmailMessage
message = EmailMessage()
sender = "me@example.com"
recipient = "you@example.com"
message["From"] = sender
message["To"] = recipient
message["Subject"] = f"Grretings from {sender} to {recipient}"
body = """Hey there

I'm learning to send emails using Python!"""
message.set_content(body)
print(message)

# The Content-Type and Content-Transfer-Encoding headers tell email clients and servers how to interpret the bytes in this email message into a string.

# In order for the recipient of your message to understand what to do with an attachment, you  need to label the attachment with a MIME type and subtype to tell them what sort of file you’re sending. The Internet Assigned Numbers Authority (IANA) (iana.org) hosts a registry of valid MIME types. If you know the correct type and subtype of the files you’ll be sending, you can use those values directly. If you don't know, you can use the Python mimetypes module to make a good guess!
print("------------------------------------------")
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_filename)
print(mime_type)
print(attachment_filename)


# Alright, that mime_type string contains the MIME type and subtype, separated by a slash. The EmailMessage type needs a MIME type and subtypes as separate strings, so let's split this up:

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)


# The entire message can still be serialized as a text string, including the image that we attached! The email message as a whole has the MIME type "multipart/mixed". Each part of the message has its own MIME type. The message body is still there as a "text/plain" part, and the image attachment is a "image/png" part. Cool!
print("-----------------------------------------------")

# With smtplib, we'll create an object that will represent our mail server, and handle sending messages to that server. If you’re using a Linux computer, you might already have a configured SMTP server like postfix or sendmail. But maybe not. Let's create a smtplib.SMTP object and try to connect to the local machine.

#mail_server = smtplib.SMTP('localhost')

# Oops! This error means that there's no local SMTP server configured. But don't panic! You can still connect to the SMTP server for your personal email address. Most personal email services have instructions for sending email through SMTP; just search for the name of your email service and "SMTP connection settings".

# When setting this up, there are a couple of things that you'll probably need to do: Use a secure transport layer and authenticate to the service using a username and password. Let's see what this means in practice.

# You can connect to a remote SMTP server using Transport Layer Security (TLS). An earlier version of the TLS protocol was called Secure Sockets Layer (SSL), and you’ll sometimes see TLS and SSL used interchangeably. This SSL/TLS is the same protocol that's used to add a secure transmission layer to HTTP, making it HTTPS. Within the smtplib, there are two classes for making connections to an SMTP server: The SMTP class will make a direct SMTP connection, and the SMTP_SSL class will make a SMTP connection over SSL/TLS. Like this:

mail_server = smtplib.SMTP_SSL('smtp.example.com')

# If you want to see the SMTP messages that are being sent back and forth by the smtplib module behind the scenes, you can set the debug level on the SMTP or SMTP_SSL object. The examples in this lesson won’t show the debug output, but you might find it interesting!

# mail_server.set_debuglevel(1)

# Now that we’ve made a connection to the SMTP server, the next thing we need to do is authenticate to the SMTP server. Typically, email providers wants us to provide a username and password to connect. Let's put the password into a variable so it's not visible on the screen.
print("---------------------------------------")
mail_pass = getpass.getpass('Password? ')
print(mail_pass)

# mail_server.login(sender, mail_pass) output: (235, b'2.7.0 Accepted')

# If the login attempt succeeds, the login method will return a tuple of the SMTP status https://datatracker.ietf.org/doc/html/rfc4954#section-6 code and a message explaining the reason for the status. If the login attempt fails, the module will raise a SMTPAuthenticationError https://docs.python.org/3.8/library/smtplib.html#smtplib.SMTPAuthenticationError exception.

# >>>>>>>>>>>If you wrote a script to send an email message, how would you handle this exception?

# mail_server.send_message(message)

# The send_message method returns a dictionary of any recipients that weren’t able to receive the message.
