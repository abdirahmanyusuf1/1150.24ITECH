def quiz1(question, correct_answer):
    # In your quiz function, you will print the question
    print(question, end=" ")

    users_answer = input()  # and ask the user for the answer.

    # If the user gets the answer correct, print a success message.
    # Else, print a message with the correct answer.
    # Your function does not need to return anything.

    if users_answer.strip().lower() == correct_answer.strip().lower():
        print('That is correct! ')
    else:
        print(f'The answer to question is incorrect, the correct answer is {correct_answer}.')


def main():
    question1 = 'Which planet is closest to the sun?'
    question2 = 'Who painted the Mona Lisa?'

    quiz1(question1, 'Mercury')  # function calling

    quiz1(question2, 'Leonardo da Vinci')  # function calling


main()