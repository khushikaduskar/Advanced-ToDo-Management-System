from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Put your MySQL password here
    database="todo_db"
)

cursor = db.cursor()

@app.route('/')
def home():

    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    tasks = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='Pending'")
    pending = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='Completed'")
    completed = cursor.fetchone()[0]

    return render_template(
        'index.html',
        tasks=tasks,
        total=total,
        pending=pending,
        completed=completed
    )

@app.route('/add', methods=['POST'])
def add():

    task = request.form['task']
    priority = request.form['priority']
    due_date = request.form['due_date']

    sql = """
    INSERT INTO tasks(title, priority, due_date)
    VALUES(%s,%s,%s)
    """

    cursor.execute(sql, (task, priority, due_date))
    db.commit()

    return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):

    cursor.execute(
        "UPDATE tasks SET status='Completed' WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):

    title = request.form['title']

    cursor.execute(
        "UPDATE tasks SET title=%s WHERE id=%s",
        (title,id)
    )

    db.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
