# Dictionary Comprehension
lst = [(101, "imran"), (102, "mamun")]
dict1 = {k:v for k,v in lst}
print(dict1)
