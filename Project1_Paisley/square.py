# Paisley Samuel
# BMME 8050 , Summer Semester
# Project 1 - square.py

name = input("Please enter customer name:")
address = input("Please enter customer address:")
dim1 = eval(input("Please enter length of side 1 of the room (in feet):"))
area = (dim1 * dim1)
flr_cost = (2.00 * area)
inst_cost = (1.50 * area)

print("\nEstimate for",name,"\nlocated at",address, "\n")
print("\nSquare room with area of",area,"square feet")
print("Estimated cost for flooring material is $",flr_cost)
print("Estimated cost for installation is $",inst_cost)
print("\nTotal estimated cost is $",flr_cost + inst_cost)
