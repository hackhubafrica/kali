import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def send_email(smtp_server, port, login, password, subject, body, recipients):
    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(login, password)

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = login
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

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
    password = 'fble xbfw oeea axle'
    subject = 'Your Subject Here'
    body = 'Your email body here.'

    # Load recipients from a CSV file
    csv_file = 'recipients.csv'
    recipients = read_recipients_from_csv(csv_file)

    # Send emails
    send_email(smtp_server, port, login, password, subject, body, recipients)
