def all_true(s):
    return all(s)
txt = tuple(map(int, input("Enter tuple elements:").split()))
result = all_true(txt)
print(result)