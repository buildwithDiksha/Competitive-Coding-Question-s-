# Write a Python program to calculate the electricity bill of a customer based on the following rules:
# For first 100 units → ₹5 per unit
# For next 100 units (101–200) → ₹7 per unit
# For units above 200 → ₹10 per unit
# Add a fixed meter charge of ₹50

units = int(input("Enter the electricity units : "))
if (units<=100):
    bill = units*5
elif(units<=200):
    bill = (100*5)+(units-100)*7
else:
    bill = (100*5)+(100*7)+(units-200)*10

bill = bill+50

print("Bill = ₹",bill)