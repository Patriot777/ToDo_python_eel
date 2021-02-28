import eel
import sqlite3

# Ініціалізація коду.
eel.init('web', allowed_extensions=['.js', '.html'])


#Функція яка вибирає записи з бази та віддає в js скрипт.
def returnet_data():
    db = sqlite3.connect('db_task.db')
    cursor = db.cursor()
    cursor.execute("SELECT id, title, text FROM tasks ORDER BY id DESC")
    title = cursor.fetchall()
    eel.public_task(title)
    db.close()


#Функція яка визивається з JS та повертає у html дані з бази.
@eel.expose
def add():
    returnet_data()


#Функція запису в базу данних.
@eel.expose
def add_task(title, text):
    title = str(title)
    text = str(text)
    db = sqlite3.connect('db_task.db')
    cursor = db.cursor()

    sql = """INSERT INTO tasks (title, text) VALUES ('{}', '{}')"""
    sss = sql.format(title, text)
    
    cursor.execute(sss)
    db.commit()
    db.close()


#Функція видалення з бази
@eel.expose 
def del_task(id):
    db = sqlite3.connect('db_task.db')
    cursor = db.cursor()
    delete_id = id
    sql_del = """DELETE from tasks where id = {}"""
    db_commit = sql_del.format(delete_id)
    cursor.execute(db_commit)
    db.commit()
    db.close()


eel.start('index.html', size=(1366, 768), jinja_templates="templates")

