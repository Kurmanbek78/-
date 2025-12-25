from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Разрешаем доступ с любого браузера
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

correct = 0
wrong = 0

@app.get("/task")
def get_task():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])
    question = f"{a} {op} {b}"
    answer = eval(question)
    return {"question": question, "answer": answer}

@app.post("/check")
def check_answer(user_answer: int, correct_answer: int):
    global correct, wrong
    if user_answer == correct_answer:
        correct += 1
        return {"result": " Правильно!", "correct": correct, "wrong": wrong}
    else:
        wrong += 1
        return {"result": " Неправильно!", "correct": correct, "wrong": wrong}
