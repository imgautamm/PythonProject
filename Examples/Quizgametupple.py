#Quiz game
questions = ("How many bones are in the human body?",
            "What is the largest mammal?",
            "What is the most abundant gas in the Earth's atmosphere?",
            "What is the atomic number of lead?",
            "What is the third planet from the sun?")

options = (("A. 116", "B. 112", "C. 114", "D. 118"),
          ("A. Whale", "B. Elephant", "C. Lion", "D. Tiger"),
          ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
          ("A. 206", "B. 208", "C. 210", "D. 212"),
          ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("A", "B", "B", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess= input("Enter (A, B, C, D) :").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("---------------------------")
print("          Resutls          ")
print("---------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
for guess in guesses:
    print(guess, end=" ")
print()

score  = int(score / len(questions) * 100)
print(f"Your score is: {score}%")