from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ruthvikreddyanugu@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'Sonusonu@143'  # Replace with your email password or app password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        phone = data['phone']
        message = data['message']

        # Email to yourself
        msg_to_self = Message(
            subject=f"New Contact Form Submission from {firstname} {lastname}",
            recipients=['ruthvikreddyanugu@gmail.com'],  # Replace with your email
            body=f"Name: {firstname} {lastname}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
        )
        mail.send(msg_to_self)

        # Confirmation email to the user
        msg_to_user = Message(
            subject="Thank you for contacting us!",
            recipients=[email],
            body=f"Dear {firstname},\n\nThank you for reaching out! We have received your message and will get back to you shortly.\n\nBest regards,\n[Your Company/Name]"
        )
        mail.send(msg_to_user)

        return jsonify({'message': 'Emails sent successfully!'}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Error sending emails.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
