# team1 = input("Enter Team One Name: ");
# team2 = input("Enter Team Two Name: ");

wantToCont = "y"
team1=0
team2=0
print(" :: Welcome to Guess the Components >> Connextion Game :: \n")
print(" !! Games Rules : Rules are simple Guess the components using a Image !!\n")

while (wantToCont == "y"):
    ch = input("Points Goes to..")
    if ch == "t1":
        team1+=1
    elif ch == "t2":
        team2+=1
    wantToCont = input("Do you want to Contin this game score..Yes or No: ")

print("Final Score Cards is >> ")
print("Team One Score is: " + str(team1))
print("Team Two Score is: " + str(team2))
