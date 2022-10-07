import smtplib
import os
import json
from email.message import EmailMessage

user_mail = ''
user_token = ''


def getCredentials():
    # getting environment variables for user email and app token
    try:
        global user_mail
        global user_token
        with open('credentials.json', 'r') as json_file:
            json_load = json.load(json_file)
        user_mail = json_load['USER_MAIL']
        user_token = json_load['USER_TOKEN']
    except Exception:
        print("Cannot read User Mail and App Password")
        exit()


def getMsg():
    # creating a EmailMessage object
    msg = EmailMessage()
    msg['To'] = input("Enter the recipient's mail :\n")
    msg['Subject'] = input("Enter the subject of the mail :\n")
    msg['From'] = os.environ.get('USER_MAIL')
    # setting message body
    message_body = input("Enter the message body :\n")
    msg.set_content(message_body)
    att_add = input("Do you want to add an attachment? (y/n):\n")
    if (att_add == 'y'):
        att_path = input(
            "Enter the file path(either relative or absolute) :")
        try:
            with open(att_path, 'rb') as f:
                file_data = f.read()
                file_name = f.name
        except Exception:
            print("Error in reading file path:")
            exit()
        # adding attachment to message
        # main type is set to application
        # and sub type to octet-stream
        # which will by default read any type of file
        msg.add_attachment(
            file_data,
            maintype='application',
            subtype='octet-stream',
            filename=file_name)
    return msg


def main():

    getCredentials()
    # creating a smtp gmail server with ssl on port 465
    # change the server from gmail.com to your prefered
    # domain using smtp.domain.org e.g .smtp.mail.yahoo.com
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        try:
            # logging in using your mail address and token
            print(user_mail, user_token)
            smtp.login(
                user_mail,
                user_token)
        except Exception:
            print("Invalid Login credentials")
            exit()
        # calling getMsg() function to get the message
        msg = getMsg()
        try:
            smtp.send_message(msg)
            print("Mail sent successfully!!")
        except Exception:
            print("Operation Failed. Mail not sent.")


main()
