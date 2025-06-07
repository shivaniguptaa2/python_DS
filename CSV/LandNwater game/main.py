import turtle
import pandas as pd
from PIL import Image

screen = turtle.Screen()
screen.title('Continents and Ocean Game')
screen.setup(width=725, height=491)

img = Image.open("CSV/LandNwater game/world_map.gif")
img = img.resize((725, 491))
img.save("CSV/LandNwater game/map_resized.gif")

screen.bgpic("CSV/LandNwater game/map_resized.gif")

cords = pd.read_csv("CSV/LandNwater game/cordinates.csv", skipinitialspace=True)
cords.columns = cords.columns.str.strip()

place = cords["places"]
place = place.to_list()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")

guessed = []

for num in range(0, 12):
    title_text = f"{len(guessed)}/12 Guessed Correct"
    response = screen.textinput(
        title=title_text,
        prompt="What is the name of another land or water?"
    )
    if response is None:
        break
    response = response.strip().upper()
    if response in [p.upper() for p in place] and response not in [g.upper() for g in guessed]:
        guessed.append(response)
        row = cords[cords["places"].str.upper() == response].iloc[0]
        writer.goto(row["x"], row["y"])
        writer.write(row["places"], align="center", font=("Arial", 10, "bold"))
turtle.mainloop()