import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments, email):
    port = 587
    smtp_server = 'smtp.gmail.com'
    login = '7dbaa1350891c0'
    password = '45b99f920a5a9f'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Email: {email}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'raavi.tejaswi1@gmail.com'
    receiver_email = email
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'PRCJ Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
