from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        education = request.form["education"]
        skills = request.form["skills"]
        career = request.form["career"]

        user_skills = [skill.strip().lower() for skill in skills.split(",")]

        career_skills = {
            "data analyst": ["python", "sql", "excel", "power bi", "statistics"],
            "data scientist": ["python", "sql", "machine learning", "statistics", "pandas"],
            "web developer": ["html", "css", "javascript", "react", "git"],
            "software developer": ["python", "java", "sql", "git", "data structures"]
        }

        required_skills = career_skills.get(
            career.lower(),
            ["python", "sql", "communication", "problem solving"]
        )

        missing_skills = [
            skill for skill in required_skills
            if skill not in user_skills
        ]

        matched_skills = [
            skill for skill in required_skills
            if skill in user_skills
        ]

        readiness_score = int(
            (len(matched_skills) / len(required_skills)) * 100
        )

        result = {
            "name": name,
            "education": education,
            "skills": skills,
            "career": career,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "readiness_score": readiness_score
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=False)