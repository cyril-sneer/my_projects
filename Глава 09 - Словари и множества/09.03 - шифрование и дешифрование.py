import my_funcs

CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',
        '{':'[','[':'{','}':']',']':'}'}

MENU = dict([("1", "Encode file"), ("2", "Decode file"), ("0", "Exit")])

def coding(file_name:str, enc = True):
        in_file = open(file_name)
        text = in_file.read()
        in_file.close()

        recoded_text = ''
        for char in text:
                if char.isspace():
                        recoded_text += char
                else:
                        recoded_text += CODE[char]

        suffix = "_encoded" if enc == True else "_decoded"
        encoded_file_name = file_name[:-4] + suffix + file_name[-4:]
        out_file = open(encoded_file_name, "w")
        out_file.write(recoded_text)
        out_file.close()


def main():
        while True:
                menu_choice = my_funcs.show_menu(MENU)
                if menu_choice == "0":
                    print(f"\nbye, bye..\n")
                    break
                elif menu_choice == "1":
                    input_file = input('Введите имя файла для кодирования: ')
                    coding(input_file)
                    print("\nEncoding done. To file name was added the '_encoded' suffix..\n")
                elif menu_choice == "2":
                    input_file = input('Введите имя файла для декодирования: ')
                    coding(input_file, enc=False)
                    print("\nDecoding done. To file name was added the '_decoded' suffix..\n")


if __name__ == '__main__':
    main()
