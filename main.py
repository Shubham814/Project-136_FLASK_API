import pandas as pd

data = pd.read_csv("Filtered_Stars.csv")

star_name = data["Star_name"]
distance = data["Distance"]
mass = data["Mass"]
radius = data["Radius"]
gravity = data["Gravity"]

star_data = {}

for i in range(0,len(star_name)):
    data_to_append = {
        "name": star_name[i],
        "distance": distance[i],
        "mass": mass[i],
        "radius": radius[i],
        "gravity": gravity[i]
    }
    star_data[i] = data_to_append

print(f"\nThe length of our dictionary is {len(star_data)}\n")
print(star_data)
