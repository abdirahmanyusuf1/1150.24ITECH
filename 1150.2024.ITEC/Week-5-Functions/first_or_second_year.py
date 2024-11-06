def first_year_second_year(class_code):
    if 1000 <= class_code <= 1999:
        return 'First Year'
    elif 2000 <= class_code <=2999:
        return 'Second Year'
    else:
        return 'Invalid Code'

def main():
    code = int(input('Please enter class code: '))
    result = first_year_second_year(code)
    print(result)

main()