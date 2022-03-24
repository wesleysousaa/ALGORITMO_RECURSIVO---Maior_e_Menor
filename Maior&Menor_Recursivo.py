def numInt(lista, op):
    if (op == 1):
        if(len(lista) == 1):
            return lista[0]
        else:
          if(lista[0] > numInt(lista[1:], op)):
            return lista[0]
          return numInt(lista[1:], op)
    elif (op == 2):
        if (len(lista) == 1):
            return lista[0]
        else:
          if (lista[0] < numInt(lista[1:], op)):
            return lista[0]
          return numInt(lista[1:], op)
lista = [10, -1, 9, 2, 20, 120]

op = 3
msg = ""

while (op != 0):
    print(f"Lista : {lista}")
    op = int(input("1 - Ver maior número da lista\n2 - Ver menor nomero da lista\n0 - Sair\n"))
    if (op == 1):
        msg = "O maior numero é "
    elif (op == 2):
        msg = "O menor numero é "
    elif (op == 0):
        print ("Fim do programa")
        continue
    else:
        print("Opção inválida")
        continue

    print(msg, numInt(lista, op))
