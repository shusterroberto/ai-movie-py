from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('learning_english.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para listar todas as tarefas
@app.route('/lessons', methods=['GET'])
def get_lessons():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lesson')
    lessons = cursor.fetchall()
    conn.close()
    lessons_list = []
    for lesson in lessons:
        leson_dict = {
            'Id': lesson['id'],
            'LessonId': lesson['lessonid'],
            'Name': lesson['name'],
            'Module': lesson['module'],
            'Path': lesson['path'],
            'Generate': bool(lesson['generate'])
        }
        lessons_list.append(leson_dict)
    return jsonify(lessons_list)

@app.route('/lesson', methods=['POST'])
def create_leson():
    data = json.loads(request.data)
    LessonId = data['LessonId']
    Module = data['Module']
    Name = data['Name']
    Path = data['Path']

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO lesson (LessonId, Module, Name, Path) VALUES (?,?,?,?)"
    cursor.execute(sql, (LessonId, Module, Name, Path))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Lesson created successfully'})

# Rota para atualizar uma tarefa existente
@app.route('/lesson/<int:id>', methods=['PUT'])
def update_lesson(id):
    data = json.loads(request.data)
    Generate = data['Generate']
    Path = data['Path']
    Name = data['Name']
    LessonId = data['LessonId']

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE lesson SET generate=?, path=?, name=?, lessonId=? WHERE id=?"
    cursor.execute(sql, (Generate, Path, Name, LessonId, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'LessonId updated successfully'})

# Rota para excluir uma tarefa
@app.route('/lesson/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM lesson WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Lesson deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
