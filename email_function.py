import smtplib

def email_send_funct (to_,subj_,msg_,from_,pass_):
    #print(to_)
    #print(subj_)
    #print(msg_)
    #print(from_)
    #print(pass_)
    s=smtplib.SMTP("smtp.gmail.com",587) #Create session for gmail
    s.starttls() #transport layer
    s.login(from_,pass_)
    msg = "Subject: {}\n\n{}".format(subj_,msg_)
    s.sendmail(from_,to_,msg)
    x=s.ehlo()
    if x [0]==250:
        return 's'
    else:
        return 'f'
    s.close()

