import random
from string import ascii_lowercase

#dict(zip(string.ascii_lowercase,[ "1781", "1771", "1871", "1881"],))

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
'''random sample - randomize the order of your questions and the order of the answer alternatives'''

questions = random.sample(list(QUESTIONS.items()),k=num_questions)

num_correct = 0 # counter
for num, (question, alternatives) in enumerate(questions, start=1): #for key,value in dictionary with enumerate
    print(f" \nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0] # the correct answer is assigned the first value in the list

    labeled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))) # sort assorted list
    for label, alternatives in labeled_alternatives.items():
        print(f"   {label}) {alternatives}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives: #walrus operator checks if valid option
        print(f"Please answer one of the {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct +=1
        print("⭐ Correct! ⭐ ")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")

