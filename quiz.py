class QuizService:

    def bemVindo(self):
        print("**************************************************************************************")
        print("BEM-VINDO AO QUIZ - PRODUTOS DE LIMPEZA")
        print("**************************************************************************************")

    def obterModoJogo(self):
        continuar = True
        while(continuar) :
            print("Digite o modo de jogo: ")
            print("1 - Individual")
            print("2 - Multiplayer")
            modoDeJogo = input("-> ")

            if (modoDeJogo == "1" or modoDeJogo == "2") :
                return modoDeJogo
            else:
                print("\nOpção inválida\n")

    def obterResposta(self):
        possiveisRespostas = ['A', 'B', 'C', 'D', 'E']
        while True :
            resposta = input("Resposta: ").upper()

            contem = False
            for r in possiveisRespostas:
                if(resposta == r):
                    contem = True

            if contem:
                return resposta
            else:
                print("\nOpção inválida\n")
        


        