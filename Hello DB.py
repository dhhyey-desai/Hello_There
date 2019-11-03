
print("Hello there!")

integer = 0

running = True

process = True

while running:

    option = input("What do you want to do? \n1.Add \n2.View\n3.Remove\n")

    if option == str(1):

        name = input("Please enter your name\n")

        print("Hello! " + name)

        age = input("Please enter your age\n")

        newfile = open("newfile.txt", "a")

        string = (name + " " + age + "\n")

        newfile.write(string)

        newfile.close()

    if option == str(2):

        print("\nWho's age would you like to know?")

        # File that is being opened and reading it.
        newfile = open("newfile.txt", "r+")

        strings = [line for line in newfile.readlines()]

        num = len(strings)

        count = 0

        while count < num:

            string = strings[count:count + 1]

            str2 = str(string)[2:-4]

            name, age = str2.split(" ")

            print((str(count + 1)) + ". " + name)

            count = count + 1

        choice = int(input("Select your option\n"))

        name, age = strings[choice - 1].split(" ")

        print(age)

    if option == str(3):

        print("Who do you want to remove?")

        newfile = open("newfile.txt", "r+")

        strings = [line for line in newfile.readlines()]

        num = len(strings)

        count = 0

        while count < num:

            string = strings[count:count + 1]

            str2 = str(string)[2:-4]

            name, age = str2.split(" ")

            print((str(count + 1)) + ". " + name)

            count = count + 1

            newfile.close()

        newfile = open("newfile.txt", "r+")

        newfile.close()

        newfile = open("newfile.txt", "a+")

        choice = int(input("Select your option\n"))

        src_file = "newfile.txt"

        f = open(src_file, "r")

        contents = f.readlines()

        f.close()

        contents.pop(choice - 1)

        f = open(src_file, "w")

        contents = "".join(contents)

        f.write(contents)

        f.close()


