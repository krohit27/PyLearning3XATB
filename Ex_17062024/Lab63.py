def print_argument(*args):  # ["ROHIT", "ANAND", "RK"]
    for i in args:
        print(i, end="\n")

print_argument("ROHIT", "ANAND", "RK")





# *args -> List
a = ["Rohit", "Anand", "ANNA"]
for i in a:
    print(i)


for i in range(1, 10):
    print(i)
#
# print_argument("pramod", "amit", "lucky")