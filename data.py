import requests

AMOUNT = 10
TYPE = "boolean"
parameters = {
    "amount": AMOUNT,
    "type": TYPE,
}

question_data = []
for i in range(0, 9):
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    question = response.json()["results"][i]["question"]
    answer = response.json()["results"][i]["correct_answer"]
    category = response.json()["results"][i]["category"]
    something = response.json()["results"][i]["type"]
    difficulty = response.json()["results"][i]["difficulty"]

    whole = {
        "category": category,
        "type": something,
        "difficulty": difficulty,
        "question": question,
        "correct_answer": answer,
    }

    question_data.append(whole)
