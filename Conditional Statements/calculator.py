a=int(input("Enter a number :"))
b= int(input("Enter a number :"))
choice = int(input("Enter a choice : "))
switch={
    1:(a+b),
    2:(a-b),
    3:(a*b),
    4:(a/b)
}
print(switch.get(choice,"invalid choice"))



# dictionary.get(key,default_value)
