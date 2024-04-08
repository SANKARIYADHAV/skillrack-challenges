"""
INPUT:
11
OUTPUT:
13
"""
#get the input from the user
n=int(input())
while True:
  n+=1
  for i in range(2,n):
    if n%i==0:
      break
    else:
      print(n)
      break
