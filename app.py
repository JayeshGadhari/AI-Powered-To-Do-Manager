from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__, template_folder="templates")

# Hugging Face pipeline for text generation
generator = pipeline("text2text-generation", model="google/flan-t5-small")

# In-memory task list
tasks = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json() or {}
    user_title = (data.get("idea") or "").strip()

    if not user_title:
        return jsonify({"error": "idea is required"}), 400

    # AI generates description based on title
    prompt = f"Write a detailed task description for this title: {user_title}"
    output = generator(prompt, max_new_tokens=64)[0]["generated_text"].strip()

    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": user_title,
        "description": output,
        "status": "pending"
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json() or {}
    for t in tasks:
        if t["id"] == task_id:
            t.update({k: v for k, v in data.items() if k in ["title", "description", "status"]})
            return jsonify(t)
    return jsonify({"error": "task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"success": True})

# New route: Summarize tasks using AI
@app.route("/tasks/summarize", methods=["GET"])
def summarize_tasks():
    if not tasks:
        return jsonify({"summary": "No tasks to summarize."})
    
    # Prepare a summary prompt
    task_list_text = "\n".join([f"- {t['title']} ({t['status']}): {t['description']}" for t in tasks])
    prompt = f"Summarize the following tasks in a concise way:\n{task_list_text}"

    summary = generator(prompt, max_new_tokens=100)[0]["generated_text"].strip()
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
