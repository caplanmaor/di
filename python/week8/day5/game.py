import random

class Game():
    def __init__(self):
        pass

    def get_user_item(self):
        user_input = ''
        while user_input != "rock" and user_input != "paper" and user_input != "scissors":
            user_input = input("choose rock paper or scissors: ")
        return user_input

    def get_computer_item(self):
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        return computer_choice

    def get_game_result(self, user_item, computer_item):
        if user_item == "rock" and computer_item == "paper":
            return "lose"

        if user_item == "rock" and computer_item == "scissors":
            return "win"

        if user_item == "rock" and computer_item == "rock":
            return "draw"

        if user_item == "paper" and computer_item == "scissors":
            return "lose"

        if user_item == "paper" and computer_item == "rock":
            return "win"

        if user_item == "paper" and computer_item == "paper":
            return "draw"

        if user_item == "scissors" and computer_item == "scissors":
            return "draw"

        if user_item == "scissors" and computer_item == "rock":
            return "lose"

        if user_item == "scissors" and computer_item == "paper":
            return "win"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item,computer_item)
        print(f'you chose {user_item}, the computer chose {computer_item}, you {result}')
        return result
