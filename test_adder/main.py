
# -*- coding: utf-8 -*-

from time import sleep
import json

INPUT_ARROW = "\n--> "

def save(test: dict):
    path = input("Куда хотите сохранить файл с тестом? ( полный путь, включая имя файла)" + INPUT_ARROW)

    with open(path, 'w') as fp:
        json.dump(test,
                  fp,
                  ensure_ascii=False,
                  indent=4)

def main():

    test = {}
    print("Добро пожаловать в testAdder")
    test["name"] = input("Введите исмя теста" + INPUT_ARROW)
    tasks_count = int(input("Сколько будет заданий?" + INPUT_ARROW))
    sleep(1)
    print("Начнем ввод заданий!")
    sleep(1)
    test["tasks"] = []
    for i in range(tasks_count):
        test["tasks"].append({ "question" : input("Введите описание задания" + INPUT_ARROW), "answers" : []})
        for j in range(4):
            test["tasks"][i]["answers"].append({"answer" : input(f"Введите ответ {j+1}" + INPUT_ARROW), "is_correct": False})
        correct_answer = int(input("Какой из ответов правильный?" + INPUT_ARROW))
        test["tasks"][i]["answers"][correct_answer-1]["is_correct"] = True

    save(test)

if __name__ == "__main__":
    main()
