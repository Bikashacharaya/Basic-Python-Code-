#Calculate Prime number using for loop and range fuctions
for i in range(1,200):
  count=0
  for j in range(1,i+1):
    if i%j==0:
       count=count+1
  if count==2:
   print(i)



