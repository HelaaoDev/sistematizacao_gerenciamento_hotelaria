# Link Vídeo - https://youtu.be/1wDEk6-Pd2w
# Link Replit - https://replit.com/@helam133/Helam-Sobrinho-Projeto-03-Sistema-de-Hotelaria?v=1

from hotel import Hotel
from quarto import Quarto
from funcionario import Funcionario
from hospede import Hospede
from reserva import Reserva


def main():
  # Hotel
  hotel = Hotel()

  # Funcionário
  funcionario = Funcionario(1, "Ana", "ana@hotel.com")

  # Quartos
  quarto1 = Quarto(101, "Standard")
  quarto2 = Quarto(102, "Deluxe")
  quarto3 = Quarto(103, "Suite")

  # Quartos do hotel
  funcionario.add_quarto(hotel, quarto1)
  funcionario.add_quarto(hotel, quarto2)
  funcionario.add_quarto(hotel, quarto3)

  # Sistema interativo
  while True:
    print("\n=== SISTEMA DE HOTEL ===")
    print("1. Registrar novo hóspede")
    print("2. Fazer reserva")
    print("3. Consultar reservas de hóspede")
    print("4. Cancelar reserva")
    print("5. Ver quartos disponíveis")
    print("6. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
      registrar_hospede(hotel, funcionario)
    elif opcao == "2":
      fazer_reserva(hotel)
    elif opcao == "3":
      consultar_reservas(hotel)
    elif opcao == "4":
      cancelar_reserva_hospede(hotel, funcionario)
    elif opcao == "5":
      ver_quartos_disponiveis(hotel)
    elif opcao == "6":
      print("Saindo do sistema...")
      break
    else:
      print("Opção inválida!")


def registrar_hospede(hotel, funcionario):
  print("\n=== REGISTRAR NOVO HÓSPEDE ===")
  try:
    id_hospede = int(input("ID do hóspede: "))
    nome = input("Nome: ")
    email = input("Email: ")

    hospede = Hospede(id_hospede, nome, email)
    funcionario.registrar_hospede(hotel, hospede)
    print(f"Hóspede {nome} registrado com sucesso!")

  except ValueError:
    print("ID deve ser um número!")


def fazer_reserva(hotel):
  print("\n=== FAZER RESERVA ===")
  try:
    id_hospede = int(input("ID do hóspede: "))
    hospede = encontrar_hospede_por_id(hotel, id_hospede)

    if not hospede:
      print("Hóspede não encontrado!")
      return

    print(f"Hóspede encontrado: {hospede.get_nome()}")

    # Mostrar quartos disponíveis
    quartos_disponiveis = obter_quartos_disponiveis(hotel)
    if not quartos_disponiveis:
      print("Não há quartos disponíveis!")
      return

    print("\nQuartos disponíveis:")
    for i, quarto in enumerate(quartos_disponiveis):
      print(f"{i+1}. {quarto}")

    escolha = int(input("Escolha um quarto (número): ")) - 1

    if 0 <= escolha < len(quartos_disponiveis):
      quarto_escolhido = quartos_disponiveis[escolha]
      reserva = hotel.realizar_reserva(hospede, quarto_escolhido)
      if reserva:
        print(f"Reserva realizada com sucesso! {reserva}")
    else:
      print("Escolha inválida!")

  except ValueError:
    print("ID deve ser um número!")


def consultar_reservas(hotel):
  print("\n=== CONSULTAR RESERVAS ===")
  try:
    id_hospede = int(input("ID do hóspede: "))
    hospede = encontrar_hospede_por_id(hotel, id_hospede)

    if not hospede:
      print("Hóspede não encontrado!")
      return

    reservas = hospede.consultar_reservas()

    if not reservas:
      print(f"O hóspede {hospede.get_nome()} não possui reservas.")
    else:
      print(f"\nReservas de {hospede.get_nome()}:")
      for i, reserva in enumerate(reservas, 1):
        print(f"{i}. {reserva}")

  except ValueError:
    print("ID deve ser um número!")


def cancelar_reserva_hospede(hotel, funcionario):
  print("\n=== CANCELAR RESERVA ===")
  try:
    id_hospede = int(input("ID do hóspede: "))
    hospede = encontrar_hospede_por_id(hotel, id_hospede)

    if not hospede:
      print("Hóspede não encontrado!")
      return

    reservas = hospede.consultar_reservas()

    if not reservas:
      print(f"O hóspede {hospede.get_nome()} não possui reservas.")
      return

    print(f"\nReservas de {hospede.get_nome()}:")
    for i, reserva in enumerate(reservas, 1):
      print(f"{i}. {reserva}")

    escolha = int(input("Escolha a reserva para cancelar (número): ")) - 1

    if 0 <= escolha < len(reservas):
      reserva_escolhida = reservas[escolha]
      funcionario.cancelar_reserva(hotel, reserva_escolhida)
      hospede.cancelar_reserva(reserva_escolhida)
      print("Reserva cancelada com sucesso!")
    else:
      print("Escolha inválida!")

  except ValueError:
    print("Entrada inválida!")


def ver_quartos_disponiveis(hotel):
  print("\n=== QUARTOS DISPONÍVEIS ===")
  quartos_disponiveis = obter_quartos_disponiveis(hotel)

  if not quartos_disponiveis:
    print("Não há quartos disponíveis!")
  else:
    print("Quartos disponíveis:")
    for quarto in quartos_disponiveis:
      print(f"- {quarto}")


def encontrar_hospede_por_id(hotel, id_hospede):
  for hospede in hotel._Hotel__hospedes:
    if hospede.get_id() == id_hospede:
      return hospede
  return None


def obter_quartos_disponiveis(hotel):
  quartos_disponiveis = []
  for quarto in hotel._Hotel__quartos:
    if quarto.esta_disponivel():
      quartos_disponiveis.append(quarto)
  return quartos_disponiveis


if __name__ == "__main__":
  main()
