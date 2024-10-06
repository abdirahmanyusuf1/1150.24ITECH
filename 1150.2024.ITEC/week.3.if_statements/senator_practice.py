import sys  # Import the sys module to use the exit() function

# This code asks the user if they can be a US senator

# First, this code will ask what state they want to be a senator in
senator_residing_currently = str(input('What state do you live in? ')).upper()

# Then the code will ask how old they are
senator_age_restriction = int(input('How old are you? '))
if senator_age_restriction < 30:
    print('You are not old enough to be eligible')
    sys.exit()  # End the program if the user is not eligible due to age
else:
    print('You are old enough to be eligible to be a senator')

# Next the code will ask how long they have been a US citizen
senator_citizenship = int(input('How long have you been a US citizen? '))
if senator_citizenship <= 8:
    print('You must wait until you have been a US citizen for 9 years to be eligible to be a US senator')
    sys.exit()  # End the program if the user is not eligible due to citizenship length
else:
    print('You are eligible to be a senator if you have been a US citizen for that long')

#The code will ask if the user what state they want to be a US senator for
senator_state_application = str(input('What state are you applying to be a senator in? ')).upper()
if senator_state_application.upper() != senator_residing_currently:
    print('You must be applying to be a senator in the state you live in')
    sys.exit() #End the program if the user is applying for a state that isn't the state he lives in
else:
    print('You are eligible to be a US senator living in your state')

#I used chatgpt to learn about sys.exit if the user wasn't eligible and end the code


#This code asks the user if they can be a US senator

#First this code will ask what state they live in
senator_residency = str(input('What state do you live in? ')).upper()

#Then the code will ask how old they are
senator_age_restriction = int(input('How old are you? '))

#Next the code will ask how long they have lived in the state they want to be a senator in
senator_citizenship = int(input('How long have you been a US citizen '))

#Finally the code will ask if they are a permanent resident in the state they want to be a senator in currently
senator_state_application = str(input('What state do you want to be a senator in? ')).upper()

#Now to check if they are eligible
#If they apply for the same state they live in, over the age of 30 and have been a US citizen for longer than 9 years then they are eligible
if senator_residency == senator_state_application and senator_age_restriction >=30 and senator_citizenship >=9:
    print('You are eligible to be a US senator')
#But if they aren't
else:

#If they aren't because they are applying to a different state
    if senator_residency != senator_state_application and senator_age_restriction >=30 and senator_citizenship >=9:
        print('You are ineligible because you are applying to be a senator in a different state than you live in')

#If they aren't because they are applying to a different state and aren't 30 or older
    elif senator_residency != senator_state_application and senator_age_restriction <29 and senator_citizenship >=9:
        print('You are ineligible because you are applying to be a senator in a different state than you live and are younger than 30')

#If they aren't because they are applying to a different state and under the age of 30 and haven't been a US citizen for 9 years then they are ineligible
    elif senator_residency != senator_state_application and senator_age_restriction <29 and senator_citizenship <8:
        print("You are ineligible because you are applying to be a senator in a different state, you are under the age of 30 and you haven't been a US citizen for more than 9 years")

#if they aren't because you haven't been a US citizen for more than 9 years
    elif senator_residency == senator_state_application and senator_age_restriction >=30 and senator_citizenship <8:
        print("You are ineligible because you haven't been a US citizen for more than 9 years")

#if they aren't because they aren't 30 years old yet
    elif senator_residency == senator_state_application and senator_age_restriction <29 and senator_citizenship >=9:
        print("You are ineligible to be a senator because you aren't 30 years old yet ")

#if they aren't because you aren't 30 years old yet and haven't been a US citizen for more than 9 years
    elif senator_residency == senator_state_application and senator_age_restriction <29 and senator_citizenship <8:
        print("You are ineligible to be a senator because you aren't 30 years old yet and haven't been a US citizen for more than 9 years")

#if they aren't because they are applying to be a senator in a different state and haven't been a US citizen for more than 9 years
    elif senator_residency != senator_state_application and senator_age_restriction >=30 and senator_citizenship <9:
        print("You are ineligible to be a senator because you are applying to be a senator in a different state and you haven't been a US citizen for more than 9 years")
