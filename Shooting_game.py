import random 

print("Welcome to the shooting Range!") 
print("HEALTH:|████████████|") 

health = 100 
zombies = 10 
bullets = 20 

print(f"{zombies} Zombies Are approaching you!!") 

while health > 0 and zombies > 0:
    if bullets <= 0:
        print("You ran out of bullets!")
        print("You died!")
        break
    decision = input("Do you want to Shoot (press Y) else press N to run: ").lower() 
    if decision == 'y': 
        shooter_decision = random.randint(0, 1) 
        if shooter_decision == 1: 
            zombies -= 1 
            print(f"\nYou killed a zombie! {zombies} are left!") 
        elif shooter_decision == 0:
            print("You missed!") 
            print("A zombie Attacked you") 
            health -= 10 
            print(f"You have {health} health left") 
        bullets -= 1 
        print(f"You Have {bullets} bullets left!") 
    elif decision == 'n': 
         print("You took cover!") 
         print("You Are SAFE!, BUT ZOMBIES are approaching you!!") 
         if health < 100: 
            health_chance = random.randint(0, 1) 
            if health_chance == 1: 
                health += 10 
                print(f"You Healed! Your health is {health}") 
            elif health_chance == 0: 
                print("THE BANDAGE GOT POISON ON IT!! Can't heal!") 
    else: 
        print("Invalid Input!\n")
if zombies == 0:
    print("Congratulations! You eliminated all the zombies and survived!")
elif health <= 0:
    print("Game Over. You were overwhelmed by the zombies.")
