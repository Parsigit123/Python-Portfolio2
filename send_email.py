import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "parsova.khayatan@gmail.com"
password = "nkulsxlxzrvpxhvz"

receiver = "parsova.khayatan@gmail.com"
my_context = ssl.create_default_context()

message = """\
Subject: Hi!
Hello World!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)