import calculator.binary_operations as op
from calculator.representations import bin2int

a = bin2int((0, 1, 1))
b = bin2int((1, 0, 0, 0, 1, 1))

print(f"{a} + {b} = {op.add(a, b)}")
