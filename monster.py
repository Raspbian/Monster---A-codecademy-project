#Whenever you see "Raspbian" That's Callum from Code Academy


inventory = []#This will be the inventory where we hold all items (Swords, drops/loot, etc.)

gold = 0 #I decided to keep gold seperate from inventory. This will be used to buy items and gold will be received after killing monsters or selling items


#Condensed profile and intro.
loop = True
while loop == True
    profile = raw_input("Hello. It's time to play our game! What do you want your profile to be called?:   ")
    if len(profile) >= 21:
        print "Profile name too long. Must be 20 characters or less."
        loop = True
    else:
        loop = False

print "Ok, ", profile, "let's play
print " You wake up in the middle of the forest with a huge headache. You can't remember anything. You turn over on your other side and groan. Suddenly, you see a huge, hulking figure smash his way into the woods and start attacking at you. He's using a club to hit you."#changed fight to fightOne, as I assume there will be multiple..
fightOne = raw_input("Do you 'fight back', or just 'dodge'?:   ") #Changed to fightOne, there will be more monsters!

#Fight back for monsterOne
if fightOne == "fight back"
    print "That was a bad decision. You end up dying without even remembering who you are." #REMEMBER TABS!(I've added in spaces and stuff, your welcome!)

loop = False #Why is this here? Loop has to be set to false way up to contine, and there is no other while loop....

elif fightOne == "dodge"
    print "You rollover, jump up (ignoring the pain) , give the guy a quick spinning snap kick, and then with accuracy so accurate it's scary, you give the guy a two handed chop to the top of his head. The head explodes and out bursts some money. You quickly collect the money, although you have no idea where this type of money is from, and start walking away. After a bit of walking you start to see a town."
    #How much gold for killing, someting like 37? Anyway, I've added 37 to total gold here -- Raspbian
    gold += 37 

decisionTownOne = raw_input("Do you walk towards it? walk/ignore:   ") # Renamed to decisionTownOne, as there will another decision I presume

#townOne
if decisionTownOne == "walk".downcase():
    print "You walk towars the town, everyone stares at you, like your wearing nothing. It's probably best to buy some clothes..."
    desicionBuyOne = raw_input("Do you wish to buy some clothes? yes/no:   ")
    
    #shopOne - Clothing
    if decitsionBuyOne == "yes".downcase():
        print "You walk up to the taylor, and he laughs. You ask him if you can see his catalogue. He willingly accepts."
        print "Hello, my names Mike, what's yours?"
        print profile + ", Mike."
        print "Nice to meet you %s" %profile
        print "Here's my catalogue %s." %profile
        print #Need to know date! -- Currently writing an AI for the boss, currently called Steve for test purposes. - Raspbian(Callum)


