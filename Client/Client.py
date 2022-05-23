import socket


def encrypt(word):
    key = 'copil'
    trailing_letter = 'a'
    result = ''

    # adding the trailing letters
    while len(word) % len(key) > 0:
        word = word + trailing_letter
        trailing_letter = chr(ord(trailing_letter) + 1)

    my_dict = {}
    for nr, letter in zip(range(len(key)), key):
        enc_letter = word[nr::len(key)]
        my_dict[letter] = enc_letter

    for letter in "".join(sorted(key)):
        result += my_dict[letter]
    return result


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 3344

    close_connection = False
    while not close_connection:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((ip, port))

        string = input("Enter string: ")
        if string == 'Close connection':
            close_connection = True
        server.send(bytes(encrypt(string), "utf-8"))
