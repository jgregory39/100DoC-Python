import requests
from string import ascii_uppercase, digits
from random import choice

QUESTIONS = 10


def get_categories():
    response = requests.get(url='https://opentdb.com/api_category.php')
    category_data = response.json()["trivia_categories"]
    cat_list = [cat['name'] for cat in category_data]
    return cat_list


def get_cat_id(category):
    if category is None:
        return None
    response = requests.get(url='https://opentdb.com/api_category.php')
    category_data = response.json()["trivia_categories"]
    cat_dict = {cat['name']: cat['id'] for cat in category_data}
    return cat_dict[category]


def get_question_data(difficulty=None, category=None, questions=QUESTIONS):
    response = requests.get(url=f'https://opentdb.com/api.php?amount={questions}&type=boolean'
                                f'&difficulty={difficulty if not difficulty is None else ""}'
                                f'&category={category if not category is None else ""}')
    code = response.json()['response_code']
    if code == 0:
        return response.json()["results"]
    elif code == 1:
        return get_question_data(difficulty, category, questions-1)
    elif code == 2:
        raise ValueError('Invalid Argument in API request')
    elif code == 3:
        raise ValueError('Invalid Session Token')
    elif code == 4:
        raise ValueError('Empty Session Token')
