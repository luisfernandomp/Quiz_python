class JogadorModel:

    def __init__(self, nome, pontuacao, acertos, erros, perguntas):
        self.nome = nome
        self.pontuacao = pontuacao
        self.acertos = acertos
        self.erros = erros
        self.perguntas = perguntas

    def setNome(self, nome):
        self.nome = nome

    def setPontuacao(self, pontuacao):
        self.pontuacao = pontuacao

    def setAcertos(self, acertos):
        self.acertos = acertos

    def setErros(self, erros):
        self.erros = erros
    
    def setPerguntas(self, perguntas):
        self.erros = perguntas

    def getNome(self):
        return self.nome

    def getPontuacao(self):
        return self.pontuacao

    def getAcertos(self):
        return self.acertos

    def getErros(self):
        return self.erros
    
    def getPerguntas(self):
        return self.perguntas

    def obterMedalha(self):
        ouro = "./templates/images/5a1cec84cd8428 1.png"
        prata = "./templates/images/5a1cec84cd8428 3.png"
        bronze = "./templates/images/5a1cec84cd8428 2.png"

        if(self.getPontuacao() < 50):
            return (bronze, 'Bronze')
        elif (self.getPontuacao() >= 50 and self.getPontuacao() <= 75):
            return (prata, 'Prata')
        else :
            return (ouro, 'Ouro')

class JogadorService:

    def obterNomeDosJogadores(self, n, perguntas):
        nome = input(f"Nome jogador {n}: ")
        jogador = JogadorModel(nome, 0, 0, 0, perguntas)
        
        return jogador
