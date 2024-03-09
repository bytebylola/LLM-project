from flask import Flask, render_template,request
from flask_mail import Mail, Message
import os
app=Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lochana.prabha@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
@app.route('/home',methods=['GET',"POST"])
@app.route('/',methods=['GET',"POST"])
def home():
    if request.method=='POST':
        msg = Message('Hello', sender='norecepients@gmail.com' ,recipients=['lochana.prabha@gmail.com'] )
        msg.body = "This is the email body."
        mail.send(msg)
        return "sent email"
    return renter_template('index.html')
if '__name__' =='__main__':
    app.run(debug=True)
           
