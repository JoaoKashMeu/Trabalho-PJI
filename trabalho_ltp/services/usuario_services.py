from models.usuario import Usuario
usuarios = []

def criar_usuario(dados):
    if any(u.email == dados['email'] for u in usuarios):
        return None
    novo = Usuario(len(usuarios)+1, dados['nome'], dados['email'])
    usuarios.append(novo)
    return novo

def listar_usuarios():
    return usuarios

def atualizar_usuario(id, dados):
    for u in usuarios:
        if u.id == id:
            u.nome = dados.get('nome', u.nome)
            u.email = dados.get('email', u.email)
            return u
    return None

def deletar_usuario(id):
    global usuarios
    for u in usuarios:
        if u.id == id:
            usuarios = [x for x in usuarios if x.id != id]
            return True
    return False