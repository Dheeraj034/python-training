#Write a program to generate otp after taking user credential.


import random    
def login():
    global cred
    cred=('ansh','ansh@2004')
    s=[]
    uid=input("Enter username:")
    pwd=input("Enter password:")
    s.append(uid)
    s.append(pwd)
    check(cred,s)

def otp_check(otp,otp_user):
    if(otp==otp_user):
        print("USERNAME:",cred[0])
        print("PASSWORD:",cred[1])
    else:
        print("Wrong otp.Regenerating OTP")
        otp_gen()

def otp_gen():
    otp=int(random.randrange(1000,9999))
    print("Your OTP is:",otp)
    print("Enter the OTP:")
    otp_user=int(input())
    otp_check(otp,otp_user)
def check(cred,s):
    if(cred[0]==s[0] and cred[1]==s[1]):
        print("LOGIN SUCCESSFULLY")
    else:
        print("Incorrect username/password")
        print("press 1 to relogin")
        print("press 2 if forget username/password")
        ch=int(input())
        if(ch==1):
            login()
        elif(ch==2):
            otp_gen()


login()
            


        







            
    
    
