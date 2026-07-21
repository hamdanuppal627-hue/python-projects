import random
# used gpt to add 100 question my brain aint huge!!
quiz = {
    # Section 1: Mathematics
    "What number comes after 9?": "Ten",
    "What shape has 3 sides?": "Triangle",
    "What is 2 plus 3?": "Five",
    "What shape is a basketball?": "Sphere",
    "What number comes before 20?": "Nineteen",
    "How many days are in one week?": "Seven",
    "What is 10 minus 4?": "Six",
    "What shape looks like a doorway?": "Rectangle",
    "What number is half of 4?": "Two",
    "What tool tells us the time?": "Clock",
    "What is 5 plus 5?": "Ten",
    "What shape has no corners?": "Circle",
    "What is 8 minus 8?": "Zero",
    "Which number is larger: 12 or 21?": "21",
    "What coin is worth one cent?": "Penny",
    "How many fingers are on one hand?": "Five",
    "What is 0 plus 7?": "Seven",
    "What do you call a shape with 4 equal sides?": "Square",
    "What number comes next: 2, 4, 6, _?": "Eight",
    "What is 9 minus 1?": "Eight",
    "How many months are in a year?": "Twelve",
    "What is 6 plus 3?": "Nine",
    "What shape is an egg?": "Oval",
    "What number comes before 11?": "Ten",
    "What is 10 plus 20?": "Thirty",
    
    # Section 2: Science & Nature
    "What star shines during the day?": "Sun",
    "What do bees make?": "Honey",
    "What color is chlorophyll?": "Green",
    "What is frozen water called?": "Ice",
    "What body part do you use to hear?": "Ears",
    "What animal is known as the king of the jungle?": "Lion",
    "What season comes after winter?": "Spring",
    "What do caterpillars turn into?": "Butterflies",
    "What planet do we live on?": "Earth",
    "What gas do humans need to breathe?": "Oxygen",
    "What part of a tree grows underground?": "Roots",
    "What animal purrs and meows?": "Cat",
    "What do you call a baby dog?": "Puppy",
    "What falls from clouds during a storm?": "Rain",
    "What body part pumps your blood?": "Heart",
    "What is the tallest animal on land?": "Giraffe",
    "What color are bananas when they are ripe?": "Yellow",
    "What force pulls objects down to the ground?": "Gravity",
    "What animal can fly and has feathers?": "Bird",
    "What season is the hottest?": "Summer",
    "What do cows produce for us to drink?": "Milk",
    "What covering protects a turtle?": "Shell",
    "What do you call a baby bear?": "Cub",
    "What body part covers your entire exterior?": "Skin",
    "What type of tree keeps its leaves in winter?": "Evergreen",
    
    # Section 3: English & Language Arts
    "What is the first letter of the alphabet?": "A",
    "What is the opposite of hot?": "Cold",
    "What punctuation mark ends a regular sentence?": "Period",
    "What do you call a person, place, or thing?": "Noun",
    "What is the plural form of the word 'cat'?": "Cats",
    "What letter comes after T?": "U",
    "What is the opposite of up?": "Down",
    "How many letters are in the word 'dog'?": "Three",
    "What vowel is in the word 'pig'?": "I",
    "What is the opposite of big?": "Small",
    "What word rhymes with 'hat'?": "Cat",
    "What is the last letter of the alphabet?": "Z",
    "What color is created by mixing red and yellow?": "Orange",
    "What is the opposite of wet?": "Dry",
    "What do you call an action word?": "Verb",
    "What letter does the word 'apple' start with?": "A",
    "What is the opposite of day?": "Night",
    "What word rhymes with 'blue'?": "Glue",
    "What is the plural form of 'book'?": "Books",
    "What letter comes before M?": "L",
    "What is the opposite of fast?": "Slow",
    "What vowel is in the word 'sun'?": "U",
    "What word rhymes with 'toy'?": "Boy",
    "What is the opposite of happy?": "Sad",
    "How many vowels are in the English alphabet?": "Five",
    
    # Section 4: General Knowledge & Social Studies
    "What color means 'stop' on a traffic light?": "Red",
    "Who cooks food at a restaurant?": "Chef",
    "What do you use to cut paper?": "Scissors",
    "What building do you go to to learn?": "School",
    "Who flies an airplane?": "Pilot",
    "What meal do you eat in the morning?": "Breakfast",
    "What color means 'go' on a traffic light?": "Green",
    "Who helps sick animals?": "Vet",
    "What do you sleep on at night?": "Bed",
    "What do you wear on your feet before putting on shoes?": "Socks",
    "What country is famous for pyramids?": "Egypt",
    "Who puts out fires?": "Firefighter",
    "What do you use to clean your teeth?": "Toothbrush",
    "What meal do you eat at night?": "Dinner",
    "What object holds water in a backyard for swimming?": "Pool",
    "Who protects a city and catches criminals?": "Police",
    "What do you use to write on a chalkboard?": "Chalk",
    "What holiday features a decorated pine tree?": "Christmas",
    "What do you open to let fresh air into a room?": "Window",
    "What do you use to erase pencil mistakes?": "Eraser",
    "What is the name of the vehicle that takes kids to school?": "Bus",
    "Who teaches students in a classroom?": "Teacher",
    "What do you use to open a locked door?": "Key",
    "What do you use to shield yourself from rain?": "Umbrella",
    "What is the name of this game?": "Quiz"
}

chances = 3
flag = True

print("---------------------")
print("Welcome to Our Quiz! ")
print("---------------------")

while flag == True and chances > 0:
    print(f"\nYou have {chances} chances left!")
    choice = input("Do you want to Play a Quick Quiz? (yes/no): ").lower().strip()
    
    if choice == "yes":
        random_question = random.choice(list(quiz.keys()))
        print("\nYour Question is: ", random_question)
        
        answer = input("Enter your Answer: ").lower().strip()
        
        # Converted the dictionary value to lowercase to match the user's lowercase input
        if answer == quiz[random_question].lower().strip():
            print("You are Absolutely Right!")
        else:
            print(f"You are wrong! The correct answer was: {quiz[random_question]}")
            chances -= 1
            
        if chances == 0:
            print("\nGame Over! You ran out of chances.")
            flag = False
            
    elif choice == "no":
        flag = False
        print("\nThanks for playing! ")
    else:
        print("Invalid Input! Please type 'yes' or 'no'.")


