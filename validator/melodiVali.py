from domain.melodi import Melodie
class melodiVali:


    def __init__(self):
        pass

    def numerical_data(self, input_data: str):
        if not input_data.isnumeric():
            raise Exception("\nData nu este un numar\n")
        if int(input_data)<1 or int(input_data)>31:
            raise Exception("\nData nu este valabila\n")

    def numerical_luna(self, input_luna: str):
        if not input_luna.isnumeric():
            raise Exception("\nLuna nu este un numar\n")
        if int(input_luna)<1 or int(input_luna)>12:
            raise Exception("\nLuna nu este valabila\n")

    def numerical_an(self, input_an: str):
        if not input_an.isnumeric():
            raise Exception("\nData nu este un numar\n")
        if int(input_an)<1900 or int(input_an)>2024:
            raise Exception("\nData nu este valabila\n")


    def gen_specific(self, input_gen:str):
        if input_gen =="Rock" or input_gen =="Pop" or input_gen =="Jazz":
            pass
        else:
            raise Exception("\nGenul muzical nu este valabil\n")


    def exista_artist(self,input_artist):
        if is isinstance(i)