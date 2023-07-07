# Paisley Samuel
# BMME 8050 , Summer Semester
# Project 1 - circle.py

name = input("Please enter customer name:")
address = input("Please enter customer address:")
diam = eval(input("Please enter length of the diameter of the room (in feet):"))
rad = diam/2
area = (rad * rad) * 3.14
flr_cost = (2.00 * area)
inst_cost = (1.50 * area)

print("\nEstimate for",name,"\nlocated at",address, "\n")
print("\nCircular room with area of",area,"square feet")
print("Estimated cost for flooring material is $",flr_cost)
print("Estimated cost for installation is $",inst_cost)
print("\nTotal estimated cost is $",flr_cost + inst_cost)
