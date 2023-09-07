import peewee as pw

# Defina a conexão com o banco de dados SQLite
db = pw.SqliteDatabase('exemplo_orm.db')

# Defina o modelo de dados para a tabela 'Usuario'
class Lesson(pw.Model):
    nome = pw.CharField()
    email = pw.CharField(unique=True)  # Garante que o email seja único
    id = pw.IntegerField()
    name = pw.CharField()

    class Meta:
        database = db

# Inicialize o banco de dados e crie a tabela, se não existir
db.connect()

db.drop_tables('lesson')
print(db.get_tables())

db.create_tables([Lesson], safe=True)

# Função para criar um novo usuário
def criar_usuario(nome, email, name):
    try:
        Lesson.create(nome=nome, email=email, name=name)
        print(f"Usuário {nome} criado com sucesso.")
    except pw.IntegrityError:
        print(f"Já existe um usuário com o email {email}.")

# Função para listar todos os usuários
def listar_usuarios():
    usuarios = Lesson.select()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.name}")

# Função para atualizar informações de um usuário
def atualizar_usuario(usuario_id, novo_nome, novo_email):
    usuario = Lesson.get_or_none(id=usuario_id)
    if usuario:
        usuario.nome = novo_nome
        usuario.email = novo_email
        usuario.save()
        print(f"Informações do usuário {usuario_id} atualizadas com sucesso.")
    else:
        print(f"Usuário com ID {usuario_id} não encontrado.")

# Função para excluir um usuário
def excluir_usuario(usuario_id):
    usuario = Lesson.get_or_none(id=usuario_id)
    if usuario:
        usuario.delete_instance()
        print(f"Usuário {usuario_id} excluído com sucesso.")
    else:
        print(f"Usuário com ID {usuario_id} não encontrado.")

# Exemplo de uso
criar_usuario("João", "joao@example.com", name="Aula 01")
criar_usuario("Maria", "maria@example.com", name="Aula 02")

print("Lista de Usuários:")
listar_usuarios()

atualizar_usuario(1, "João da Silva", "joao.silva@example.com")

print("\nLista de Usuários após a atualização:")
listar_usuarios()

excluir_usuario(2)

print("\nLista de Usuários após a exclusão:")
listar_usuarios()
