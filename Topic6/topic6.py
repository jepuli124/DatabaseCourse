import sqlite3
db = sqlite3.connect('hw5tennis.db')
cur = db.cursor()
def initializeDB():
    try:
        f = open("sqlcommands.sql", "r")
        commandstring = ""
        for line in f.readlines():
            commandstring+=line
        cur.executescript(commandstring)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except:
        print("No SQL file to be used for initialization") 


def main():
    initializeDB()
    userInput = -1
    while(userInput != "0"):
        print("\nMenu options:")
        print("1: Print Players")
        print("2: Print Ranking")
        print("3: Print Matches")
        print("4: Search for one player")
        print("5: Move matchdate")
        print("6: Delete player")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            printPlayers()
        if userInput == "2":
            printRanking()
        if userInput == "3":
            printMatches()
        if userInput == "4":
            searchPlayer()
        if userInput == "5":
            moveMatch()
        if userInput == "6":
            deletePlayer()
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return

############## Do not touch part ends ##############
####################################################


############## Please modify the following ##############
def printPlayers():
    print("Printing players")
   
    cursor = db.cursor()
    for row in cursor.execute("SELECT * FROM Player"):
        print(row)
    #Start your modifications after this comment
    #You should print the data noe row at a time.


    return

def printRanking():
    print("Printing ranking")

    cursor = db.cursor()
    for row in cursor.execute("SELECT * FROM Ranking"):
        print(row)
    #Start your modifications after this comment
    #You should print the data noe row at a time.

    return

def printMatches():
    print("Printing matches")
    cursor = db.cursor()
    for row in cursor.execute("SELECT * FROM Matches"):
        print(row)
    #Start your modifications after this comment
    #You should print the data one row at a time.



    return

def searchPlayer():
    playerName = input("What is the player's surname? ")
    #print(playerName)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Player where Player.last_name = ?", (playerName,))
    #Start your modifications after this comment
    #You are given the print statements, now you need to add the fetched data to the five prints.
    listFetch = cursor.fetchone()
    print("ID:", listFetch[0])
    print("First name:", listFetch[1])
    print("Last name:", listFetch[2])
    print("Birthdate: ", listFetch[4])
    print("Nationality:", listFetch[3])


    return

def moveMatch():
    matchID = input("What is the matchID of the match you want to move? ")
    newMatchDate = input ("What is the new matchdate you want to set?")
    
    # """ 
    # Using the correct Python and SQL comands:
    # Change the match date based on the given matchID and new matchdate
    # IF a new matchdate is set to NULL, set the winner and result to NULL as well
    # """
    #Start your modifications after this comment
    cursor = db.cursor()

    if newMatchDate == "NULL" or newMatchDate == None:
        cursor.execute("UPDATE Matches Set matchDate = NULL, resultSets = NULL, winnerID = NULL  where Matches.matchid = ?", (matchID,))
    else:   
        cursor.execute("UPDATE Matches Set matchDate = ? where Matches.matchid = ?", (newMatchDate, matchID,))
    return

def deletePlayer():
    playerID = input("What is the player's PlayerID? ")
    # """ 
    # Using the correct Python and SQL comands:
    # Delete the Player and his Ranking information
    # Additionally, set the playerid to NULL in ALL match-data it is found
    # """
    cursor = db.cursor()
    cursor.execute("DELETE FROM Player where playerid = ?", (playerID,))
    cursor.execute("DELETE FROM Ranking where FK_playerid = ?", (playerID,))
    cursor.execute("UPDATE Matches Set FK_playerOne = NULL where Matches.FK_playerOne = ?", (playerID,))
    cursor.execute("UPDATE Matches Set FK_playerTwo = NULL where Matches.FK_playerTwo = ?", (playerID,))
    cursor.execute("UPDATE Matches Set winnerID = NULL where Matches.winnerID = ?", (playerID,))
  
    #Start your modifications after this comment



main()