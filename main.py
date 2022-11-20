from math import fabs
import arquivo
import pergunta
import jogador
import quiz
import os
import time

clear = lambda: os.system('cls')
arquivoService = arquivo.ArquivoService()
perguntaService = pergunta.PerguntaService()
quizService = quiz.QuizService()
jogadorService = jogador.JogadorService()


quizService.bemVindo()
modo = [1, 2] if quizService.obterModoJogo() == "2" else [1] 
dados = arquivoService.lerArquivoJson("./configurations/perguntas.json")
perguntas = perguntaService.converterJsonToPergunta(dados)

jogadores = []
for n in modo:
    perguntasAleatorias = perguntaService.escolherPerguntasAleatorias(perguntas)
    jogadores.append(jogadorService.obterNomeDosJogadores(n, perguntasAleatorias))


for jogador in jogadores:
    print(f"Jogador {jogador.getNome()}");
    print("Preparando jogo...")
    time.sleep(1)
    
    perguntas = jogador.getPerguntas()
    i = 0
    for pergunta in perguntas:
        clear()

        i += 1
        print(f"{i}) - {pergunta.getPergunta()}")
        for alternativa in pergunta.getAlternativas():
            print(alternativa)
        
        resposta = quizService.obterResposta()
        pergunta.setRespostaJogador(resposta)

        gabarito = pergunta.getGabarito().upper()
        if(resposta == gabarito):
            pergunta.setAcertou(True)
            jogador.setAcertos(jogador.getAcertos() + 1)
            
            print("\nResposta correta\n")
            time.sleep(1)

            nivelDificuldade = pergunta.getDificuldade()

            if(nivelDificuldade == 1):
                jogador.setPontuacao(jogador.getPontuacao() + 3.75)
            elif(nivelDificuldade == 2):
                jogador.setPontuacao(jogador.getPontuacao() + 8.75)
            else:
                jogador.setPontuacao(jogador.getPontuacao() + 25)

        else:
            print("\nResposta errada\n")
            print("-> Explicação")
            print(pergunta.getExplicacao())
            time.sleep(5)
            print("\nPróxima pergunta...\n")
            time.sleep(1)

    print(jogador.getPontuacao())
        

if(len(modo) == 1):
    arquivoService.criarHtmlPontuacaoIndividual(jogadores[0])
else:
    arquivoService.criarHtmlPontuacaoMultiplayer(jogadores)

