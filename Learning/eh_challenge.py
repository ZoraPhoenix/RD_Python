actor = {"name": "The Rock", "age": 50, "movies": ["Fast & Furious", "Jumanji", "Moana"]}

def get_last_name():
    return actor["name"].split()[1]

def get_age():
    return actor["age"]

print("The actor's last name is %s" % get_last_name())
print("The age of the actor is: %d" % get_age())