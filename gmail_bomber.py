import smtplib as m

print ('''
         _ _
    _(,_/ \ \____________
    |`. \_@_@   `.     ,'
    |\ \ .        `-,-'
    || |  `-.____,-'
    || /  /
    |/ |  |
`..     /   
\\   /    |
||  |      
\\ /-.    |
||/  /_   |
hh \(_____)-'_)
''')

ob = m.SMTP("smtp.gmail.com", 587)
ob.starttls()
ob.login("gmail id", "gmail password")
subject = "We are trying to hack your account"
body = "Hacking in process... 7%\nHacking in process... 19%\nHacking in process... 24%\nHacking in process... 39%\nHacking in process... 44%\nHacking in process... 59%\nHacking in process... 73%\nHacking in process... 85%\nHacking in process... 97%\nHacked! successfully. :D... 100%"
message = "Subject:{}\n\n{}".format(subject, body)
listOfAddress = ["yourMail@gmail.com"]
#for 500 mail
for i in range(0, 500):
    ob.sendmail("username...", listOfAddress, message)
ob.quit()
print("send mails successfully")