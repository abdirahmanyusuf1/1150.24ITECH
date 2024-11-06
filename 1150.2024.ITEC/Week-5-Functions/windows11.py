def main():
    # Asks the user for their memory, storage, and OS compatibility
    memory= int(input('How many GB of memory do you have? '))
    storage = int(input('How many GB of free storage space do you have? '))
    os_name = input('What is the name of the operating system you are currently running? ').lower()

    # Calls the "windows_11_compatible" function to check if the user can upgrade
    windows_11_compatible(memory, storage, os_name)


def windows_11_compatible(memory, storage, os_name):
    # Defines the minimum requirements for memory, storage, and OS compatiblity
    min_memory, min_storage_space, compatible_os = 8, 64, 'windows 10'

    # Conditional statements that check if the user meets the minimum requirements
    # Prints 'You can upgrade' if the conditions are met
    if memory >= min_memory and storage >= min_storage_space and os_name in compatible_os:
        print('You can upgrade')
    # Prints "You can't upgrade" if the conditions are not met
    else:
        print("You can't upgrade")


main()  # Calls the main function to start the program