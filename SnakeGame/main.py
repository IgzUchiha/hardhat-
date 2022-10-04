from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from web3 import Web3
from tkinter import *
import webbrowser


def click():
    print('Works')


web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/d7ba549ef43b443d8ddb7f1fb9d10d9f'))
# print(web3.isConnected())
balance = web3.eth.get_balance('0xC5A66758501De57Cd39EC8087dc4b4BEB8Cbb117')
print(balance)
print(web3.eth.blockNumber)
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("red")
screen.title("My SLATT Game")
screen.tracer(0)
button = Button(text='Connect Meta Mask')
button.config(command=click)
button.pack()
# webbrowser.open_new("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
webbrowser.open_new("https://metamask.io")




snake = Snake()
food = Food()
scoreboard = Scoreboard()
# metaMask = MetaMask()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision With Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # Detect collision with tail game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

screen.exitonclick()
