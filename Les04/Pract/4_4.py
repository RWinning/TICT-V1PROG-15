oudwachtwoord = 'Geheim'

def new_password(x):
    if x == oudwachtwoord:
        print('zelfde als oud wachtwoord')
    elif len(x) >= 6:
        newpassword = x
        print('Je wachtwoord is veranderd')
    else:
        print('wachtwoord is niet lang genoeg')


newpassword =input('geef new wachtwoord: ')
new_password(newpassword)

