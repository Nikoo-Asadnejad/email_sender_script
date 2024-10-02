from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(subject, body, to_email):
    from_email = 'your_email@gmail.com'
    password = 'your_email_password'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

@app.route('/send-email', methods=['POST'])
def send_email_api():
    try:
        data = request.json
        subject = data.get('subject')
        body = data.get('body')
        to_email = data.get('toEmail')
        
        if not subject or not body or not to_email:
            return jsonify({'error': 'Missing required fields'}), 400
        
        send_email(subject, body, to_email)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)