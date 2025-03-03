def count(l):
    upper = sum(1 for char in l if char.isupper())
    lower = sum(1 for char in l if char.islower())
    print(upper)
    print(lower)
a = input("Enter a string:")
count(a)