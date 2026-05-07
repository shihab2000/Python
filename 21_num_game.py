def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose1():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)


def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i += 1
    return True


def start1():
    xyz = []
    last = 0

    while True:
        print("\nEnter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input("> ")

        # ================= FIRST CHANCE =================
        if chance.upper() == "F":

            while True:
                if last == 20:
                    lose1()

                print("\nYour turn.")
                inp = int(input("How many numbers do you wish to enter? (1-3)\n> "))

                if inp < 1 or inp > 3:
                    print("Wrong input. You are disqualified.")
                    lose1()

                print("Enter your numbers:")
                for _ in range(inp):
                    xyz.append(int(input("> ")))

                if not check(xyz):
                    print("\nYou did not enter consecutive integers.")
                    lose1()

                last = xyz[-1]

                if last >= 21:
                    lose1()

                # Computer move
                comp = 4 - inp
                print("\nComputer's Turn:")

                for i in range(1, comp + 1):
                    xyz.append(last + i)

                last = xyz[-1]

                print("Numbers:", xyz)

        # ================= SECOND CHANCE =================
        elif chance.upper() == "S":

            xyz = []
            last = 0

            while last < 20:

                # Computer move
                comp = 1
                print("\nComputer's Turn:")

                for i in range(1, comp + 1):
                    xyz.append(last + i)

                last = xyz[-1]
                print("Numbers:", xyz)

                if last >= 21:
                    lose1()

                # User move
                print("\nYour turn.")
                inp = int(input("How many numbers do you wish to enter? (1-3)\n> "))

                if inp < 1 or inp > 3:
                    print("Wrong input.")
                    lose1()

                print("Enter your numbers:")
                for _ in range(inp):
                    xyz.append(int(input("> ")))

                if not check(xyz):
                    print("\nYou did not enter consecutive integers.")
                    lose1()

                last = xyz[-1]

                if last >= 21:
                    print("\n\nCongratulations!!!")
                    print("YOU WON!")
                    exit(0)

                near = nearestMultiple(last)
                comp = near - last

                if comp == 4:
                    comp = 3

        else:
            print("Wrong choice. Please enter F or S.")


# ================= MAIN MENU =================
while True:
    print("\nPlayer 2 is Computer.")
    ans = input("Do you want to play the 21 number game? (Yes/No)\n> ")

    if ans.lower() == "yes":
        start1()
    else:
        nex = input("Do you want to quit the game? (Yes/No)\n> ")

        if nex.lower() == "yes":
            print("You are quitting the game...")
            exit(0)
        elif nex.lower() == "no":
            print("Continuing...")
        else:
            print("Wrong choice")