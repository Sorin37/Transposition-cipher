import socket


def decrypt(word):
    key = 'copil'
    result = ''

    my_dict = {}
    step = len(word) / len(key)
    for nr, letter in zip(range(len(key)), "".join(sorted(key))):
        x = step * nr
        y = step * (nr + 1)
        my_dict[letter] = word[int(x):int(y)]

    word = ''
    for letter in key:
        word += my_dict[letter]

    for nr in range(int(step)):
        result += word[nr::int(step)]
    return result


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 3344

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    print("Server online!")

    close_connection = False
    while not close_connection:
        client, address = server.accept()
        # print(f"Connection established - {address[0]}:{address[1]}")

        string = client.recv(1024)
        string = string.decode("utf-8")
        print(string)
        print(decrypt(string))
        print()

        if 'Close connection' in decrypt(string)[0:len('Close connection')]:
            client.close()
            close_connection = True
