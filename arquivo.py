import json
import webbrowser 
import os 

class ArquivoService:
    def lerArquivo(self, nomeArquivo):
        with open(nomeArquivo, "r") as json_file:
            dados = json.load(json_file)

        return dados   

    def exibirPontuacao(individual):
        if individual :
            filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
            webbrowser.open_new_tab(filename) 
        else:
            filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
            webbrowser.open_new_tab(filename)

    def criarHtmlPontuacaoIndividual(nomeJogador, pontuacao):
        print("not implementation")

    def criarHtmlPontuacaoMultiplayer(nomeJogador, pontuacao):
        print("not implementation")
