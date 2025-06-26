from models.progresso import Progresso
progresso_lista = []

def registrar_progresso(dados):
    novo = Progresso(len(progresso_lista)+1, dados['usuario_id'], dados['licao_id'], dados['completou'])
    progresso_lista.append(novo)
    return novo

def listar_progresso():
    return progresso_lista

def atualizar_progresso(id, dados):
    for p in progresso_lista:
        if p.id == id:
            p.usuario_id = dados.get('usuario_id', p.usuario_id)
            p.licao_id = dados.get('licao_id', p.licao_id)
            p.completou = dados.get('completou', p.completou)
            return p
    return None

def deletar_progresso(id):
    global progresso_lista
    for p in progresso_lista:
        if p.id == id:
            progresso_lista = [x for x in progresso_lista if x.id != id]
            return True
    return False