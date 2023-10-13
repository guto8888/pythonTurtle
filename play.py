from turtle import Turtle

playTurtle = int(input("Para jogar digite um um número\n1 - Definir velocidade \n2 - Movimentar para frente \n3 - Movimentar para trás \n4 - Girar para a direita \n5 - Girar para a esquerda \n6 - Parar \nEscolha: "))

t = Turtle()
t.speed(1)

while playTurtle != 7:
    match playTurtle:
        case 1:
            vel = int(input("Qual a velocidade? "))
            while vel <= 0 or vel > 10:
                print("Velocidade incorreta")
                vel = int(input("Qual a velocidade? "))
            t.speed(vel)
            playTurtle =  int(input("Para jogar digite um um número\n1 - Definir velocidade \n2 - Movimentar para frente \n3 - Movimentar para trás \n4 - Girar para a direita \n5 - Girar para a esquerda \n6 - Parar \nEscolha: "))
        case 2:
            forward = int(input("Defina quanto quer ir para frente: "))
            t.forward(forward)
            playTurtle = int(input("Para jogar digite um um número\n1 - Definir velocidade \n2 - Movimentar para frente \n3 - Movimentar para trás \n4 - Girar para a direita \n5 - Girar para a esquerda \n6 - Parar \nEscolha: "))
        case 3:
            backward = int(input("Quanto quer ir para trás: "))
            t.backward(backward)
            playTurtle = int(input("Para jogar digite um um número\n1 - Definir velocidade \n2 - Movimentar para frente \n3 - Movimentar para trás \n4 - Girar para a direita \n5 - Girar para a esquerda \n6 - Parar \nEscolha: "))
        case 4:
            t.right(90)
            forward = int(input("Defina quanto quer andar: "))
            t.forward(forward)
            playTurtle = int(input("Para jogar digite um um número\n1 - Definir velocidade \n2 - Movimentar para frente \n3 - Movimentar para trás \n4 - Girar para a direita \n5 - Girar para a esquerda \n6 - Parar \nEscolha: "))
            
        case 5:
            t.left(90)
            forward = int(input("Defina quanto quer andar: "))
            t.forward(forward)
            playTurtle = int(input("Para jogar digite um um número\n1 - Definir velocidade \n2 - Movimentar para frente \n3 - Movimentar para trás \n4 - Girar para a direita \n5 - Girar para a esquerda \n6 - Parar \nEscolha: "))
        case 6:
            break
        case _:
            print("Número incorreto")
            playTurtle = int(input("Para jogar digite um um número\n1 - Definir velocidade \n2 - Movimentar para frente \n3 - Movimentar para trás \n4 - Girar para a direita \n5 - Girar para a esquerda \n6 - Parar \nEscolha: "))
        