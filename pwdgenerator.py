import secrets
import string
import argparse

def create_password(include_lowercase=True, include_uppercase=True,
                include_digits=True, include_special_chars=True,
                length=12) -> str:
    
    if(length == 0):
        raise Exception("You can't have a password length of zero!")

    alphabet = ''
    if(include_lowercase):
        alphabet += string.ascii_lowercase
    if(include_uppercase):
        alphabet += string.ascii_uppercase
    if(include_digits):
        alphabet += string.digits
    if(include_special_chars):
        alphabet += string.punctuation

    if (len(alphabet) == 0):
        raise Exception("You need to select at least one option!")
    
    return ''.join(secrets.choice(alphabet) for i in range(length))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A simple Python-based CLI application that allows a quick and easy way to generate strong passwords without hassle.')
    
    parser.add_argument('length', type=int, default=12, help='Length of password to generate. Recommended length is twelve chars.')
    parser.add_argument('-ex_lowercase', '--lc', dest='lc', default=True, action='store_false', help='Exclude lowercase letters in password generation. Included by default.')
    parser.add_argument('-ex_uppercase', '--uc', dest='uc', default=True, action='store_false', help='Exclude uppercase letters in password generation. Included by default..')
    parser.add_argument('-ex_digits', '--d', dest='d', default=True, action='store_false', help='Exclude digits letters in password generation. Included by default.')
    parser.add_argument('-ex_special_chars', '--sc', dest='sc', default=True, action='store_false', help='Exclude special chars letters in password generation. Included by default.')
    parser.add_argument('-verbosity', '--v', default=False, action='store_true', dest='v', help='Increase detail output')
    
    args = parser.parse_args()

    if(args.v == True):
        print(f'Password generation details: ')
        print(f'--> Length: {args.length} characters')
        print(f'--> Uppercase chars included: {args.uc}')
        print(f'--> Lowercase chars included: {args.lc}')
        print(f'--> Digits included: {args.d}')
        print(f'--> Special chars included: {args.sc}')

    print("Password generated: " + 
        create_password(
            length=args.length,
            include_uppercase=args.uc,
            include_lowercase=args.lc,
            include_digits=args.d,
            include_special_chars=args.sc
        )
    ) 

else:
    pass # do nothing intentionallly