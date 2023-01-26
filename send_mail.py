def send_mail(customer, dealer, rating, comments, email):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_content = f"<h3>Your Feedback Received!</h3><ul><li>Customer: {customer}</li><li>Email: {email}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    #The mail addresses and password
    sender_address = 'raavi.tejaswi1@gmail.com'
    sender_pass = 'xugozmvvlsnxiqlc'
    receiver_address = email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Thank you for your Feedback, Keep visiting.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

'''import smtplib
from email.message import EmailMessage


def send_mail(customer, dealer, rating, comments, email):
    port = 465
    smtp_server = 'smtp.gmail.com'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Email: {email}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'raavi.tejaswi1@gmail.com'
    sender_password='xugozmvvlsnxiqlc'
    receiver_email = email
    msg = EmailMessage(message, 'html')
    msg['Subject'] = 'PRCJ Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # context=ssl.create_default_context()

    # Send email
    with smtplib.SMTP_SSL(smtp_server, port) as smtp:
        smtp.login(send_mail, sender_password)
        smtp.sendmail(sender_email, receiver_email, msg.as_string())
'''