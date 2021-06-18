import mouse
from time import sleep
import keyboard as key

print("Автокликер для ЛКМ")
start_key = input("Клавиша запуска: ")
stop_key = input("Клавиша остановки: ")

while True:
    if key.is_pressed(start_key):
        while True:
            sleep(0.01)
            mouse.double_click('left')
            if key.is_pressed(stop_key):
                break