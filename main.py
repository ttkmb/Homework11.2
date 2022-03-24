from flask import Flask , render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)

data = load_candidates_from_json()

@app.route('/')
def main():
    return render_template("index.html", candidates = data)

@app.route("/candidate/<int:uid>")
def profile(uid):
    candidate = get_candidate(uid)
    return render_template("single.html", candidate = candidate)


@app.route("/search/<name>")
def search(name):
    candidates = get_candidates_by_name(name)
    return render_template("search.html", candidates = candidates, candidates_len = len(candidates))


@app.route("/skills/<skill>")
def search_skills(skill):
    candidates = get_candidates_by_skill(skill)
    return render_template("skill.html", candidates = candidates, candidates_len = len(candidates))


app.run(debug=True)