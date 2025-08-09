# Inicializamos pygame
import pygame

# Le indica a pygame que cierre sus funciones y deje de trabajar en segundo plano
import sys

import random

pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 800, 800

# Crea la ventana, toma una tupla que representa la dimension de la ventana en pixeles
pantalla = pygame.display.set_mode((ALTO, ANCHO))

# Establece el titulo que aparece en la barra superior
pygame.display.set_caption('Taller dabado pygame')

# Primera clase
class Jugador:
    # Metodo constructor, caracteristicas del jugador
    def __init__(self,x, y, color):
        # X, Y hacen referencia a la posicion
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = 5
    
    # Acciones que realiza el jugador - Polimorfismo : tener la misma palabra para realizar acciones diferentes
    def mover(self, direccion):
        if direccion == 'izquierda':
            self.x -= self.velocidad
        elif direccion == 'derecha':
            self.x += self.velocidad
        elif direccion == 'arriba':
            self.y -= self.velocidad
        elif direccion == 'abajo':
            self.y += self.velocidad
        
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - 50:
            self.x = ANCHO - 50

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - 50:
            self.y = ALTO - 50
        
    def dibujar (self,pantalla):
            
            # Draw.rect es para dinujar un rectangulo en la pantalla
            
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, 50,50) )

# Clase Enemigo
class Enemigo:

    def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color
            self.velocidad = 5
    # Movimiento
    def mover(self):
        self.x += random.choice([-self.velocidad, self.velocidad])
        self.y += random.choice([-self.velocidad, self.velocidad])

        # Limitar movimiento
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, 50, 50))

# Crear o instanciar objetos
jugador = Jugador(375, 275, (255,0,0)) # Jugador rojo en el centro
enemigo = Enemigo(100,100, (0,255,0)) # Enemigo verde


corriendo = True
# Bucle principal
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # es darle un click a la 'X' en la ventana
            corriendo = False
    
    # Obtener las teclas presionadas
    # Obtiene el estado de todas las teclas del teclado. Esta funcion nos devuelve una linea de valores que son true o folse de si una tecla esta presionada si o no
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador.mover('izquierda')
    if teclas[pygame.K_RIGHT]:
        jugador.mover('derecha')
    if teclas[pygame.K_UP]:
        jugador.mover('arriba')
    if teclas[pygame.K_DOWN]:
        jugador.mover('abajo')
    
    # Mover al enemigo
    enemigo.mover()

    # Colision
    if (jugador.x < enemigo.x + 50 and jugador.x > enemigo.x and jugador.y < enemigo.y + 50 and jugador.y + 50 > enemigo.y):
        print('Colision!!')
        corriendo = False
    
    # Rellenamos la pantalla de color negro
    pantalla.fill((0, 0, 0)) # RGB 
    
    jugador.dibujar(pantalla)
    enemigo.dibujar(pantalla)
    
    # Actualizacion de pantalla
    pygame.display.flip()

pygame.quit()
