from flask import Flask, render_template, request
from datetime import date
from email.mime.text import MIMEText
import sys
import smtplib

sys.dont_write_bytecode = True

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/order", methods=['POST'])
def order():
# the text file contains only ASCII characters.
# Create a text/plain message
    template = 'Name: {0}\nPhone: {1}\nDelivery Address: {2}\nOrder: {3}'
    elements = ['name', 'phone', 'address', 'order']
    args = [request.form[arg] for arg in elements]
    msg = MIMEText(template.format(*args))

    me = 'no-reply@noreply.net'
    #you = 'lukemeados@gmail.com'
    you = 'deanjohnson222@gmail.com'

# me == the sender's email address
# you == the recipient's email address
    msg['Subject'] = '[DELIVERY] Sent at %s.' % date.today()
    msg['From'] = me
    msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()
    return render_template("order_submitted.html")


app.run("127.0.0.1", 80, debug=True)
