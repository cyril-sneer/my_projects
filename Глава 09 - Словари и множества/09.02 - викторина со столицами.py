import random

COUNTRIES = ["France", "Italy", "Norway", "England", "Germany", "Poland", "Spain", "Portugal", "Netherlands"]
CITIES = ["Paris", "Rome", "Oslo", "London", "Berlin", "Warshaw", "Madrid", "Lisbon", "Amsterdam"]
QUIZ = dict(zip(COUNTRIES, CITIES))

def main():
    right = 0
    wrong = 0
    capital = " "
    while capital != "":
        country = random.choice(list(QUIZ.keys()))
        capital = input(f"Input the capital of {country.upper()} (blank string for exit): ").capitalize()
        if capital == "":
            pass
        elif capital == QUIZ[country]:
            print("You are right!")
            right += 1
        else:
            print("You are mistaken!")
            wrong += 1
    else:
        print(f"Total questions: {right+wrong}, right: {right}, wrong: {wrong}")

if __name__ == '__main__':
    main()