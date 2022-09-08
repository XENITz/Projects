rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
opciones = [rock, paper, scissors]

#ELECCION DEL USUARIO
eleccion_usuario = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if eleccion_usuario >= 3 or eleccion_usuario < 0: 
  print("You typed an invalid number, you lose!")
else:
  posicion_usuario = opciones[eleccion_usuario]
  
  #ELECCION DE LA MAQUINA
  import random
  eleccion_maquina = random.randint(0, 2)
  posicion_maquina = opciones[eleccion_maquina]
    
  #IMAGENES DE LAS ELECCIONES
  print(posicion_usuario)
  print("Computer chose: ")
  print(posicion_maquina)
  
  #CONDICIONES DEL JUEGO
  #PIEDRA
  
  if eleccion_usuario == 0 and eleccion_maquina == 0:
    print("Tie")
  if eleccion_usuario == 0 and eleccion_maquina == 1:
    print("You lose")
  if eleccion_usuario == 0 and eleccion_maquina == 2:
    print("You win")
    
    #PAPEL
  if eleccion_usuario == 1 and eleccion_maquina == 0:
    print("You win")
  if eleccion_usuario == 1 and eleccion_maquina == 1:
    print("Tie")
  if eleccion_usuario == 1 and eleccion_maquina == 2:
    print("You lose")
  
  #TIJERAS
  if eleccion_usuario == 2 and eleccion_maquina == 0:
    print("You lose")
  if eleccion_usuario == 2 and eleccion_maquina == 1:
    print("You win")
  if eleccion_usuario == 2 and eleccion_maquina == 2:
    print("Tie")

