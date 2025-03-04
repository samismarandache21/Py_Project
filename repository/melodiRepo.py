from domain.melodi import *

class melodiRepo:
    def __init__(self):
        self.__all_melodi = []

    def get_all_melodi(self):
        """

        :return:lista de melodii
        """

        return self.__all_melodi

    def empty(self) -> bool:
        """

        :return:bool
        """
        return len(self.__all_melodi) == 0

    def read_from_file(self):
        """
        citim din fisier
        :return:
        """

        file = open("file_name\\melodi.txt", "r")
        lines = file.readlines()
        for line in lines:

            fields = line.split(".")
            if len(fields) >= 4:

                melodie = Melodie(fields[0], fields[1], fields[2], int(fields[3]), int(fields[4]), int(fields[5]))
                self.__all_melodi.append(melodie)

            else:
                print("Error: Insufficient fields in the input data.")


        file.close()

    def rewrite_to_file(self):
        """
        rescriem in fisier
        :return:
        """
        res = ""

        for i in range(len(self.__all_melodi) - 1):
            res += self.__all_melodi[i].__str__() + "\n"

        if not self.empty():
            res += self.__all_melodi[len(self.__all_melodi) - 1].__str__()

        file = open("file_name\\melodi.txt", "w")
        file.write(res)
        file.close()


    def modifica_melodie(self,titlu:str,artist:str,gen:str,ziua:int,luna:int,anul:int,new_gen:str, new_ziua:int, new_luna:int, new_an: int):
        """

        :param titlu:str
        :param artist: str
        :param gen: str
        :param ziua: int
        :param luna: int
        :param anul: int
        :param new_gen: str
        :param new_ziua: int
        :param new_luna: int
        :param new_an: int
        :return: melodia modificata
        """
        melodie_to_update = Melodie(titlu,artist,gen,ziua,luna,anul)
        melodie_to_update.set_gen(new_gen)
        melodie_to_update.set_ziua(new_ziua)
        melodie_to_update.set_luna(new_luna)
        melodie_to_update.set_anul(new_an)


        self.rewrite_to_file()


