from datetime import datetime

def part_of_day_description(hour):
    if hour >= 0 and hour < 12:
        return 'Morning'
    elif hour >= 12 and hour < 18:
        return 'Afternoon'
    elif hour >= 18 and hour < 21:
        return 'Evening'
    else:
        return 'Night'

def main():
    current_time = datetime.now()
    current_hour = current_time.hour
    part_of_day = part_of_day_description(current_hour)
    user_name = input('Please enter your name: ')
    print(f'Good {part_of_day}, {user_name}')

main()

# Changes made in future