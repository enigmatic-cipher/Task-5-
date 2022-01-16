"""
Print table of 5 in following format using For loop.
Expected Output: 

5X1=5 
5X2=10 
. . 
5X10=50
"""

n = 5
pro = 0
for i in range(1,11):
  pro = n * i
  print(f"5 X {i} = {pro}")
