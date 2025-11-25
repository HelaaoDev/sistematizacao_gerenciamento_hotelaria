from pessoa import Pessoa

class Hospede(Pessoa):
            def __init__(self, id, nome, email):
                super().__init__(id, nome, email)
                self.__reservas = []

            def fazer_reserva(self, reserva):
                self.__reservas.append(reserva)

            def cancelar_reserva(self, reserva):
                if reserva in self.__reservas:
                    self.__reservas.remove(reserva)

            def consultar_reservas(self):
                return self.__reservas
