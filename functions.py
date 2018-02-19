def call_numbers():
    for number in range(0,10):
        print(number)

def call_numbers_with_limits(limit):
    for number in range(0,limit):
        print(number)

def calculater(x=10, y=15):
    return (x+y)


result = calculater(x=10, y=5)
print ("Result is", result)