import sys
import time
import urllib.request


def large_print(intext, newlines=10):
    print('\n'*newlines)
    text = []
    for char in intext:
        text.append(char_to_ascii_block(char))
    chars = len(text)
    rows = len(text[0])
    cols = len(text[0][0])
    
    for row in range(rows):
        outrow = '  '
        for char in range(chars):
            thechar = text[char][row]
            if type(thechar) == tuple:
                thechar = ''.join(thechar)
            outrow += thechar + ' '
        print(outrow)


def get_external_ip():
    external_ip = '000.000.000.000'
    try:
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        # If 4 digits after the decimal point, remove the last digit
        if len(external_ip.split('.')[3]) == 4:
            external_ip = external_ip[0:2] + external_ip[3][0:2]
        return external_ip
    except:
        external_ip = '000.000.000.000'
    return external_ip


def char_to_ascii_block(char):
    unfilled = ' '
    filled = '▓'
    if char == '0':
        return ((filled*5),
                (filled, unfilled*3, filled),
                (filled, unfilled, unfilled, unfilled, filled),
                (filled, unfilled*3, filled),
                (filled*5))
    elif char == '1':
        return ((unfilled, filled*2, unfilled*2),
            (filled*3, unfilled*2),
                (unfilled*2, filled, unfilled*2),
                (unfilled*2, filled, unfilled*2),
                (filled*5))
    elif char == '2':
        return ((filled*5),
                (unfilled*4, filled),
                (filled*5),
                (filled, unfilled*4),
                (filled*5))
    elif char == '3':
        return ((filled*5),
                (unfilled*4, filled),
                (filled*5),
                (unfilled*4, filled),
                (filled*5))
    elif char == '4':
        return ((filled, unfilled*3, filled),
                (filled, unfilled*3, filled),
                (filled*5),
                (unfilled*4, filled),
                (unfilled*4, filled))
    elif char == '5':
        return ((filled*5),
                (filled, unfilled*4),
                (filled*5),
                (unfilled*4, filled),
                (filled*5))
    elif char == '6':
        return ((filled*5),
                (filled, unfilled*4),
                (filled*5),
                (filled, unfilled*3, filled),
                (filled*5))
    elif char == '7':
        return ((filled*5),
                (unfilled*4, filled),
                (unfilled*4, filled),
                (unfilled*4, filled),
                (unfilled*4, filled))
    elif char == '8':
        return ((filled*5),
                (filled, unfilled*3, filled),
                (filled*5),
                (filled, unfilled*3, filled),
                (filled*5))
    elif char == '9':
        return ((filled*5),
                (filled, unfilled*3, filled),
                (filled*5),
                (unfilled*4, filled),
                (filled*5))
    elif char == '.':
        return ((unfilled*5),
                (unfilled*5),
                (unfilled*5),
                (unfilled*5),
                (unfilled*2, filled, unfilled*2))
    else:
        raise ValueError('Invalid character')


def main():
    # Two blank lines
    print('\n\n')
    prev_external_ip, external_ip = None, None
    while True:
        prev_external_ip = external_ip
        external_ip = get_external_ip()
        if external_ip != prev_external_ip:
            large_print(external_ip)
        time.sleep(1)
        sys.stdout.write("\033[F" * 5) # Clears the previously printed lines

if __name__ == '__main__':
    main()

