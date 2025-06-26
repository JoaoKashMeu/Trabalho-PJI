from models.estatistica import Estatistica
estatisticas = []

def gerar_estatistica(dados):
    nova = Estatistica(dados['usuario_id'], dados['acertos'], dados['erros'], dados['tempo'])
    estatisticas.append(nova)
    return nova

def listar_estatisticas():
    return estatisticas