

def print_hi(name):
    f = open('art.txt', 'r')

    print(''.join([line for line in f]))

    protocol = input('Which Protocol or Tool?: ')

    if protocol == 'ftp':
        a = open("Field_Guide/FTP.txt", "r")
        print(a.read())

    if protocol == 'snmp':
        b = open("Field_Guide/SNMP.txt", "r")
        print(b.read())

    if protocol == 'ike':
        b = open("Field_Guide/IKE.txt", "r")
        print(b.read())
    if protocol == 'smtp':
        b = open("Field_Guide/SMTP.txt", "r")
        print(b.read())

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
