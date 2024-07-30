"""
Game class to represent a game.
"""
from Quiz import Quiz
from Player import Player
import random
class Game:
    def __init__(self):
        self.players = {}
        self.winner = ''
        self.db = ''
        self.last_player_id = 1
        self.quiz = ''

    def add_players(self,players):
        # add player to game
        for player_name in players:
            self.players[self.last_player_id] = Player(player_name)
            self.last_player_id += 1
        self.last_player_id = 1
        return True

    def generate_quiz(self,category,level):
        q =  Quiz(category,level)
        self.quiz = q.questions


    def check_winner(self):
        return False

    def play_game(self):
        found_winner = False
        player_num = 1
        question_num = 1
        while found_winner is False:
            while player_num <= 2:
                question = self.ask_question()
                current_player = self.players[player_num]
                print(f"\nPlayer {player_num} ({current_player.name}) - Current Points: {current_player.points} \n")
                print(f"Question({question_num}): {question['question']['text']}\n")
                options_ls = [question['correctAnswer']] + question['incorrectAnswers']
                random.shuffle(options_ls)
                print("Pick an option from below:")
                for i,ans in enumerate(options_ls):
                    print(f"{i+1} - {ans}\n")
                choice = int(input("Choice: "))
                result = self.check_answer(question,options_ls[choice-1])
                if result:
                    current_player.points += 1
                if current_player.points == 4:
                    found_winner = True
                    print(f"\n CONGRATULATIONS - {current_player.name} you WON!")
                    print(f"\n Final score: ") # [TODO] - ADD SCORES
                    # [TODO] - WRITE TO DATABASE
                    break
                player_num += 1
            player_num = 1


    def ask_question(self):
        question = self.quiz.pop()
        return question

    def check_answer(self,question,answer):
        if answer == question['correctAnswer']:
            print("\nYou are correct! You have earned a point\n")
            return True
        print(f"\nSorry, the correct answer is {question['correctAnswer']}\n")
        return False

    def reset_game(self):
        for player in self.players: player.points = 0

    def rematch(self):
        pass

    def write_db(self):
        pass

    def read_db(self):
        pass
