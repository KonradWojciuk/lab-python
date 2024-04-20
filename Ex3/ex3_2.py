import smtplib
from email.message import EmailMessage

def read_config(filename):
    """
    Read configuration from file.

    Args:
    filename (str): The path to the configuration file.

    Returns:
        dict: A dictionary containing key-value pairs read from the configuration file.
        
    Example configuration file format:
    
    sender_email=sender emial
    sender_password=password
    recipient_email=recipient email
    subject=subject
    text=text
    """
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split("=")
            config[key.strip()] = value.strip()
    return config

def send_email(sender_email, sender_password, receiver_email, subject, message):
    msg = EmailMessage()
    msg['from'] = sender_email
    msg['to'] = receiver_email
    msg['subject'] = subject
    msg.set_content(message)
    

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()

    server.login(sender_email, sender_password)

    server.send_message(msg)

    server.quit()

def main():
    file_data = read_config('D:\\Projects\\python\\Cw3\\data.txt')

    sender_email = file_data['sender_email']
    sender_password = file_data['sender_password']
    recipient_email = file_data['recipient_email']
    subject = file_data['subject']
    text = file_data['text']
    send_email(sender_email, sender_password, recipient_email, subject, text)


if __name__ == "__main__":
    main()