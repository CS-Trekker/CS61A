n = int(input())
lst = []
for i in range (n):
    length = int(input())
    bike = length/3+50
    walk = length/1.2
    if bike < walk:
        lst.append("Bike")
    elif bike > walk:
        lst.append("Walk")
    else:
        lst.append("All")
for i in lst:
    print(i)