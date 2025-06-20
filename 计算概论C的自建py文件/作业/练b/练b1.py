length = int(input())
bike = length/3+50
walk = length/1.2
if bike < walk:
    print("Bike")
elif bike > walk:
    print("Walk")
else:
    print("All")