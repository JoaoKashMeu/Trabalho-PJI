from models.licao import Licao
licoes = []

def criar_licao(dados):
    if any(l.titulo == dados['titulo'] for l in licoes):
        return None
    nova = Licao(len(licoes)+1, dados['titulo'], dados['imagem'], dados['audio'])
    licoes.append(nova)
    return nova

def listar_licoes():
    return licoes

def atualizar_licao(id, dados):
    for l in licoes:
        if l.id == id:
            l.titulo = dados.get('titulo', l.titulo)
            l.imagem = dados.get('imagem', l.imagem)
            l.audio = dados.get('audio', l.audio)
            return l
    return None

def deletar_licao(id):
    global licoes
    for l in licoes:
        if l.id == id:
            licoes = [x for x in licoes if x.id != id]
            return True
    return False