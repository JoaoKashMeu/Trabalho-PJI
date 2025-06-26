from models.exercicio import Exercicio
exercicios = []

def criar_exercicio(dados):
    novo = Exercicio(len(exercicios)+1, dados['pergunta'], dados['alternativas'], dados['correta'])
    exercicios.append(novo)
    return novo

def listar_exercicios():
    return exercicios