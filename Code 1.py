def children():
    clothes=1
    water=1.5
    food=1
    blanket = 1.25
    mask = 0.05
    print("Do you have any young children?(yes/no)")
    children = input()
    if children == "no":
        print("\n***Checklist for a Flood***")
        print("Treking Rucksack - 1.1kg")
        print("Water Bottle - 1.5kg")
        print("2 Cans of Beans - 1kg")
        print("Jacket and Clothes - 1kg")
        print("Blanket - 1.25kg")
        print("Wind up Torch - 0.3kg")
        print("Mask - 50g")
        print("Small First Aid Kit - 0.2kg")
        print("ID or Personal Documentation\n")
        print("Total weight: 6.4kg")        
    elif children == "yes":
        numberofkids=int(input("How many children do you have?"))
        for n in range(numberofkids):
            age =int(input("How old are they?"))
            if age <=5:
                clothes = clothes + 1
                water= water+1.5
                food= food+1
                blanket = blanket +0.75
                mask=mask+0.05
                
        print("\n***Checklist for a Flood***")
        print("Treking Rucksack - 1.1kg")
        print("Childrens' Clothes - ",clothes," kg")
        print("Water Bottles - ",water," kg")
        print("Cans of beans - ",food," kg")
        print("Blankets - ",blanket," kg")
        print("Wind up Torch - 0.3kg")
        print("Mask - ",mask," kg")
        print("Small First Aid Kit - 0.2kg")
        print("ID or Personal Documentation\n")
            
        totalweight= (1.1+clothes+water+food+blanket+0.3+mask+0.2)
        print ("Total weight: ",totalweight, " kg")
 
def anotherperson():
    answer=input ("Are you with anyone?(yes/no)\n")
    if answer == "yes":
        print ("How many people are with you?\n")
        numberofpeople = input #+1??
        return numberofpeople


print ("Are you in danger? (yes/no)")
reply = input()
if reply == "yes":
    age=int(input("How old are you?\n"))
    if age<=13:
        adult=input ("Are you with an adult? (yes/no)\n")
        if adult == "no":
            anotherperson()
    elif age>=14 and age<=16:
        adult=input ("Are you with an adult?(yes/no)\n")
        if adult == "no":
            anotherperson()
    elif age>=17 and age<=65:
        anotherperson()
    print ("Do you want to call an emergency service?(yes/no)")
    callhelp = input().lower()
    if callhelp == "yes":
        print ("Calling...")
else:
    repeat = True
    while repeat == True:
        print("\n****Menu*****")
        print("Would you like to: \nA.play game \nB.get ready \nC.quit?")
        choice = input().lower()
        if (choice == "quit")or (choice == "c"):
            repeat = False
        elif (choice == "play game")or(choice == "a"):
            points=[]

            def questionone():
                print("\nWhat water source is safe to drink from?")
                print("\nA.River")
                print("B.Mountain stream")
                print("C.Lake")
                print("D.Sea\n")
                answer=input().lower()
                if (answer == "mountain stream")or (answer == "b"):
                    print ("Correct")
                    points.append(1)
                else:
                    print ("Incorrect. The right answer was 'Mountain Stream'")

            def questiontwo():
                print("\nWhat is the best food to bring in case of an emergency?")
                print("\nA.Cans of beans")
                print("B.Fruits")
                print("C.Packets of crisps")
                print("D.Burgers\n")
                answer=input().lower()
                if (answer == "cans of beans")or (answer=="a"):
                    print ("Correct")
                    points.append(1)
                else:
                    print ("Incorrect. The right answer was 'cans of beans'")


            print("This is an education game to raise awareness on what to do if natural disasters strike.\n")
##            print("Would you like to play?")
##            reply = input()
##            if reply == "no":
##                repeat = True
##                print ("ok")
##            else:
                
            questionone()
            questiontwo()
            print("You got ",len(points)," points.\n")
            returnmenu=input("Would you like to return to the menu?(yes/no)")
            if returnmenu == "yes":
                repeat = True
            else:
                repeat = False
        else:
            print("\nPlease type where you are.")
            area=input().lower()
            if area== "uk":
                print ("\nYou are in risk of flooding.")
                print ("Do you want to see: \nA.the flood checklist \nB.plan")
                floodreply = input().lower()
                if (floodreply == "checklist") or (floodreply == "a"):          
                    children()
                elif (floodreply == "plan") or (floodreply == "b"):
                    print("\n1.Pack your bag")
                    print("2.Check if friend and family are vulnerable")
                    print("3.Head for high ground")
                    print("4.Find shelter and call for help on an emergency help line\n")

            elif area == "philippines":
                print("You are in risk of: \nA.Flooding \nB.Earthquakes \nC.Tsunamis \nD.Volcanoes")
                danger = input().lower
                if (danger == "flooding") or (danger == "a"):
                    print ("Do you want to see the flood checklist or plan?")
                    floodreply = input().lower()
                    if floodreply == "checklist":          
                        children()
                    elif floodreply == "plan":
                        print("1.Pack your bag")
                        print("2.Check if friend and family are vulnerable")
                        print("3.Head for high ground")
                        print("4.Find shelter and call for help on an emergency help line")
                    
                
            
            returnmenu=input("\nWould you like to return to the menu?(yes/no)")
            if returnmenu == "yes":
                repeat = True
            else:
                repeat = False

            
