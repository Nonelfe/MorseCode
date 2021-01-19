#coding: utf-8

#----------------------
# morse code dictionary
#---------------------

class Morse():
        def __init__(self):
            self.morse_tables = self.MORSE_TABLES

        def error_check(self, datas):
            result = ''
            datas_list = datas.replace(' ', '')
            for data in list(datas_list):
                if data.isalpha():
                    data = data.upper()
                if not data in self.morse_tables.keys():
                    result = result + data
            if not result == '':
                print("Input ERROR : '{}'".format(result))
                return False
            return True


        MORSE_TABLES = {
                '1' : '･----',
                '2' : '･･---',
                '3' : '･･･--',
                '4' : '････-',
                '5' : '･････',
                '6' : '-････',
                '7' : '--･･･',
                '8' : '---･･',
                '9' : '----･',
                '0' : '-----',

                'A' : '･-',
                'B' : '-･･･',
                'C' : '-･-･',
                'D' : '-･･',
                'E' : '･',
                'F' : '･･-･',
                'G' : '--･',
                'H' : '････',
                'I' : '･･',
                'J' : '･---',
                'K' : '-･-',
                'L' : '･-･･',
                'M' : '--',
                'N' : '-･',
                'O' : '---',
                'P' : '･--･',
                'Q' : '--･-',
                'R' : '･-･',
                'S' : '･･･',
                'T' : '-',
                'U' : '･･-',
                'V' : '･･･-',
                'W' : '･--',
                'X' : '-･･-',
                'Y' : '-･--',
                'Z' : '--･･',

                '+' : '･-･-･',
                '-' : '-････-',
                '*' : '-･･-',
                '/' : '-･･-･',
                ':' : '-･･･-',
                '(' : '-･--･',
                ')' : '-･--･-',
                ':' : '---･･･',
                ',' : '--･･--',
                '.' : '･-･-･-',
                "'" : '･----･',
                '"' : '･-･･-･',
                '?' : '･･--･･',
                '@' : '･--･-･',
                }

def main(s):
    err_check = Morse()
    print(err_check.error_check(s))

if __name__ == '__main__':
    import sys
    args = sys.argv
    if 2 <= len(args):
        print("--*-- input test--*--")
        print("input: {}".format(args[1]))
        main(args[1])
    else:
        print('Arguments are too short')

