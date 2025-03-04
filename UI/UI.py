from service.melodiService import *

class Console:

    def __init__(self, melodi_service:melodiService):
        self.__service = melodi_service

    def print_menu(self):
        print("1. MOdificati una dintre melodii")
        print("2. Creaza aleator melodii")
        print("3. Exporta melodiile sortate")


    def run_modifica_melodie(self):
        keep_trying = 1
        while keep_trying:
            titlul = input("titlul melodiei careia i se fac modificari: ")
            artist = input("artistul melodiei careia i se fac modificari: ")
            gen = input("gen melodiei: ")
            ziua = input("ziua melodiei: ")
            luna = input("luna melodiei: ")
            anul = input("anul melodiei: ")
            new_gen = input("noul gen: ")
            new_ziua = input("noua zi: ")
            new_luna = input("noua luna: ")
            new_an = input("noul an: ")
            try:
                self.__service.try_modifica(titlul,artist,gen,ziua,luna,anul,new_gen,new_ziua,new_luna,new_an)
                print("\nMelodia a fost modificata cu succes\n")
                keep_trying = 0
            except Exception as e:
                print(e)


    def run_app(self):
        run = 1
        while run:
            self.print_menu()
            option =int(input(">>>"))

            if option == 1:
                self.run_modifica_melodie()
            else:
                break