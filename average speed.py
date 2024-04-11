""" A single line L with a set of space separated values indicating distance travelled and time taken is passed as the input. The program must calculate the average speed S (with precision upto 2 decimal places) and print S as the output.
Note: The distance and time taken will follow the format DISTANCE@TIMETAKEN. DISTANCE will be in kilometers and TIMETAKEN will be in hours.
Input Format:
The first line contains L.
Output Format:
The first line contains the average speed S.
Boundary Conditions:
Length of L will be from 3 to 100.
Example Input/Output 1:
Input:
60@2 120@3
Output:
36.00 kmph
Explanation:
Total distance = 60+120 = 180 km.
Total time taken = 2+3 = 5 hours.
Hence average speed = 180/5 = 36.00 kmph """

l=input().split()
s,t=0
for i in range(len(l)):
  speed,time=l[i].split("@")
  s+=speed
  t+=time
avg="{:.2f}".format(speed/time)
print(avg," kmph")

  
