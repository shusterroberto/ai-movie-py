import peewee as pw

db = pw.SqliteDatabase('learning_english.db')

class Lesson(pw.Model):
    path = pw.CharField()
    name = pw.CharField()    
    module = pw.CharField()
    genarate = pw.BooleanField()
    lessonId = pw.CharField(unique=True)
    
    class Meta:
        database = db

db.connect()
db.create_tables([Lesson], safe=True)

def create_lesson(module, lessonId, name, path):
    try:
        Lesson.create(module=module, lessonId=lessonId, name=name, path=path)
        print(f"Lesson {name} successfully created")
    except pw.IntegrityError:
        print(f"Lesson already exists {name}.")

def list_lessons(name=""):
    if(len(name)>0):
        lessons = Lesson.get_or_none(name=name)
        return lessons
    
    print("List of lessons")
    lessons = Lesson.select()
    return lessons

def update_lesson(lessonId, name, path):
    lesson = Lesson.get_or_none(id=lessonId)
    if lesson:
        lesson.name = name
        lesson.lessonId = lessonId
        lesson.path = path
        lesson.save()
        print(f"Lesson {lessonId} sucessfull updated.")
    else:
        print(f"Lesson id {lessonId} not found.")

# Função para excluir um usuário
def delete_lesson(lessonid):
    lesson = Lesson.get_or_none(id=lessonid)
    if lesson:
        lesson.delete_instance()
        print(f"Lesson {lessonid} sucessfull deleted.")
    else:
        print(f"Lesson ID {lessonid} not found.")