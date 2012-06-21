def is_power_of_two(number):
    # if number == 0:
    #     return False
    # if number == 1:
    #     return True
    # else:
    #     return (number & (number-1)) == 0
    # return (number != 0) and ((number & (number-1)) == 0)
    return (number & -number) == number

def which_power_of_two(number):
    if number == 1:
        return 0
    a = 0
    return which_power_of_two_r(number,a)

def which_power_of_two_r(number,a):
    if number == 0:
        return a-1
    else:
        return  which_power_of_two_r(number>>1,a+1)

def trailing_zeros(num):
    t = 0
    while not (num & 1):
        t += 1
        num = num >> 1
    return t

def trailing_ones(num):
    t = 0
    while (num & 1):
        t += 1
        num = num >> 1
    return t

num = int('1101000',2)

print trailing_zeros(num)

num = int('1101011',2)
print trailing_ones(num)

print is_power_of_two(2048), is_power_of_two(0), is_power_of_two(1), is_power_of_two(2)
print which_power_of_two(2048), which_power_of_two(4096), which_power_of_two(2**14)
