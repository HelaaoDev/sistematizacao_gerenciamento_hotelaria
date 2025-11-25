class Pessoa:
    def __init__(self, id, nome, email):
        self.__id = id
        self.__nome = nome
        self.__email = email

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
