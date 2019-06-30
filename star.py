
star = "*"
space = " "
def build_pyramid():
    for i in range(9):
        print(space * (9 - 1- i), star * ((2 * i) +1))
build_pyramid()       
