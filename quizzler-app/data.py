import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    # "category": 19,
    # "difficulty": "medium",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]

# Sample
# question_data = [
#     {"category": "General Knowledge",
#     "type": "boolean",
#     "difficulty": "easy",
#     "question": "The Great Wall of China is visible from the moon.",
#     "correct_answer": "False",
#     "incorrect_answers": ["True"]
#      },
# ]
