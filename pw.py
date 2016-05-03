#! /usr/bin/python3.4
# pw.py  - Um programa para repositorio de senhas que nao e seguro.
import sys, pyperclip, getopt

PASSWORDS = {'email': 'bchjrhjhfjhsu',
                              'blog': 'd737ffyidcv',
                                'luggage': 'hfhjfisa'}

        
try:
    
    opts, args = getopt.getopt(sys.argv[1:], "a:s:", ["search","add"])
    
except getopt.GetoptError as err:
    print(str(err))
    print('Usage: python pw.py -a email_add')
    print('Usage: python pw.py -s email_pesquisado')


for o,a in opts:
    if o in ('-a','--add'):
        PASSWORDS['email']=a
    elif o in ('-s','--search'):
        if a in PASSWORDS:
            pyperclip.copy(PASSWORDS[a])
            print('Password for ' + a + ' copied to clipboard')
        else:
            print('There is no account named' + a)
    else:
        assert False, 'Unhandled Option'


