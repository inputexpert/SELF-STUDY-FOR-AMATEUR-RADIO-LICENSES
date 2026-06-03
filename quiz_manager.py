import json
import random

def run_quiz():
    file_path = 'data/exams/technician_2026_2030.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    questions = data['questions']
    random.shuffle(questions)
    
    score = 0
    for q in questions:
        print(f"\nQuestion: {q['question']}")
        for key, value in q['answers'].items():
            print(f"{key}: {value}")
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        
        if user_answer == q['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['correct']}.")
            print(f"Explanation: {q.get('explanation', 'No explanation provided.')}")
            
    print(f"\nQuiz complete! Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
  
