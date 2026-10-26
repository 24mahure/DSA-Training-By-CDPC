rec = {'name': 'pyhton', 'age': 20}

r = rec.copy()

print(id(r) == id(rec))
print(id(r))
print(id(rec))