# Dictionaries to be merged:
d1 = {"x": 1, "y": 4, "z": 10}
d2 = {"a": 7, "b": 9, "x": 5}

# Expected output after merging
# {'x': 5, 'y': 4, 'z': 10, 'a': 7, 'b': 9}
# ^^^^^ Notice that "x" got overridden by value from second dictionary

# 1. Option
d = dict(d1, **d2)
print(d)

# 2. Option
d = d1.copy()  # Copy the first dictionary
d.update(d2)   # Update it "in-place" with second one
print(d)

# 3. Option
d = {**d1, **d2}
print(d)

