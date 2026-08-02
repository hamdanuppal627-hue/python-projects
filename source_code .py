## --- File Reading ---
try:
    with open('f1.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("f1.txt does not exist yet. It will be created in the next step.")

# --- File Writing ---
with open("f1.txt", "w", encoding="utf-8") as file:
    file.write("I am the Coder OF ALL THE HISTORY")
print("Input has Successfully Been written into the File!")

# --- File Appending & Reading using "with" ---
with open("f2.txt", "a", encoding='utf-8') as file:
    input_user = input("Enter the Text you want to Add into the file: ")
    file.write(input_user)
with open("f2.txt", "r", encoding='utf-8') as file:
    print(f"\nYour File contains:\n{file.read()}")

