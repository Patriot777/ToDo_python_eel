import eel
import sqlite3

#Підключення до бази данних
#db = sqlite3.connect('db_task.db')
#cursor = db.cursor()

# Ініціалізація коду
eel.init('web', allowed_extensions=['.js', '.html'])



print("hello GIT")



def returnet_data():
    db = sqlite3.connect('db_task.db')
    cursor = db.cursor()
    cursor.execute("SELECT title, text FROM tasks")
    title = cursor.fetchall()
    eel.public_task(title)

@eel.expose
def add():
    
    #cursor.execute(f"""INSERT INTO tasks (text) VALUES ('{ff}')""")
    #db.commit()
    returnet_data()

eel.start('index.html', size=(850, 500), jinja_templates="templates")

