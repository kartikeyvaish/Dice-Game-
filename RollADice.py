import os
import time
import random

def Clear():
    os.system("CLS")

def Pause(a):
    time.sleep(a)

def Rules(PlayerOne, PlayerTwo):
    Pause(1)
    Clear()
    print("Rules Of the Game are very simple\n")
    Pause(2)
    print("Both of you will be given a dice...Both of you will roll the dice and it will be added to your points..")
    Pause(5)
    print(f"Suppose {PlayerOne} rolls the dice and 5 comes up, then 5 will be added to {PlayerOne}'s Points")
    Pause(6)
    print("Whoever reaches a decided point will win the match...So let's Begin..... ")
    Pause(5)
    Clear()

def RandomNumber(a,b):
    ch = random.randint(a, b)
    return ch

def DiceThrow():
    Pause(1)
    print("Dice Throw....", end="", flush=True)
    Pause(0.2)
    print("3.....", end="", flush=True)
    Pause(0.2)
    print("2.....", end="", flush=True)
    Pause(0.2)
    print("1.....", end="", flush=True)
    return random.randint(1,6)

def  CheckForWin(PlayerPoints, PointsToReach):
    if PlayerPoints >= PointsToReach:
        return 1
    else:
        return 0

def PrintingPoints(arr):
    sum = 0
    if(len(arr) > 1):
        for i in range(len(arr)):
            if i == (len(arr) - 1):
                sum = sum + arr[i]
                print(arr[i], " = ", end="")
            else:
                sum = sum + arr[i]
                print(arr[i], " + ", end="")
        print(sum)
    elif (len(arr) == 1):
        print(arr[0])
    else:
        print(sum)

def Game(PlayerOne, PlayerTwo, PointsToReach):
    turn = 0
    ch = ''
    Run = 1
    P1 = []
    P2 = []
    PlayerOnePoints = 0
    PlayerTwoPoints = 0
    while Run == 1:
        print(f"\t\tPoints to Reach has been decided as {PointsToReach}\n\n")
        print(f"{PlayerOne} Points - ", end="")
        PrintingPoints(P1)
        print(f"{PlayerTwo} Points - ", end="")
        PrintingPoints(P2)
        if turn % 2 == 0:
            print(f"{PlayerOne}'s Turn - ...Press F to Throw the Dice")
            ch = input()
            print("\n\n")
            Clear()
            sum = DiceThrow()
            PlayerOnePoints = PlayerOnePoints + sum
            P1.append(sum)
            print(f"And {sum} comes up..{PlayerOne} gets {sum} points ")
            if CheckForWin(PlayerOnePoints, PointsToReach) == 1:
                print(f"\n\n{PlayerOne} Points - ", end="")
                PrintingPoints(P1)
                print(f"{PlayerTwo} Points - ", end="")
                PrintingPoints(P2)
                print(f"\n\n{PlayerOne} Wins!")
                break
            Pause(1.5)
        if turn%2 != 0:
            print(f"{PlayerTwo}'s Turn - ...Press F to Throw the Dice")
            ch = input()
            Clear()
            sum = DiceThrow()
            PlayerTwoPoints = PlayerTwoPoints + sum
            P2.append(sum)
            print(f"And {sum} comes up..{PlayerTwo} gets {sum} points ")
            if CheckForWin(PlayerTwoPoints, PointsToReach) == 1:
                print(f"\n\n{PlayerOne} Points - ", end="")
                PrintingPoints(P1)
                print(f"{PlayerTwo} Points - ", end="")
                PrintingPoints(P2)
                print(f"\n\n{PlayerTwo} Wins!")
                break
            Pause(1.5)
        turn = turn + 1
        Clear()

def Main():
    print("\t\tWELCOME TO TIC TAC TOE GAME\n")
    PlayerOne = input("Enter Player One's Name - ")
    PlayerTwo = input("Enter Player Two's Name - ")
    Rules(PlayerOne, PlayerTwo)
    PointsToReach = RandomNumber(30, 60)
    Pause(1)
    Game(PlayerOne, PlayerTwo, 10)
    ch = input("\n\nEnter 1 to Play More")
    if ch == '1':
        Main()

Main()