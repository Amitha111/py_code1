
l1 = [9, "roses", 0.9, 12, "butterfly", 15.9, "lavenders"]
l2 = ["daffodils", 1.8, "tulips", 10, 56, "lillies", 33, "wasp"]
l3 = [89, "pollen", "weeds", 87, 99.9, "humming", 34, "scent", 0.6]
l4 = []
## Just for the all list combine use concatenation like l1 + l2 + l3 without the filter using isinstance
l4 = [value for value in l1 + l2 + l3 if isinstance(value, str)]


print(l4)