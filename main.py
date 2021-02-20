import eel
import sqlite3

#Підключення до бази данних
#db = sqlite3.connect('db_task.db')
#cursor = db.cursor()

# Ініціалізація коду
eel.init('web', allowed_extensions=['.js', '.html'])

def returnet_data():
    db = sqlite3.connect('db_task.db')
    cursor = db.cursor()
    cursor.execute("SELECT title, text FROM tasks")
    title = cursor.fetchall()
    eel.public_task(title)
    db.close()

#Функція яка визивається з JS та повертає у html дані з бази.
@eel.expose
def add():
    returnet_data()

@eel.expose
def test(title, text):
    print(title)
    print(text)

eel.start('index.html', size=(1366, 768), jinja_templates="templates")

