from reserva import Reserva

class Hotel:
    def __init__(self):
        self.__quartos = []
        self.__hospedes = []
        self.__reservas = []

    def add_quarto(self, quarto):
        self.__quartos.append(quarto)

    def remover_quarto(self, quarto):
        if quarto in self.__quartos:
            self.__quartos.remove(quarto)

    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)

    def cancelar_reserva(self, reserva):
                if reserva in self.__reservas:
                    reserva._Reserva__quarto.liberar()
                    self.__reservas.remove(reserva)

    def realizar_reserva(self, hospede, quarto):
                if quarto.esta_disponivel():
                    reserva = Reserva(hospede, quarto)
                    self.__reservas.append(reserva)
                    hospede.fazer_reserva(reserva)
                    quarto.reservar()
                    return reserva
                else:
                    print("Quarto indisponível")
                    return None