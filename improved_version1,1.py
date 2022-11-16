questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


def new_game():

    questions_num = 1
    quesses = []
    correct_answer = 0
    for key in questions:
        print(key)
        print('________________')
        for el in options[questions_num - 1]:
            print(el)
        print('________________')
        quess = input("Please enter answer (A, B, C, D) :").upper()
        while quess not in  "ABCD" or quess == '':
            quess = input("Please enter answer. Choose one of the options (A, B, C, D)").upper()
        quesses.append(quess)
        correct_answer += check_answer(questions.get(key), quess)
        questions_num += 1
    display_score(correct_answer, len(quesses))


def check_answer(answer, quess):
    if answer == quess:
        print("CORRECT !")
        return 1
    else:
        print("WRONG !")
        return 0


def display_score(correct_ans, quesses):
    total = (correct_ans / quesses) * 100
    print("your total score is :", total, "%")


def play_again():
    while True:
        response = input("Do you wanna play again? Choose one of the options (yes, no) : ").upper()
        if response == "YES" or response == "NO":
            break
    if response == "YES":
        return True
    elif response == 'NO':
        return False


new_game()


def main():
    while play_again():
        new_game()
    create = input("Do you wanna create a question for this quiz? (yes, no) : ").upper()
    count = 0
    options_2 = []
    if create == "YES":
        new_question = input("Enter your question : ").capitalize()
        new_ans = input("Enter true option (EX: B) :  ").upper()
        while new_ans not in "ABCD" or new_ans == '':
            new_ans = input("Enter true option (EX: A, B, C, D) :  ").upper()
        questions.setdefault(new_question, new_ans)
        while count < 4:
            option = input("Enter options with answers (EX: A. Your answer) : ")
            options_2.append(option)
            count += 1
        options.append(options_2)
    elif create == "NO":
        print("Byeee!")

    if create == "YES":
        while True:
            again = input("Do you wanna play again with your questions?(yes, no) :").upper()
            if again == "YES":
                new_game()
            elif again == "NO":
                print("Byee!")
                return False




main()