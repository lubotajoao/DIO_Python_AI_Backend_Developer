salario = 2000


# def salario_bonus(bonus):
#     global salario
#     salario += bonus
#     return salario
#
#
# print(salario_bonus(500))  # 2500


def salario_bonus_2(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"Lista Aux={lista_aux}")

    salario += bonus
    return salario


lista = [1]
salario_com_bonus = salario_bonus_2(500, lista)
print(salario_com_bonus)
