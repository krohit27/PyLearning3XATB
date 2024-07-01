numbers = [1, 2, 3, 4, 5]

#List - Collection of items

def do_something(RK_List):
    RK_List.append(6)
    RK_List[5] = 10
    return RK_List


l = do_something(numbers)
print(l)
