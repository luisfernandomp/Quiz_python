from datetime import datetime
import json
import uuid
import webbrowser 
import os

from jogador import JogadorModel 

class ArquivoService:
    def lerArquivoJson(self, nomeArquivo):
        with open(nomeArquivo, "r") as json_file:
            dados = json.load(json_file)

        return dados   

    def lerArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, "rt", encoding='cp1252')
        linhas = arquivo.readlines()

        return "".join(linhas)  

    def exibirPontuacao(self, individual):
        if individual :
            filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
            webbrowser.open_new_tab(filename) 
        else:
            filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
            webbrowser.open_new_tab(filename)

    def  nomeArquivo(self):
        data = datetime.now()
        data = data.strftime("%d%m%Y") + "_"
        guid = str(uuid.uuid1())
        return str(str(data) + guid + ".html")

    def criarHtmlPontuacaoIndividual(self, jogador):
        perguntas = jogador.getPerguntas()

        html = self.lerArquivo("./templates/individual.html")

        html = html.replace("#NOME_JOGADOR#", jogador.getNome())     
        html = html.replace("#PONTUACAO#", str(jogador.getPontuacao()))

        porcentagem = round(((jogador.getAcertos() * 100)/10),0) 

        html = html.replace("#PORCENTAGEM#", str(porcentagem) + '%')

        (medalha, classificacao) = jogador.obterMedalha()
        html = html.replace("#IMAGE#", medalha)
        html = html.replace('#CLASSIFICACAO#', classificacao)
        
        nomeArquivo = self.nomeArquivo()
        arquivo = open(nomeArquivo, "a")

        tabela = self.criarTabelaJogador(perguntas)

        arquivo.write(html.replace("#TABELA#", "".join(tabela)))

        filename = 'file:///'+os.getcwd()+'/' + nomeArquivo
        webbrowser.open_new_tab(filename)
        

    def criarHtmlPontuacaoMultiplayer(self, jogadores):
        jogador1 = JogadorModel
        jogador2 = JogadorModel

        if(jogadores[0].getPontuacao() > jogadores[1].getPontuacao()):
            jogador1 = jogadores[0]
            jogador2 = jogadores[1]
        else:
            jogador1 = jogadores[1]
            jogador2 = jogadores[0]

        html = self.lerArquivo("./templates/multiplayer.html")
        if(jogador1.getPontuacao() > jogador2.getPontuacao()):
            html = html.replace("#NOME_JOGADOR_VENCEDOR#", jogador1.getNome())
        else:
            html = html.replace("#NOME_JOGADOR_VENCEDOR#", jogador2.getNome())
            

        html = html.replace("#NOME_JOGADOR_1#", jogador1.getNome())
        
        html = html.replace("#CLASSIFICACAO_JOGADOR_1#", "Ouro")
        html = html.replace("#PONTUACAO_JOGADOR_1#", str(jogador1.getPontuacao()))
        html = html.replace("#IMAGEM_JOGADOR_1#", "./templates/images/5a1cec84cd8428 1.png")
        
        
        html = html.replace("#NOME_JOGADOR_2#", jogador2.getNome())
        
        html = html.replace("#CLASSIFICACAO_JOGADOR_2#", "Prata")
        html = html.replace("#PONTUACAO_JOGADOR_2#", str(jogador2.getPontuacao()))
        html = html.replace("#IMAGEM_JOGADOR_2#", "./templates/images/5a1cec84cd8428 3.png")
        
        
        nomeArquivo = self.nomeArquivo()
        arquivo = open(nomeArquivo, "a")
        arquivo.write(html)

        filename = 'file:///'+os.getcwd()+'/' + nomeArquivo
        webbrowser.open_new_tab(filename)
        
    def criarTabelaJogador(self, perguntas):
        tabela = list() 
        tabela.append("<table class='table table-hover'>")
        tabela.append("<thead>")
        tabela.append("<tr>")
        tabela.append("<th scope='col'>#</th>")
        tabela.append("<th scope='col'>Pergunta</th>")
        tabela.append("<th scope='col'>Sua Resposta</th>")
        tabela.append("<th scope='col'>Gabarito</th>")
        tabela.append("</tr>")
        tabela.append("</thead>")
        tabela.append("<tbody>")
              
        cont = 0
        for pergunta in perguntas:
            cont = cont + 1

            classe = "table-success" if pergunta.getAcertou() else  "table-danger"

            tabela.append(f"<tr class='{classe}' {self.obterExplicacao(pergunta)}>")
            tabela.append(f"<th scope='row'>{cont}</th>")
            tabela.append(f"<td>{pergunta.getPergunta()}</td>")
            tabela.append(f"<td>{pergunta.getRespostaJogador()}</td>")
            tabela.append(f"<td>{pergunta.getGabarito()}</td>")
            tabela.append("</tr>")
        
        tabela.append("</tbody>")
        tabela.append("</table>")

        return tabela
    
    def obterExplicacao(self, pergunta):
        tooltip = list()
        tooltip.append("data-container='body' data-toggle='tooltip' data-placement='top'")

        if(pergunta.getAcertou()):
            tooltip.append("data-original-title='Muito bem.'")
        else:
           tooltip.append(f"data-original-title='{pergunta.getExplicacao()}'")

        return "".join(tooltip)

