from flask_apscheduler import APScheduler
import ssl, smtplib, secret_config

scheduler = APScheduler()

def contact_form_email(name, email, subject, body):
    context = ssl.create_default_context()
    
    from_addr = 'noreply@yichenchong.com'
    to_addrs = ['yichenchong@yahoo.com', 'noreply@yichenchong.com']
    msg = f"""\
From: {from_addr}
To: {to_addrs[0]}
Subject: Webform email: {subject}
{body}

Sent by {name}, {email}"""
    
    with smtplib.SMTP_SSL(
        secret_config.current_mail_config["server"],
        port=secret_config.current_mail_config["port"],
        context=context
    ) as server:
        server.login(secret_config.current_mail_config["username"], secret_config.current_mail_config["password"])
        server.sendmail(from_addr, to_addrs, msg)
        server.quit()
    
    print("mail sent.")