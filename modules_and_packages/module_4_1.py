from fake_math import divide as fake_div
from true_math import divide as true_div

result1 = fake_div(69, 3)
result2 = fake_div(3, 0)
result3 = true_div(49, 7)
result4 = true_div(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
