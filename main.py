

def print_hi(name):
    f = open('art.txt', 'r')

    print(''.join([line for line in f]))

    protocol = input('Which Protocol or Tool?: ')



    if protocol == 'ftp' or '21':
       f = open("Field_Guide/FTP.txt", "r")
       print(f.read())
    else:
       print(f'PROTOCOL NOT FOUND')


   # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
