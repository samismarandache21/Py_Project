
class Melodie:

    def __init__(self, titlu: str, artsit: str, gen: str, ziua: int, luna: int, anul: int):
        """

        :param titlu: str
        :param artsit: str
        :param gen: str
        :param ziua: int
        :param luna: int
        :param anul: int
        """
        self.__titlu = titlu
        self.__artist = artsit
        self.__gen = gen
        self.__ziua = ziua
        self.__luna = luna
        self.__anul = anul

    def get_titlu(self):
        """

        :return:titlul
        """
        return self.__titlu

    def get_artist(self):
        """

        :return:artsitul
        """
        return self.__artist

    def get_gen(self):
        """

        :return:genul
        """
        return  self.__gen

    def get_ziua(self):
        """

        :return:ziua
        """
        return self.__ziua

    def get_luna(self):
        """

        :return:luna
        """
        return self.__luna

    def get_anul(self):
        """

        :return:anul
        """
        return self.__anul

    def set_titlu(self, new_titlu:str):
        """

        :param new_titlu:str
        :return:
        """
        self.__titlu = new_titlu

    def set_artist(self, new_artist: str):
        """

        :param new_artist: str
        :return:
        """
        self.__artist = new_artist

    def set_gen(self, new_gen: str):
        """

        :param new_gen:str
        :return:
        """
        self.__gen = new_gen

    def set_ziua(self, new_ziua: int):
        """

        :param new_ziua:int
        :return:
        """
        self.__ziua = new_ziua

    def set_luna(self, new_luna:int):
        """

        :param new_luna:int
        :return:
        """
        self.__luna = new_luna

    def set_anul(self, new_an: int):
        """

        :param new_an: int
        :return:
        """
        self.__anul = new_an

    def __str__(self):
        return self.__titlu + "." + self.__artist + "." + self.__gen + "." + str(self.__ziua) + "." + str(self.__luna) + "." + str(self.__anul)
