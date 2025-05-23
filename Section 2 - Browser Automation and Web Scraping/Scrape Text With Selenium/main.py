from driver_config import get_driver
from turtle import Turtle, Screen

FONT = ("Ink Free", 24, "normal")

def get_text() -> str:
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    text = element.text
    parts = text.split(",", 1)
    if len(parts) == 2:
         text = f"{parts[0]}, \n {parts[1]}"
    # driver.quit()
    return text

def show_on_screen():
    text = get_text()
    screen = Screen()
    screen.setup(width=1000, height=800)
    screen.bgcolor("black")

    text_object = Turtle()
    text_object.color("white")
    text_object.hideturtle()
    text_object.write(text, False, "center", FONT)
    screen.exitonclick()

show_on_screen()

# print(get_text())

# py main.py 