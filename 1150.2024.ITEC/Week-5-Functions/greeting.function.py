def greeting(name):
    message = f'Hello {name}!!!!'
    return message.upper()

def main():
    username = 'Zoe'
    hello_message = greeting(username)
    print(hello_message)

main()
