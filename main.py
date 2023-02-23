from array import array

print("app for arrays")

my_arr = array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def insert_to_arr():
    for i in range(10):
        print('enter', i + 1, 'num')
        my_arr[i] = int(input())


insert_to_arr()


def show():
    index = 0
    for i in my_arr:
        index = index + 1
        print('\n', 'my_arr[', index, '] = ', i)


show()

print('\n', 'MAX NUM IS', max(my_arr))


def find_max_value():
    max_value = my_arr[0]
    for i in my_arr:
        if i > max_value:
            max_value = i
    print('\n', 'max is', max_value)

# find_max_value()
