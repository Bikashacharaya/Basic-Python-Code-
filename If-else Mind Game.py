print("---Welcome to Do & Die Game---")
name=input("Enter your name? ")
age=int(input("Enter your age? "))
print("Hello {} you are {} year old ".format(name,age))

health=15
print("You are starting with",health, "Health")

if age>=18:
  print("You are old enough!")

  want_to_play=input(("Do you want to play? (Yes/No) "))

  if want_to_play=="Yes":
    print("Lets play!")

    left_or_right=input("First choice ... Left or Right(left/right)? ")

    if left_or_right=="left":

      ans=input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)")

      if ans=="around":
        print("You want around and reach the other side of the lake... ")
       
    
      elif ans=="across":
        print("You manage to get across, but were bit by a fish and lost 5 health...")
        health-= 5
       

      ans1=input("You notice a house and a river. Which do you go to (river/house)? ")  
      if ans=="house":
         print("You go to the house and are greted by the owner.. He doesnot like you and you loss 5 health")
         health-=5

         if health <=0:
          print("You now have 0 health and you lost the game...")

         else:
            print("You have have survived .. You win")


      else:
        print("You fell in the river and lost ")

        


           
      
  

    else:
      print("You feel down and lost....")  





  elif want_to_play=="No":
    print("Thankyou for visiting us...")

  else:
    print(input("Please Enter Valid Option (Yes/No)..."))

else:
    print("You are not old enough to play... ")





