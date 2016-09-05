
import sys
import hashlib

haslo = 'kogutlysy'
hasz_hasla = hashlib.md5(haslo.encode()).hexdigest()


def make_word(m, base_string=False):
    znaki = 'qwertyuiopasdfghjklzxcvbnm'
    for i in znaki:
        if base_string:
            string = base_string + i
        else:
            string = i

        if hashlib.md5(string.encode()).hexdigest() == m:
            print('Podane Haslo to: ' + string)
            sys.exit()
        elif len(string) < 5:
            make_word(m=m, base_string=string)


make_word(hasz_hasla)