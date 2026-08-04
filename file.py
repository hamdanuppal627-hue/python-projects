# 1. Create and write to a file
with open("simple_demo.txt", "w") as file:
    file.write("Line 1: Hello Python!\n")

# 2. Append a new line to the same file
with open("simple_demo.txt", "a") as file:
    file.write("Line 2: Adding more data.\n")

# 3. Read and print the file line-by-line
print("--- Reading File Content ---")
with open("simple_demo.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes extra spacing
