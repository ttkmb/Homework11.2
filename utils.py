import json

data = []
def load_candidates_from_json():
    global data
    with open ("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    for candidate in data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not found': 'Не найдено'}

def get_candidates_by_name(candidate_name):
    return [candidate for candidate in data if candidate_name.lower() in candidate['name'].lower()]

def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name in skills:
            candidates.append(candidate)
    return candidates
