import random, time

def iniciar():
    vida_jugador = 5
    numero_aleatorio = random.randint(1, 99)
    segundo_digito = int(str(numero_aleatorio)[1]) if numero_aleatorio > 9 else None  #devuelve el segundo digito
    primer_digito = int(str(numero_aleatorio)[0]) if numero_aleatorio > 9 else None
    pistas = [
      "El número es menor que 50" if numero_aleatorio < 50 else "El número es mayor o igual a 10",  # expresion condicional u operador ternario
      "El número es par" if numero_aleatorio % 2 == 0 else "El número es impar",
      "El segundo digito es menor que 5" if segundo_digito < 5 else "El segundo digito es mayor o igual a 5",
      "EL primer digito es menor que 5" if primer_digito < 5 else "El primer digito es mayor o igual a 5"
    ]
    def mostrar_pista(indice):
        print("Pista:", pistas[indice])
    def jugar_de_nuevo():
      print("Quieres jugar de nuevo?\n")
      jugador = input("1.- Si 2.- No\n")
      if jugador == "1":
          iniciar()
    print("Adivina el número:\n")
    time.sleep(1)
    print("Pista: El número es entre 1 y 99")
    for i in range(vida_jugador):
      time.sleep(1)
      jugador = (input())
      if jugador == numero_aleatorio:
          print("¡Felicidades! Adivinaste el número")
          time.sleep(1)
          print()
          jugar_de_nuevo()
      else:
          print("Número equivocado, inténtalo de nuevo\n")
          if i < len(pistas):
              mostrar_pista(i)
      if i == vida_jugador - 2: # comprueba si la vida del jugador es igual a 1 (0)
        print("Última oportunidad")
    print("Lo siento, has perdido. El número era", str(numero_aleatorio) + "\n")
    time.sleep(1)
    print()
    jugar_de_nuevo()

iniciar()