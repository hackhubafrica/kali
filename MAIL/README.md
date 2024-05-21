use mail.py to send simple email

use mailattache if you need to send files



Explanation

    MIME Setup:
        The MIMEMultipart object is used to create a message that can contain multiple parts.
        MIMEBase is used to represent the attachment.

    File Attachment:
        The file is opened in binary mode and read into a MIMEBase object.
        The file content is encoded in base64 to ensure it is transmitted correctly.
        A header is added to specify the filename.
        The attachment is added to the MIMEMultipart message.

    Sending the Email:
        The email is sent to each recipient with the attachments included.

Notes

    Error Handling: The script includes basic error handling to catch and print exceptions.
    Security: Use environment variables or secure vaults to store sensitive information such as email passwords.
    File Paths: Ensure the paths to the attachments are correct.

By following this script, you can send emails with attachments, such as zip files or APKs, using Python.
