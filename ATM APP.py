import random
u_name='abhishek'
pas='abhi.123'
s=[]
def login():
    id=input('Enter username: ')
    pswd=input('Enter password: ')
    s.append(id)
    s.append(pswd)
    checking()

def check(otp,otp_user):
    if(otp==otp_user):
        print("USERNAME: ",u_name)
        print("PASSWORD: "<pas)
    else:
        print("Wrong otp.Regenerating OTP") 
        otp_gen()   

def otp_gen():
    otp=int(random.randrange(1000,9999))
    print('Your OTP is; ',otp)
    print('Enter the OTP: ')
    otp_user =int(input())
    check(otp,otp_user)

def checking():
    if(u_name==s[0] and pas==s[1]) :
        print('LOGIN SUCESSFUL') 
    else:
        print("Incorrect username/password")
        print('press 1 to relogin')    
        print('press 2 if forgot username/password') 
        ch=int(input()) 
        if(ch==1):
            login()
        elif(ch==2):
            otp_gen()

login()            
