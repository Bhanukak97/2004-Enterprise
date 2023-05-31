import random

# List of spirit animals
spirit_animals = ["Tiger", "Eagle", "Lion", "Wolf", "Owl", "Fox", "Dolphin", "Butterfly"]

# Prompt the user for their name
name = input("What is your name? ")

# Choose a random spirit animal
spirit_animal = random.choice(spirit_animals)

# Print the name and spirit animal
print("Hello, " + name + "! Your spirit animal is: " + spirit_animal)
