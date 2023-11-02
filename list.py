#(question, correct answer, options)
quiz = [
    ("What is the capital of France?", "c", ["a) London", "b) Berlin", "c) Paris", "d) Rome"]),
    ("What is 2 + 2?", "b", ["a) 3", "b) 4", "c) 5", "d) 6"]),
    ("What is the largest planet in our solar system?", "d", ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"]),
    ("Who wrote 'Romeo and Juliet'?", "c", ["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare", "d) Mark Twain"])
]

# Function to run the quiz
def run_quiz(quiz):
    score = 0

    for question, correct_answer, options in quiz:
        print(question)
        for option in options:
            print(option)
        
        user_answer = input("Enter the letter of your answer (e.g., 'a', 'b', 'c', 'd'): ").strip().lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

    return score

# Main program
if __name__ == "__main__":
    print("Welcome to the Simple Quiz!\n")
    total_questions = len(quiz)
    user_score = run_quiz(quiz)

    print(f"You got {user_score} out of {total_questions} questions correct.")
    percentage = (user_score / total_questions) * 100
    print(f"Your score is {percentage}%.")


import random

# Function to generate random addition or subtraction questions
def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-"])
    
    if operator == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2
    
    question = f"What is {num1} {operator} {num2}?"
    
    return question, answer

# Function to run the math quiz
def run_math_quiz(num_questions):
    score = 0

    for _ in range(num_questions):
        question, correct_answer = generate_question()
        print(question)
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

    return score

# Main program
if __name__ == "__main__":
    print("Welcome to the Math Quiz!\n")
    num_questions = 2 # You can change the number of questions here
    user_score = run_math_quiz(num_questions)

    print(f"You got {user_score} out of {num_questions} questions correct.")
    percentage = (user_score / num_questions) * 100
    print(f"Your score is {percentage}%.")