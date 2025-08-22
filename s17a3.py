num_pessoas = int(input("Qual o número de pessoas: "))
tipo_reuniao = input("Tipo de reunião ('normal' ou 'executiva'): ").lower()

if tipo_reuniao == "executiva" or num_pessoas > 15:
    print("Sala grande.")
elif num_pessoas >= 1 and num_pessoas <= 5:
    print("Sala pequena.")
elif num_pessoas > 5 and num_pessoas <= 15:
    print("Sala média.")
else:
    print("Reunião cancelada.")










