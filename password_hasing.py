import bcrypt

password=b"Thisismypassword"
newpass=bcrypt.hashpw(password, bcrypt.gensalt())
print(newpass)


enter_pass=input('enter password to login :')
enter_pass=bytes(enter_pass,'utf-8')
if bcrypt.checkpw(enter_pass,newpass):
    print('login successful.')

else:
    print('worng password entered.')
