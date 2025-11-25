class Reserva:
            def __init__(self, hospede, quarto):
                self.__hospede = hospede
                self.__quarto = quarto

            def __str__(self):
                return f"Reserva para {self.__hospede.get_nome()} no Quarto {self.__quarto.get_numero()}"

            def __repr__(self):
                return self.__str__()


