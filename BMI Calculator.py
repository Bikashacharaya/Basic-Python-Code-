#def sum(a,b):
 #   x=a+b
  #  print("The sum is :",x)
#sum(5,2)    
print("--Welcome to BMI calculator--")
name=input("Enter your Name : ")
age=input("Enter your Age : ")
add=input("Enter your Address : ")
weight=float(input("Enter your Weight in kg : "))
height=float(input("Enter your Height in ft. : "))
height_into_meter=(height/10)*3
bmi=int(((weight/(height_into_meter**2))))
print("Hello, {}\n Age : {}\n Adresss : {} \n Weight : {}kg \n Height : {}ft \n Total Body Mass Index : {}  ".format(name,age,add,weight,height,bmi))

if bmi<=19:
  print("Report Classification: Under Weight")

elif bmi in range(20,25):
  print("Report Classification : Normal", ) 

elif bmi in range(25,30):
  print("Report Classification : Over Weight")

elif bmi in range(30,35):
  print("Report Classification : Obesity Class I")

elif bmi in range(35,40):
  print("Report Classification : Obesity Class II")

elif bmi >= 40:
  print("Report Classification : Extreme Obesity")

else:
  print("You are not Healthy !! ")

print("-Thankyou Stay Healthy :)-")



