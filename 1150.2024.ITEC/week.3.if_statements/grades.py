test_score = float(input('Please enter the test score, out of 100: '))

#Convert test score to a letter grade

if test_score >= 90:
    print('Your letter grade is an A')
elif test_score >= 80:
    print('Your letter grade is a B')
elif test_score >= 70:
    print('You letter grade is a C')
elif test_score >= 60:
    print('Your letter grade is a D')

else:
    print('Sorry, you failed the quiz')
