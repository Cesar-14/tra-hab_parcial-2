from OpenGL.GL import *
from glew_wish import *
import glfw
import math
# from Principal import *

class Jugador:
    #unidades por segundo
    velocidad = 0.4
    posicion = [-0.2, 0.0, 0.0]
    tiempo_anterior = 0.0
    posicion = [-0.7, 0.7, 0.0]
    fase = 90.0
    avanzar = True
    window = None

    def dibujar(self):

        glPushMatrix()
        glTranslatef(self.posicion[0], self.posicion[1], 0.0)
        glBegin(GL_QUADS)
        # if colisionando():
        #     glColor3f(0,0,1)
        # else:
        #     glColor3f(1,0,0)
        glColor3f(1,0,0)
        glVertex3f(-0.05, 0.05,0.0)
        glVertex3f(0.05, 0.05,0.0)
        glVertex3f(0.05, -0.05,0.0)
        glVertex3f(-0.05, -0.05,0.0)
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor(0,0,0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(-0.05, 0.05, 0)
        glVertex3f(0.05, 0.05, 0)
        glVertex3f(0.05, -0.05, 0)
        glEnd()

        glPopMatrix()

    def actualizar(self):

        tiempo_actual = glfw.get_time()
        # Cuanto tiempo paso entre la ejecucion actual
        # y la inmediata anterior de esta funcion
        tiempo_delta = tiempo_actual - self.tiempo_anterior
        
        # Revisamos estados y realizamos acciones
        cantidad_movimiento = self.velocidad * tiempo_delta

        # Controles jugador
        estado_tecla_w = glfw.get_key(self.window, glfw.KEY_UP)
        estado_tecla_s = glfw.get_key(self.window, glfw.KEY_DOWN)
        estado_tecla_a = glfw.get_key(self.window, glfw.KEY_RIGHT)
        estado_tecla_d = glfw.get_key(self.window, glfw.KEY_LEFT)

        if estado_tecla_w == glfw.PRESS:
            self.posicion[1] = self.posicion[1] + cantidad_movimiento
        if estado_tecla_s == glfw.PRESS:
            self.posicion[1] = self.posicion[1] - cantidad_movimiento
        if estado_tecla_a == glfw.PRESS:
            self.posicion[0] = self.posicion[0] + cantidad_movimiento
        if estado_tecla_d == glfw.PRESS:
            self.posicion[0] = self.posicion[0] - cantidad_movimiento
        
        # if estado_tecla_w == glfw.PRESS:
        #     if not colisionando():
        #         posicion_cuadrado[1] = posicion_cuadrado[1] + cantidad_movimiento
        #     else:
        #         posicion_cuadrado = [-0.7, 0.7, 0.0]
        # if estado_tecla_s == glfw.PRESS:
        #     if not colisionando():
        #         posicion_cuadrado[1] = posicion_cuadrado[1] - cantidad_movimiento
        #     else:
        #         posicion_cuadrado = [-0.7, 0.7, 0.0]
        # if estado_tecla_a == glfw.PRESS:
        #     if not colisionando():
        #         posicion_cuadrado[0] = posicion_cuadrado[0] + cantidad_movimiento
        #     else:
        #         posicion_cuadrado = [-0.7, 0.7, 0.0]
        # if estado_tecla_d == glfw.PRESS:
        #     if not colisionando():
        #         posicion_cuadrado[0] = posicion_cuadrado[0] - cantidad_movimiento
        #     else:
        #         posicion_cuadrado = [-0.7, 0.7, 0.0]