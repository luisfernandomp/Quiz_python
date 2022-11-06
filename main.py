import arquivo
import pergunta
import jogador
import quiz
import os

arquivoService = arquivo.ArquivoService()
perguntaService = pergunta.PerguntaService()
quizService = quiz.QuizService()
jogadorService = jogador.JogadorService()

clear = lambda: os.system('cls')
modo = [1, 2] if quizService.obterModoJogo() == "2" else [1] 

dados = arquivoService.lerArquivo("./configurations/perguntas.json")
perguntas = perguntaService.converterJsonToPergunta(dados)

jogadores = []
for n in modo:
    perguntasAleatorias = perguntaService.escolherPerguntasAleatorias(perguntas)
    jogadores.append(jogadorService.obterNomeDosJogadores(n, perguntasAleatorias))


for jogador in jogadores:
    print(f"Jogador {jogador.getNome()}");

    for pergunta in jogador.getPerguntas():
        #clear()
        print(pergunta.getPergunta())
        for alternativa in pergunta.getAlternativas():
            print(alternativa)
        
        resposta = input("Resposta: ");    
        if(resposta == pergunta.getGabarito()):
            jogador.setPontuacao(jogador.getPontuacao() + 1)

    print(jogador.getPontuacao())

            