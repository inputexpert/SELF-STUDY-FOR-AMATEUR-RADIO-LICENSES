import json

def get_question_by_id(question_id):
    file_path = 'data/exams/technician_2026_2030.json'
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for q in data['questions']:
                if q['id'] == question_id:
                    return q
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return None

if __name__ == "__main__":
    target_id = "T1A01"
    question = get_question_by_id(target_id)
    if question:
        print(f"Question: {question['question']}")
        print(f"Options: {question['answers']}")
    else:
        print(f"Question {target_id} not found.")
      
