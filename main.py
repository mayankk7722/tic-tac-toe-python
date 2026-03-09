def intro():
    print("\n" * 2)
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 50 + "║")
    print("║" + "        🎮 TIC TAC TOE GAME 🎮        ".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("║" + "         Developed by Mayank         ".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("╚" + "═" * 50 + "╝")
    print("\n")
    print("           Press Enter to Start...")
    input()

def draw_screen():
    print("\n")
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 50 + "║")
    print("║            🤝 IT'S A DRAW 🤝            ".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("╚" + "═" * 50 + "╝")
    print("\n")

def winner_screen(player):
    print("\n")
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 50 + "║")
    print(f"║        🏆 PLAYER {player} WINS! 🏆        ".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("╚" + "═" * 50 + "╝")
    print("\n")

def exit_screen():
    print("\n")
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 50 + "║")
    print("║         👋 THANK YOU FOR PLAYING         ".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("╚" + "═" * 50 + "╝")
    print("\n")


def print_borad(borad):
    print("\n==============================")
    print("        ⚔ TIC TAC TOE ⚔")
    print("==============================\n")
    print("         0     1     2        ")
    print("        ---   ---   ---        \n")

    for i,row in enumerate(borad):
        print(f" {i} |     {row[0]}  ║  {row[1]}  ║  {row[2]}")
        if i < 2:
            print("       ═════════════════")
        else:
            print("\n==============================\n")

def check_win(borad,player):
     for row in borad:
         if row[0] == row[1] == row [2] == player:
             return True
         
     for col in range(3):
         if borad[0][col] == borad[1][col] == borad[2][col] == player:
             return True
         
     if borad[0][0] == borad[1][1] == borad[2][2] == player:
         return True

     if borad[0][2] == borad[1][1] == borad[2][0] == player:
         return True

     return False 

def check_draw(borad):
    for row in borad:
        if " " in row:
            return False
    return True

def play_game():
    borad =[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

    current_player ="X"
    
    intro()
    while True:
        print_borad(borad)
        
        try:
             row = int(input(f"Player {current_player} - Enter row (0-2): "))
             col = int(input(f"Player {current_player} - Enter colmuns (0-2): "))
        except ValueError:
            print("Invalid input. Enter numbers only.")
            continue
        
        if row not in range(3) or col not in range(3):
            print("\nRow and Column must be between 0 and 2.")
            continue

        if borad[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        borad[row][col] = current_player
        
        if check_win(borad, current_player):
            print_borad(borad)
            winner_screen(current_player)
            break

        if check_draw(borad):
            print_borad(borad)
            draw_screen()
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

while True:
    play_game()
    restart = input("Do you want to restart? (y/n): ").lower()
    if restart != "y":
        exit_screen()
        break


print(input("\nPress Enter to exit: "))
