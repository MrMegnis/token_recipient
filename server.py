from tg import bot
import schedule
import requests


def wake_up():
    response = requests.get("https://glitch.com/~crystalline-flint-grease")
    print("waked up!")


bot.start_bot()
schedule.every(5).minute(wake_up)
