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

        perguntasFaceis = []
        perguntasMedias = []
        perguntasDificeis = []

        for pergunta in perguntas:
            nivelDificuldade = pergunta.getDificuldade()

            if(nivelDificuldade == 1):
                perguntasFaceis.append(pergunta)
            elif(nivelDificuldade == 2):
                perguntasMedias.append(pergunta)
            else:
                perguntasDificeis.append(pergunta)

        while len(perguntasAleatorias) < 4:
            num = random.randint(0, len(perguntasFaceis) - 1)
            if(num not in numerosEscolhidos ):
                perguntasAleatorias.append(perguntasFaceis[num])
            numerosEscolhidos.append(num)

        numerosEscolhidos = []
        while len(perguntasAleatorias) < 8:
            num = random.randint(0, len(perguntasMedias) - 1)
            if(num not in numerosEscolhidos ):
                perguntasAleatorias.append(perguntasMedias[num])
            numerosEscolhidos.append(num)
        
        numerosEscolhidos = []
        while len(perguntasAleatorias) < 10:
            num = random.randint(0, len(perguntasDificeis) - 1)
            if(num not in numerosEscolhidos ):
                perguntasAleatorias.append(perguntasDificeis[num])
            numerosEscolhidos.append(num)

        return perguntasAleatorias

class PerguntaModel:

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

    def setExplicacao(self, explicaco):
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

    def getExplicacao(self):
        return self.explicacao
    
    def getRespostaJogador(self):
        return self.respostaJogador
    
    def getAcertou(self):
        return self.acertou
    


