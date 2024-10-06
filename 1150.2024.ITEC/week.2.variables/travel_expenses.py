# Write a program that calculates the amount of money spent on bus fares last month.
# Ask the user for the number of times they rode the bus last month (what data type do you need to convert the input to?) and save in a variable.
num_of_times_rode_on_bus = int(input('How many times did you ride the bus last month? '))
# Ask the user for the cost of one bus ride (what data type do you need to convert the input to?) and save in another variable.
cost_of_bus_ride = float(input('How much does it cost to ride the bus? '))
# Calculate the total cost of riding the bus last month. Multiply the two variables and store the result in a new variable.
price_of_riding_the_bus_last_month = num_of_times_rode_on_bus * cost_of_bus_ride
# Print the number of rides, the cost of one bus ride, and the total cost for the user. Convert numeric variables to strings.
print('You rode the bus ' +str(num_of_times_rode_on_bus) + ' times last month. ')
print('The bus costed $' + str(cost_of_bus_ride) + ' last month.')
print('You spent $' + str(price_of_riding_the_bus_last_month) + ' riding the bus last month.')

