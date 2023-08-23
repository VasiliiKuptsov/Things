import json
import os



class Сompound:
    def __init__(self, path_file):
        self.__data_file = path_file
        self.__compounding()

    @property

    def data_file(self):
        return self.__data_file

    @data_file.setter

    def data_file(self, value):
        self.__data_file = value
        self.__compounding()


    def __compounding(self):
        try:
            if not os.path.exists(self.__data_file):
                with open(self.__data_file, 'w') as file:
                    file.write(json.dumps([]))
        expect FileNotFoundError:
            raise PathNotFoundError

    def insert(self,data:list[dict]):
        file_data = self.load_data
        new_list = []
        ids = [v["id"]for v in file_data]
        for vacancy in data:
            p = vacancy["id"]
            if p not in ids:
                new_list.append(vacancy)
        with open(self.__data_file, 'w') as file:
            json.dump(file_data + new_list, file, indent=4, ensure_ascii=False)


    def select(self, query:dict):
        with open(self.__data_file, 'r') as file:
            file_data = json.load(file)


    def load_data(self):
        try:
            with open(self, __data_file, 'r') as file:
                file_data = json.load(file)
            expect json.load(file)

