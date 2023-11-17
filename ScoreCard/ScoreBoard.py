# team1 = input("Enter Team One Name: ");
# team2 = input("Enter Team Two Name: ");
import time

wantToCont = "y"
team1=0
team2=0
Qes=0
print(" :: Welcome to Guess the Components ->> Connextion Game <<- :: \n")
print(" !! Games Rules : Rules are simple Guess the components using a Image !!\n")

while (wantToCont == "y"):
    ch = input("Points Goes to Team..")
    # 1,2 consider as Team 1, Team 2
    if ch == "1":
        team1+=1
    elif ch == "2":
        team2+=1

    # If Qestion are Exceed above 10 it will ask 
    Qes=Qes+1
    if Qes >= 10:
        wantToCont = input("Do you want to Contin this game score..Yes or No: ")
    #print(Qes)

print("\n<< Final Score Cards is >> ")
print("Team One Score is: " + str(team1))
print("Team Two Score is: " + str(team2))
time.sleep(10000)

