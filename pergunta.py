import random

class PerguntaService:

    def converterJsonToPergunta(self, questoes):
        perguntas = []

        for questao in questoes:
            pergunta = PerguntaModel(questao['pergunta'], 
                                    questao['alternativas'],
                                    questao['gabarito'],
                                    questao['nivelDeDificuldade'],
                                    questao['explicacao'])
            perguntas.append(pergunta)

        return perguntas

    def escolherPerguntasAleatorias(self, perguntas):
        perguntasAleatorias = []
        numerosEscolhidos = []

        while len(perguntasAleatorias) < 10:
            num = random.randint(1, 30)
            if(num in numerosEscolhidos ):
                perguntasAleatorias.append(perguntas[num])
            numerosEscolhidos.append(num)

        return perguntasAleatorias

class PerguntaModel:
    def __init__(self):
        pass

    def __init__(self, pergunta, alternativas, gabarito, dificuldade, explicacao):
        self.pergunta = pergunta
        self.alternativas = alternativas
        self.gabarito = gabarito
        self.dificuldade = dificuldade
        self.explicacao = explicacao
        self.respostaJogador = ""
        self.acertou = False

    def setPergunta(self, pergunta):
        self.pergunta = pergunta

    def setAlternativas(self, alternativas):
        self.alternativas = alternativas

    def setGabarito(self, gabarito):
        self.alternativas = gabarito

    def setDificuldade(self, dificuldade):
        self.dificuldade = dificuldade

    def setExplicaco(self, explicaco):
        self.explicacao = explicaco

    def setRespostaJogador(self, respostaJogador):
        self.respostaJogador = respostaJogador
    
    def setAcertou(self, acertou):
        self.acertou = acertou

    def getPergunta(self):
        return self.pergunta

    def getAlternativas(self):
        return self.alternativas

    def getGabarito(self):
        return self.gabarito
    
    def getDificuldade(self):
        return self.dificuldade

    def getExplicaco(self):
        return self.explicacao
    
    def getRespostaJogador(self):
        return self.respostaJogador
    
    def getAcertou(self):
        return self.acertou
    


