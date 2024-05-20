import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import os

def send_email(smtp_server, port, login, app_password, subject, body, recipients, attachment_paths=None):
    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(login, app_password)

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = login
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Attach files
        if attachment_paths:
            for file_path in attachment_paths:
                # Open the file in binary mode
                with open(file_path, 'rb') as attachment:
                    # Create a MIMEBase object
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    # Encode file in ASCII characters to send by email
                    encoders.encode_base64(part)
                    # Add header to the attachment
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename={os.path.basename(file_path)}',
                    )
                    # Attach the MIMEBase object to the message
                    message.attach(part)

        # Send the email to each recipient
        for recipient in recipients:
            message['To'] = recipient
            text = message.as_string()
            server.sendmail(login, recipient, text)
            print(f'Email sent to {recipient}')

        # Disconnect from the server
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

def read_recipients_from_csv(csv_file):
    recipients = []
    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                recipients.append(row[0])  # Assuming email addresses are in the first column
    except Exception as e:
        print(f"Failed to read CSV file: {e}")
    return recipients

if __name__ == '__main__':
    # Configuration
    smtp_server = 'smtp.gmail.com'
    port = 587
    login = 'crimsonsummer81@gmail.com'
    app_password = 'fble xbfw oeea axle'  # Use the app-specific password here
    subject = 'AI and Machines'
    body = 'This is so AWESOME!!!!'

    # Load recipients from a CSV file
    csv_file = 'recipients.csv'
    recipients = read_recipients_from_csv(csv_file)

    # File paths to attach
    attachment_paths = ['./Screenshot_12.zip'] #, 'path/to/your/file.apk'

    # Send emails
    send_email(smtp_server, port, login, app_password, subject, body, recipients, attachment_paths)
