address="北京大学信息管理系，北京 100871"
iCol=address.find("，")
#print(iCol)
sInstitute=address[0:iCol]
iSpace=address.find(" ")
#print(iSpace)
sCity=address[iCol+1:iSpace]
sPostcode=address[iSpace+1:]
print(sInstitute)
print(sCity)
print(sPostcode)