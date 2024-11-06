#First, I will write a code just for the first of the month


for month in range(1,32):
    if (month >10 and month <14):
        print(f'January {month}th') #This will print the month January and the day +1 because py starts from zero
    elif month % 10 ==1:
        print(f'January {month}st')
    elif month % 10 == 2:
            print(f'January {month}nd')
    elif month % 10 == 3:
        print(f'January {month}rd')
    else:
        print(f'January {month}th')



