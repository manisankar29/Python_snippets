def email_slicer(email):
    username, domain = email.split('@')

    print(f'Username: {username}')
    print(f'Domain: {domain}')
    
print("Welcome to Simple Email Slicer!")
user_email = input('Enter your email address: ')

email_slicer(user_email)
