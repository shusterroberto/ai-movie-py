import peewee as pw

db = pw.SqliteDatabase('learning_english.db')

class Line(pw.Model):
    tag = pw.CharField()
    wordId = pw.IntegerField()
    lessonId = pw.IntegerField()
    lineId = pw.AutoField(unique=True)
    
    class Meta:
        database = db

db.connect()
db.create_tables([Line], safe=True)

def create_line(lineId, lessonId, wordId, tag):
    try:
        Line.create(lessonId=lessonId, wordId=wordId, tag=tag)
        print(f"Line successfully created")
    except pw.IntegrityError:
        print(f"Line already exists {lineId}.")

def list_lines(lineId=0):
    if(lineId>0):
        lines = Line.get_or_none(lineId=lineId)
        print(lines)
        return lines
    
    print("List of Lines")
    lines = Line.select()
    print(lines)
    return lines

def update_line(lineId, lessonId, wordId, tag):
    lines = Line.get_or_none(id=lineId)
    if lines:
        lines.lessonId = lessonId
        lines.wordId = wordId
        lines.tag = tag
        lines.save()
        print(f"Line {lineId} sucessfull updated.")
    else:
        print(f"Line id {lineId} not found.")

# Função para excluir um usuário
def delete_line(lineId):
    line = Line.get_or_none(id=lineId)
    if line:
        line.delete_instance()
        print(f"Line {lineId} sucessfull deleted.")
    else:
        print(f"Line ID {lineId} not found.")