import json
import tkinter as tk
from difflib import get_close_matches as find_close_matches

def load_database():
    # Function to load the database from a JSON file.
    with open('C:\\Users\\efe\\Desktop\\self learning chatbot\\database.json', 'r') as file:
        return json.load(file)

def write_to_database(data):
    # Function to write data to the database JSON file.
    with open('C:\\Users\\efe\\Desktop\\self learning chatbot\\database.json', 'w') as file:
        json.dump(data, file, indent=2)

def find_closest_match(question, questions):
    # Function to find the closest match to a given question in a list of questions.
    matched = find_close_matches(question, questions, n=1, cutoff=0.6)
    return matched[0] if matched else None

def find_answer(question, database):
    # Function to find the answer to a given question in the database.
    for question_answers in database["questions"]:
        if question_answers["question"] == question:
            return question_answers["answer"]
    return None

def chat_bot():
    # Main function to operate the chatbot.
    database = load_database()

    print("not teach mode --->0 . teach mode--->1")
    new_response = input("Please select mode:")
    
    # Operate in non-teach mode
    if new_response == '0':
        while True:
            question = input("You: ")
            if question == 'exit':
                break
            # Find the closest matching question in the database
            matched_result = find_closest_match(question, [question_answers["question"] for question_answers in database["questions"]])
            if matched_result:
                # If a match is found, retrieve the answer
                response = find_answer(matched_result, database)
                print(f"Bot: {response}")
            else:
                # If no match is found, inform the user
                print("I don't know the answer. You can ask me other questions or exit ")
    # Operate in teach mode
    elif new_response == '1':
        while True:
            question = input("You: ")
            if question == 'exit':
                break
            # Find the closest matching question in the database
            matched_result = find_closest_match(question, [question_answers["question"] for question_answers in database["questions"]])
            if matched_result:
                # If a match is found, retrieve the answer
                response = find_answer(matched_result, database)
                print(f"Bot: {response}")
            else:
                # If no match is found, ask user for a new answer
                print("Bot: I don't know how to respond to that. Could you teach me?")
                new_answer = input("You can write to teach me or say 'pass'. ")

                if new_answer != 'pass':
                    # Add the new question-answer pair to the database
                    database["questions"].append({
                        "question": question,
                        "answer": new_answer
                    })
                    write_to_database(database)
                    print("Bot: Thanks, I've learned something new thanks to you.")
    else:
        # If an undefined variable is selected, inform the user
        print("Undefined variable was selected. Chatbot is shutting down.")
      
if __name__ == '__main__':
    chat_bot()
