# This code is called: Do you have a dollar?

# I wrote a program that asks the user how many cents (penny coins) they have.
dollars_owned = int(input('How many cents do you have? '))

# If they have less than 100 cents, it will print the message 'you have less than a dollar'.
if dollars_owned <= 99:
    print('you have less than a dollar')
# Or, if the user has exactly 100 cents, the code will print the message 'you have exactly one dollar'
elif dollars_owned ==100:
    print('you have exactly one dollar')
# But if the user has more than 100 cents, the code will print the message 'you have more than one dollar'
else:
    print('you have more than one dollar')
