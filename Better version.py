import random

# List of countries and their capitals
quiz_data = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Brazil": "Brasília",
    "Australia": "Canberra",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "Italy": "Rome",
    "Egypt": "Cairo",
    "Argentina": "Buenos Aires",
    "South Africa": "Pretoria",
}

def ask_question(country, capital, options):
    print(f"\nWhat is the capital of {country}?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Get user input
    answer = input("Enter the correct option number (1/2/3/4): ")
    
    # Check if the input is valid and correct
    try:
        if options[int(answer) - 1] == capital:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is {capital}.")
            return False
    except (ValueError, IndexError):
        print("Invalid input. Moving to the next question.")
        return False

def quiz_game():
    print("Welcome to the World Capitals Quiz!")
    score = 0
    total_questions = 5

    # Get a random subset of questions
    questions = random.sample(list(quiz_data.items()), total_questions)
    
    # Loop through the questions
    for country, capital in questions:
        # Generate options with one correct answer and three wrong ones
        wrong_answers = random.sample(list(quiz_data.values()), 3)
        if capital in wrong_answers:
            wrong_answers.remove(capital)
            wrong_answers.append(random.choice(list(quiz_data.values())))
        
        options = wrong_answers + [capital]
        random.shuffle(options)
        
        # Ask the question and update score if correct
        if ask_question(country, capital, options):
            score += 1
            print(f"Your current score: {score}/{total_questions}")

    # Final score
    print(f"\nQuiz Over! Your final score: {score}/{total_questions}")
    
    # Feedback based on score
    if score == total_questions:
        print("Excellent! You got all answers correct!")
    elif score >= total_questions // 2:
        print("Good job! You did pretty well.")
    else:
        print("Keep practicing! You'll get better.")

if __name__ == "__main__":
    quiz_game()
