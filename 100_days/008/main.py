def greet(one, two, three):
    print(f"{one}")
    print(f"{two}")
    print(f"{three}")
    
greet("Hi","my name is","John")


def life_in_weeks(x):
    y = (90-x)*52
    print(f"You have {y} weeks left.")
    
life_in_weeks(39)

def calculate_love_score(name1, name2):
    true_word = "true"
    love_word = "love"
    t = 0
    l = 0
    for i in name1.lower():
        if i in true_word:
            t += 1
    for i in name2.lower():
        if i in true_word:
            t += 1
    for i in name1.lower():
        if i in love_word:
            l += 1
    for i in name2.lower():
        if i in love_word:
            l += 1
    print(f"Your love score is: {t}{l}")

calculate_love_score("Angela Yu", "Jack Bauer")