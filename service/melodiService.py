from repository.melodiRepo import *
from validator.melodiVali import *

class melodiService:

    def __init__(self, melodi_repo:melodiRepo, melodi_vali:melodiVali):
        self.__repo = melodi_repo
        self.__vali = melodi_vali

    def try_modifica(self,titlu:str,artist:str,gen:str,ziua:str,luna:str,anul:str,new_gen:str,new_ziua:str,new_luna:str,new_an:str):
        self.__repo.read_from_file()
        self.__vali.numerical_data(new_ziua)
        self.__vali.numerical_luna(new_luna)
        self.__vali.numerical_an(new_an)
        self.__repo.modifica_melodie(titlu, artist, gen, int(ziua), int(luna), int(anul), new_gen, int(new_ziua),
                                     int(new_luna), int(new_an))
