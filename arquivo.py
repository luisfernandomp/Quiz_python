from datetime import datetime
import json
import uuid
import webbrowser 
import os 

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

    def criarHtmlPontuacaoIndividual(self, nomeJogador, pontuacao, perguntas):
        html = self.lerArquivo("./templates/individual.html")

        html = html.replace("#NOME_JOGADOR#", nomeJogador)     
        html = html.replace("#PORCENTAGEM#", "20%")
        html = html.replace("#PONTUACAO#", str(pontuacao))
        
    
        nomeArquivo = self.nomeArquivo()
        arquivo = open(nomeArquivo, "a")

        tabela = self.criarTabelaJogador(perguntas)

        arquivo.write(html.replace("#TABELA#", "".join(tabela)))

        filename = 'file:///'+os.getcwd()+'/' + nomeArquivo
        webbrowser.open_new_tab(filename)


    def criarHtmlPontuacaoMultiplayer(nomeJogador, pontuacao):
        pass

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

