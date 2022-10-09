from os import remove
from random import random
import socket
from ipaddress import ip_address

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8080
server.bind((ip_address, port))
server.listen()


client = []
print("server is running.....")
list_of_client = []


questions = [
    'What is the Italian word for "PIE"?  \n a. Mozerella \n b. Pasty \n c. Patty \n d. Pizza',
    'Water boils at 212 Units at which scale? \n a. Celsius \n b. Kelvin \n c. Fahrenheit \n d. Rankine',
    'Which sea creature has three hearts? \n a. Dolphins \n b. Octopus \n c. Walrus \n d. Seal',
    'What is the capital of Australia? \n a. Canberra \n b. Sydney \n c. Melbourne \n d. Perth',
    'How many bones does an adult human have? \n a. 206 \n b. 208 \n c. 210 \n d. 212',
    'How many wonders are there in the world? \n a. 8 \n b. 7 \n c. 10 \n d. 4',
    'Which is the largest country in the world? \n a. Canada \n b. China \n c. Russia \n d. USA',
    'How many states are there in the India? \n a. 28 \n b. 29 \n c. 30 \n d. 31',
    'Which is the largest continent in the world? \n a. Africa \n b. Asia \n c. Europe \n d. Australia',
    'Who was the first Indian female astronaut? \n a. Kalpana Chawla \n b. Sunita Williams \n c. Rakesh Sharma \n d. Kalpana Mohan',
    'Which is the largest planet in the solar system? \n a. Neptune \n b. Saturn \n c. Jupiter \n d. Uranus',
    'which planet is closest to the sun? \n a. Mercury \n b. Pluto \n c. Earth \n d. Venus',
]

answer = [
    'd',
    'c',
    'b',
    'a',
    'a',
    'b',
    'c',
    'a',
    'b',
    'a',
    'c',
    'a',
]


def get_random_questions_answer(conn):
    random_index = random.randint(0, len(questions)-1)
    random_questions = questions[random_index]
    random_answer = answer[random_index]
    conn.send(random_questions.encode('utf-8'))
    return random_index, random_answer, random_questions


def remove_questions(index):
    questions.pop(index)
    answer.pop(index)


def clientthread(conn):
    score = 0
    conn.send('Welcome to this quiz! '.encode('utf-8'))
    conn.send(
        'You wil receive. The answer to that questions will be a, b, c or d. '.encode('utf-8'))
    conn.send('Good Luck! '.encode('utf-8'))
    index, questions, answer = get_random_questions_answer(conn)
    while True:
        conn, addr = server.accept()
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message == answer:
                    score += 1
                    conn.send(
                        'Brave! Your score is {score}\n\n'.encode('utf-8'))
                else:
                    conn.send(
                        'Incorrect answer! Better luck next time!\n\n'.encode('utf-8'))
                    remove_questions(index)
                    index, questions, answer = get_random_questions_answer(
                        conn)
            else:
                remove(conn)
        except:
            continue
