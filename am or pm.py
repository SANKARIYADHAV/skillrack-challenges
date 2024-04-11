"""
INPUT:
00:00
OUTPUT:
AM
""
n=int(input())
h,m=n.split(":")
if(h>24 and m>60):
  print("INVALID INPUT")
elif(h>=12) and (h!=0):
  print("PM")
else:
  print("AM")
