print("""Simple Rock-Paper-Scissors Game!!!""")

import random #Random is imported from python library

print("""You are to make a move by pressing either R, P or S while CPU make its move too""")

while True:
    new_list = { "R" : "Rock", "P" : "Paper", "S" : "Scissors"}

    try:
        comp_input = random.choice(list(new_list))
        new_input = input("Enter your choice: ").title() 
        #the input is capitalised to prevent error

        player = new_list[new_input]
        CPU = new_list[comp_input]

        if new_input in new_list.keys():
            if player == "Rock" and CPU == "Scissors":
                print(f"player ({player}) : CPU ({CPU}).")
                print("The final winner is player.")
                break

            elif player == "Paper" and CPU == "Rock":
                print(f"player ({player}) : CPU ({CPU}).")
                print("The final winner is player.")
                break

            elif player == "Scissors" and CPU == "Paper":
                print(f"player ({player}) : CPU ({CPU}).")
                print("The final winner is player.")
                break

            elif player == "Scissors" and CPU == "Rock":
                print(f"player ({player}) : CPU ({CPU}).")
                print("The final winner is CPU.")
                break

            elif player == "Rock" and CPU == "Paper":
                print(f"player ({player}) : CPU ({CPU}).")
                print("The final winner is CPU.")
                break

            elif player == "Paper" and CPU == "Scissors":
                print(f"player ({player}) : CPU ({CPU}).")
                print("The final winner is CPU.")
                break

            elif player == CPU:
                print("It is a tie. Repeat all over.")
                pass

            else:
                print("An invalid input")
    
    except:
        print("Error, the input is not in the list. Try again.")
        continue

    

