parking_time = float(input('How many hours have you parked? '))

# The max parking time allowed is 2 hours.

if parking_time >= 2:
    print('Warning! You should move your car.')
    time_over = parking_time -2
    print('You are ' + str(time_over) + ' hours overdue')
else:
    print('You are ok for parking, you still have time.')
    time_left = 2 - parking_time
    print('You have ' + str(time_left) + ' hours left.')
