import peewee as pw

db = pw.SqliteDatabase('learning_english.db')

class Word(pw.Model):
    path = pw.CharField()
    portuguese = pw.CharField()
    english = pw.CharField()
    tagId = pw.IntegerField()
    wordId = pw.CharField(unique=True)
    
    class Meta:
        database = db

db.connect()
db.create_tables([Word], safe=True)

def create_word(tagId, english, portuguese, path):
    try:
        words = Word.select()
        maxId = len(words)+1
        Word.create(wordId=maxId, tagId=tagId, english=english, portuguese=portuguese, path=path)
        print(f"Word {english} successfully created")
        return True
    except pw.IntegrityError:
        print(f"Word already exists {english}.")
        return False

def list_words(english=""):
    if(len(english)>0):
        words = Word.get_or_none(english=english)
        return words

    print("List of words")
    words = Word.select()
    for word in words:        
        print(f"ID: {word.id}, Word: {word.english}, Translate: {word.portuguese}")
    
    return words

def update_word(wordId, tagId, english, portuguese, path):
    word = Word.get_or_none(id=wordId)
    if word:
        word.tagId = tagId
        word.english = english
        word.portuguese = portuguese
        word.path = path
        word.save()
        print(f"Word {wordId} sucessfull updated.")
        return True
    else:
        print(f"Word id {wordId} not found.")
        return False

# Função para excluir um usuário
def delete_word(wordId):
    word = Word.get_or_none(id=wordId)
    if word:
        word.delete_instance()
        print(f"Word {wordId} sucessfull deleted.")
    else:
        print(f"Word ID {wordId} not found.")

def force_word(english, portuguese, path):
    try:
        word = list_words(english=english)
        if(word==None):
            create_word(tagId=1, english=english, portuguese=portuguese, path=path)
            word = list_words(english=english)
        else:
            update_word(wordId=word.wordId, tagId=1, english=english, portuguese=portuguese, path=path)
        
        return word.wordId
    except pw.IntegrityError:
        return 0