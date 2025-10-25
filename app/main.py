from flask import Flask, request, jsonify, render_template
from db import get_db, init_db
from models import create_task, get_all_tasks, delete_task

app = Flask(__name__)

# --------------------------
# واجهة المستخدم (الويب)
# --------------------------
@app.route('/')
def home():
    return render_template('index.html')

# --------------------------
# REST API
# --------------------------
@app.route('/api/tasks', methods=['GET'])
def list_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    title = data.get('title')
    if not title:
        return jsonify({"error": "Title is required"}), 400
    task_id = create_task(title)
    return jsonify({"message": "Task created", "id": task_id}), 201

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    deleted = delete_task(task_id)
    if deleted:
        return jsonify({"message": "Task deleted"})
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    # Initialize DB before starting the server
    init_db()
    app.run(host='0.0.0.0', port=5000)

