#coding: utf-8

#----------------------
# morse code dictionary
#---------------------

class Morse():
        def __init__(self):
            self.morse_tables = self.MORSE_TABLES

        def error_check(self, datas):
            result = ''
            for data in list(datas):
                if data == ' ':
                    continue
                if data.isalpha():
                    data = data.upper()
                get_value = self.morse_tables.get(data, False)
                if not get_value:
                    result += data
            if not result == '':
                print("Input ERROR : '{}'".format(result))
                return False
            return True

        def encode(self, datas):
            result = ''
            datas_list = datas.replace(' ', '')
            for data in list(datas_list):
                if data.isalpha():
                    data = data.upper()
                result += self.morse_tables.get(data) + ' '
            return result

        def decode(self, datas, wabun=False):
            from string import ascii_uppercase
            from string import digits

            alpha = ascii_uppercase
            alphanum = alpha + digits
            result = ''
            data_list = datas.split()
            for data in data_list:
                for key, value in self.morse_tables.items():
                    if data == value:
                        if wabun:
                            if not key in alpha:
                                result += key
                        else:
                            if key in alphanum:
                                result += key
            return result

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

                'イ' : '･-',
                'ロ' : '･-･-',
                'ハ' : '-･･･',
                'ニ' : '-･-･',
                'ホ' : '-･･',
                'ヘ' : '･',
                'ト' : '･･-･･',
                'チ' : '･･-･',
                'リ' : '--･',
                'ヌ' : '････',
                'ル' : '-･--･',
                'ヲ' : '･---',
                'ワ' : '-･-',
                'カ' : '･-･･',
                'ヨ' : '--',
                'タ' : '-･',
                'レ' : '---',
                'ソ' : '---･',
                'ツ' : '･--･',
                'ネ' : '--･-',
                'ナ' : '･-･',
                'ラ' : '･･･',
                'ム' : '-',
                'ウ' : '･･-',
                'ヰ' : '･-･･-',
                'ノ' : '･･--',
                'オ' : '･-･･･',
                'ク' : '･･･-',
                'ヤ' : '･--',
                'マ' : '-･･-',
                'ケ' : '-･--',
                'フ' : '--･･',
                'コ' : '----',
                'エ' : '-･---',
                'テ' : '･-･--',
                'ア' : '--･--',
                'サ' : '-･-･-',
                'キ' : '-･-･･',
                'ユ' : '-･･--',
                'メ' : '-･･･-',
                'ミ' : '･･-･-',
                'シ' : '--･-･',
                'ヱ' : '･--･･',
                'ヒ' : '--･･-',
                'モ' : '-･･-･',
                'セ' : '･---･',
                'ス' : '---･-',
                'ン' : '･-･-･',
                '゛' : '･･',
                '゜' : '･･--･',
                'ー' : '･--･-',
                '、' : '･-･-･-',
                '（' : '-･--･-',
                '）' : '･-･･-･',
        }

def main(s):
    morse = Morse()
    result = morse.error_check(s)
    print("error check: {}".format(result))
    if not result:
        exit()
    d = morse.encode(s)
    print("encode: {}".format(d))
    print("decode: {}".format(morse.decode(d)))
    print("decode wabun: {}".format(morse.decode(d, wabun=True)))

if __name__ == '__main__':
    import sys
    args = sys.argv
    if 2 <= len(args):
        print("--*-- input test--*--")
        print("input: {}".format(args[1]))
        main(args[1])
    else:
        print('Arguments are too short')

