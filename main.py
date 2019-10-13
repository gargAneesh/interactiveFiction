print("When entering the options, please enter them exactly as presented.")

print("The world is ending")

print("The year is 69420, and Artificial Intelligence has taken control of the world. It is your job to find survivors and supplies. Be careful, most automated or electronic devices may be controlled by the enemies.")

print("You were across the country from your family studying mechanical engineering in college. When the first attack occured, you were flying back home.")

print("Unfortunately, your plane got controlled by AI and crash-landed into a lake. It is your job to find supplies and reach your family.")

print("You wake up in the plane and take off your seatbelt, seeing the destruction around you. You have 5 minutes before the plane sinks beneath the lake.")

q = int(input("Enter '1' if you want to help other passengers or enter '2' if you want to ignore the cries to gather supplies and escape the plane instead. "))

if q == 1:

    print ("You barely mananaged to escape with 3 other people. One is a doctor, the second is another student, and the third is a profesional athlete.")

    print("You enter a nearby town and see an abandoned warehouse.")

    s = int(input("Enter '1' to enter the warehouse or enter '2' to stay."))

    if s == 1:   

        print("As you enter the warehouse, you cut yourself on a rusty pipe. Luckily, the doctor has medical equipment that healed you. As you explore the warehouse, you find food and weapons.")

        t = int(input("With your newly found supplies you are able to make it to a new town. As you search through the town, you see a robot. You can either press '1' to attack the robot or press '2' to try and escape."))
    
        if t == 1:
            print("The robot sees your advance and shoots at you, killing you all.")
        
        elif t == 2: 
            
            print("You are able to escape safely and find your way to a police station, where you obtain weapons and a map. Additionally, you find a map of the surrounding region, seeing that your home town is only a 2 hour drive from here.")
            
            u = int(input("You follow the road out the town. Enter '1' if you want to follow the main road or enter '2' if you want to take a longer route that will add an hour to your journey."))
    
            if u == 1:
                
                print("The main road is patrolled by robots, that promptly capture and kill you.")\
            
            elif u ==2:
                
                print("You follow the road home, without any trouble. Unfortunately, when you arrive home, you find it empty.")
            
                v = int(input("Enter '1' if you want to stay home or enter '2' if you want to leave."))
                
                if v == 1:
                    
                    print("After a few days your family comes back. Unfortunately, your brother did not survive, as he was killed gathering resources while you were driving back. He left an hour before you arrived. ")
    
                elif v == 2:
                    
                    print("When you were searching for resources you got caught by a robot patrol, that shot you and your companions.")
    
elif s == 2: 

        print("Eventually, you go delirious due to a lack of water and kill the doctor. Later, you get cut on a twig and die without proper medical attention.")

elif q == 2:

    print ("You managed to gather supplies and escape the plane. However, the supplies were not good.")

    print("You enter a nearby town and see an abandoned warehouse")

    r = int(input("Enter '1' if you decide to go inside or enter '2' if you decide to stay with the supplies you have."))

    if r == 1:

        print("As you enter the warehouse, you get cut on a rusty pipe you tried pulling out. Without proper care, you die of an infected arm.")

    if r == 2:

        print("Your supplies are useless and you die of starvation.")
 
