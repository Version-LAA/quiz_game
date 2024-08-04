"""
Game class to represent a game.
"""
from Quiz import Quiz,QUIZ_CATEGORIES
from Player import Player
import random
import csv
import os
from datetime import date
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

    def play_game(self,cat,lev):
        found_winner = False
        player_num = 1
        question_num = 1
        while found_winner is False:
            while player_num <= 2:
                opponent = self.players[2] if player_num == 1 else self.players[1]
                question = self.ask_question()
                current_player = self.players[player_num]
                if current_player.points == 2:

                    print(f"\n*[CURRENT PLAYER] Player{player_num} ({current_player.name}) - Score:[ {current_player.points} ] [** MATCH POINT **]\n")
                else:
                    print(f"\n*[CURRENT PLAYER] Player{player_num} ({current_player.name}) - Score:[ {current_player.points} ]\n")

                if opponent.points == 2:

                    print(f"Player2 ({opponent.name}) Score: [ {opponent.points} ] [** MATCH POINT **]\n")
                else:
                    print(f"Player2 ({opponent.name}) Score: [ {opponent.points} ]\n")

                print("---------------------------------------------")
                print(f"\nQuestion({question_num}): {question['question']['text']}\n")
                options_ls = [question['correctAnswer']] + question['incorrectAnswers']
                random.shuffle(options_ls)
                print("Pick an option from below:")
                for i,ans in enumerate(options_ls):
                    print(f"{i+1} - {ans}\n")
                choice = int(input("Choice: "))
                result = self.check_answer(question,options_ls[choice-1])
                if result:
                    current_player.points += 1
                if current_player.points == 3:
                    found_winner = True
                    print(f"\n CONGRATULATIONS - {current_player.name} you WON!")
                    print(f"\n Final score: ") # [TODO] - ADD SCORES
                    # [TODO] - WRITE TO DATABASE
                    stats = {
                        'date':date.today(),
                        'p1':self.players[1].name,
                        'p2':self.players[2].name,
                        'category':QUIZ_CATEGORIES[int(cat)],
                        'level':lev,
                        'winner':current_player.name
                    }
                    self.write_db(stats)
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
        for player in self.players: self.players[player].points = 0


    def write_db(self,log):
        headers = ['date','p1','p2','category','level','winner']
        if os.path.exists('gamedb.csv'):
            with open('gamedb.csv','a') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=headers)
                writer.writerow(log)
        else:
            with open('gamedb.csv','w') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=headers)
                writer.writeheader()
                writer.writerow(log)


    def read_db(self):
         headers = ['date','p1','p2','category','level','winner']
         hist = []
         if os.path.exists('gamedb.csv'):
            with open('gamedb.csv','r') as csvfile:
                reader = csv.DictReader(csvfile,fieldnames=headers)
                for r in reader:
                    hist.append(r)
         else:
           print("No history!")
         return hist

    def print_hist(self):
        history = self.read_db()
        print("** HISTORICAL MATCHUPS **")
        print("-------------------------\n")
        for h in history[1:]:
            print(f"* {h['date']} P1({h['p1']}) vs. P2({h['p2']}) Cat:({h['category']}) Lvl: ({h['level']}) WINNER(** {h['winner']} **)\n")
