class QuizService:
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


        