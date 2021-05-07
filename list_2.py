def add_list_get_num(a, b, c):
    add_list_get_num = [value for value in (a, b) if isinstance(value, int) ]

    
li1 = [1, "red", 0, "blue", 1, "red", 0, "blue", 1, "red", 0, "blue", 1, 0]
li2 = [2, "white", 0, "white", 2, "white", 0, "white",  2, "white", 0,]
li3 = [value for value in li1 + li2 if isinstance(value, int)]

print(li3)