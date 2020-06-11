import base64
import json


def check_user_exists(e):
    with open('users.txt', 'r') as f:
        for line in f:
            user = json.loads(line.strip())
            if user.get('email') == e:
                return user
    return False


def user_signup():
    email = input('Enter email ')
    name = input('Enter full name ')
    password1 = input('Enter password1 ')
    password2 = input('Enter password2 ')
    if check_user_exists(email):
        print('user already exists')
        return
    if not password1 == password2:
        print('passwords donot match')
        return
    pass_byte = base64.b64encode(password1.encode(encoding='UTF-8', errors='strict'))
    password = pass_byte.decode('UTF-8')

    user = json.dumps({
        "email": email,
        "name": name,
        "password": password
    })

    with open('users.txt', 'a') as text_file:
        text_file.write(user + '\n')
    print('user created successfully')

def user_login():
    email = input('Enter email ')
    password = input('Enter password ')
    user = check_user_exists(email)
    if not user:
        print('wrong email and password')
        return
    db = base64.b64decode(user['password'].encode(encoding='UTF-8', errors='strict'))
    if password == db.decode('UTF-8'):
        print('User login succesful')
    else:
        print('wrog email and password')
    
count = 0    
while True:
    decision = input('Enter s for Signup or l for login -> ').lower()
    if decision == 's':
        user_signup()
        break
    elif decision == 'l':
        user_login()
        break
    else:
        count +=1
        if count == 3:
            print('Out of trials')
            break
        else:
            print('Wrong input, try again')


