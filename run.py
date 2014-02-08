from flask import Flask, render_template, request
from datetime import date
from email.mime.text import MIMEText
import sys
import smtplib


sys.dont_write_bytecode = True

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
# the text file contains only ASCII characters.
# Create a text/plain message
    if request.method == "POST":
        template = 'Name: {0}\nPhone: {1}\nDelivery Address: {2}\nOrder: {3}'
        elements = ['name', 'phone', 'address', 'order']
        args = [request.form.get(arg)for arg in elements]
        msg = MIMEText(template.format(*args))
        #msg = template.format(*elements)
        me = 'no-reply@noreply.net'
        #you = 'lukemeados@gmail.com'
        you = 'deanjohnson222@gmail.com'

# me == the sender's email address
# you == the recipient's email address
        msg['Subject'] = '[DELIVERY] Sent on %s.' % date.today()
        msg['From'] = me
        msg['To'] = you
# Send the message via our own SMTP server, but don't include the
# envelope header.
        fromaddr = 'noreply.zippyxpress@gmail.com'
        toaddrs  = 'zippyxpress@gmail.com'

# Credentials (if needed)
        username = ''
        password = ''

# The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()

        return render_template("order_submitted.html")
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)
