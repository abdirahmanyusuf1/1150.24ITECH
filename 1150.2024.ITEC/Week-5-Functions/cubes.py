def main():
    for number in range(10):
        c = cube(number)
        print(c)

def cube(value):
    cube_value = value * value *value
    return cube_value

main()