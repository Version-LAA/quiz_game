"""
Quiz class to represent a quiz object to use within a game.
"""
import requests
QUIZ_CATEGORIES = (
    "Music",
    "Sports and Leisure",
    "Film and TV",
    "Arts and Literature",
    "History",
    "Society and Culture",
    "Science",
    "Geography",
    "Food and Drink",
    "General Knowledge"
)

class Quiz:
    def __init__(self,type,difficulty):
        self.type = int(type)
        self.difficulty = difficulty
        self.quiz_category = ''
        self.questions = self.generate_quiz(self.type,self.difficulty)
        self.num_questions = len(self.questions)


    def generate_quiz(self,type,difficulty):
        # Generate quiz based on type and difficulty
        valid_quizes = {
            1:"music",
            2:"sport_and_leisure",
            3:"film_and_tv",
            4:"arts_and_literature",
            5:"history",
            6:"society_and_culture",
            7:"science",
            8:"geography",
            9:"food_and_drink",
            10:"general_knowledge"
        }

        params = {
            'categories':valid_quizes[type],
            'limit':50
        }
        url = 'https://the-trivia-api.com/v2/questions'
        response = requests.get(url,params=params)

        if difficulty == 1:
            filtered = [q for q in response.json() if q['difficulty'] == 'easy' or q['difficulty'] == 'medium' ]
        else:
            filtered = [q for q in response.json() if q['difficulty'] == 'hard']

        print(len(filtered))
        self.quiz_category = params['categories']
        return filtered
