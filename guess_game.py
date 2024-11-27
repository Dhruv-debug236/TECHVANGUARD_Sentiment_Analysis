name=['tarunjit','yuman','tarun']
count=0
while count<3:
    usr_input=input("Guess my name:")
    if usr_input in name:
        print("you win")
        break
    else:
     if count<3:
        print("try again")
        count=count+1
if count>=3:
    print("Game over") 