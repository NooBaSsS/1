import random

garden = ["покрышка", "бутылка", "окурок", "железяка", "череп коровы"]
garden.clear()

order = (
    ("ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис"),
    ("роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза"),
    ("пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион")
)

for package in order:
    for seed in package:
        garden.append(seed)

weeds = ("борщевик", "крапива", "лопух")

for weed in weeds:
    for i in range(random.randint(5, 10)):
        garden.append(weed)

random.shuffle(garden)
print("сад до прополки:", garden)
print(id(garden))

print()
print()
print(set(garden))


while len(set(garden)) != 3: 
    for weed in garden:
        if weed in weeds:
            garden.remove(weed)


print()
print()
print(set(garden))
print()
print()

print("сад после прополки:", garden)
print(id(garden))
