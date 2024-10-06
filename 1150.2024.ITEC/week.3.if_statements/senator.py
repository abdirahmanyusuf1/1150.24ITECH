# This code asks the user if they can be a US senator

# First this code will ask what state they live in
senator_residency = str(input('What state do you live in? ')).upper()

# Then the code will ask how old they are
senator_age_restriction = int(input('How old are you? '))

# Next the code will ask how long they have been a US citizen
senator_citizenship = int(input('How long have you been a US citizen? '))

# Finally the code will ask what state they want to be a senator in
senator_state_application = str(input('What state do you want to be a senator in? ')).upper()

# Check eligibility

#If they apply for the same state they live in, over the age of 30 and have been a US citizen for longer than 9 years then they are eligible
if senator_residency == senator_state_application and senator_age_restriction >= 30 and senator_citizenship >= 9:
    print('You are eligible to be a US senator')
#But if they aren't
else:

    # If they aren't because they are applying to a different state
    if senator_residency != senator_state_application and senator_age_restriction >= 30 and senator_citizenship >= 9:
        print('You are ineligible because you are applying to be a senator in a different state than you live in')

    # If they aren't because they are applying to a different state and aren't 30 or older
    elif senator_residency != senator_state_application and senator_age_restriction < 30 and senator_citizenship >= 9:
        print('You are ineligible because you are applying to be a senator in a different state and are younger than 30')

    # If they aren't because they are applying to a different state and under the age of 30 and haven't been a US citizen for 9 years then they are ineligible
    elif senator_residency != senator_state_application and senator_age_restriction < 30 and senator_citizenship < 9:
        print("You are ineligible because you are applying to be a senator in a different state, you are under the age of 30, and you haven't been a US citizen for 9 years")

    # if they aren't because you haven't been a US citizen for more than 9 years
    elif senator_residency == senator_state_application and senator_age_restriction >= 30 and senator_citizenship < 9:
        print("You are ineligible because you haven't been a US citizen for 9 years")

    # if they aren't because they aren't 30 years old yet
    elif senator_residency == senator_state_application and senator_age_restriction < 30 and senator_citizenship >= 9:
        print("You are ineligible to be a senator because you aren't 30 years old yet")

    # if they aren't because you aren't 30 years old yet and haven't been a US citizen for more than 9 years
    elif senator_residency == senator_state_application and senator_age_restriction < 30 and senator_citizenship < 9:
        print("You are ineligible to be a senator because you aren't 30 years old yet and haven't been a US citizen for 9 years")

    # if they aren't because they are applying to be a senator in a different state and haven't been a US citizen for more than 9 years
    elif senator_residency != senator_state_application and senator_age_restriction >= 30 and senator_citizenship < 9:
        print("You are ineligible to be a senator because you are applying to be a senator in a different state and you haven't been a US citizen for 9 years")
