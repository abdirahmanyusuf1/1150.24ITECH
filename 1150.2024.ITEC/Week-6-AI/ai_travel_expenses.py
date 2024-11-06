# Ask the user for the number of times they rode the bus last month
rides = int(input("Enter the number of times you rode the bus last month: "))

# Ask the user for the cost of one bus ride
cost_per_ride = float(input("Enter the cost of one bus ride: "))

# Calculate the total cost
total_cost = rides * cost_per_ride

# Print the result
print("You rode the bus " + str(rides) + " times last month. One bus ride costs $" + str(cost_per_ride) + ". Your total cost was $" + str(total_cost))
