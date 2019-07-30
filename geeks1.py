import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def checkemail(email):

    if (re.search(regex,email)):
        print("Valid Email")
    else:
        print("Email Address is not Valid")


if __name__ == '__main__':
    while(True):
        email = input("Enter Email Address")
        if email == 'Quit':
            break
        else:
            checkemail(email)
