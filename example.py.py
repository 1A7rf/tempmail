import tempmail
temp=tempmail.tempMail()
temp.getNewMail(max_length=10,min_length=10)
print('email : '+temp.email,'token : '+temp.token)