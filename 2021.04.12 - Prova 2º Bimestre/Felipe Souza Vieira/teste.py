def emiteSenhaComum():
    senhaComum.append(1)
    senhaComum.append(2)
    senhaComum.append(3)
    # senhaComum.append(str(input('Insira seu nome completo: ')))
    print("Você é o {}º da fila.".format((len(senhaComum))))
    # for i in senhaComum:
        # print(senhaComum(i))
    print(senhaComum[2])

senhaComum = []
emiteSenhaComum()
