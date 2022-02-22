from game import Game
session = Game()

def menu():
    user_input = input("choose play scores or quit: ")
    return user_input

def print_results(results):
    print(results)
    
    
def main():
    user_input = menu()
    all_results = {"win": 0,"lose": 0,"draw": 0}
    while user_input != "play" and user_input != "quit" and user_input != "scores":
        user_input = menu()

    while user_input != "quit":
        if user_input == "play":
            session_results = session.play()
            if session_results == "win":
                all_results["win"] += 1
            if session_results == "lose":
                all_results["lose"] += 1
            if session_results == "draw":
                all_results["draw"] += 1
            
        if user_input == "scores":
            print_results(all_results)
        user_input = menu()
    print_results(all_results)
main()

