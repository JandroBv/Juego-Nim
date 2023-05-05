import math
import random

class palos_juego:
    def __init__(self, no_palos):
        self.no_palos = no_palos
        self.max = 4
        self.min = 1
    
    def quitarPalos(self, palos):
        self.no_palos -= palos
    
    def imprimirPalos(self):
        for i in range(self.no_palos):
            print("|", end = " ")

    def turnoComputadora(self):
        pieza = "1" 
        posicion = self.minimax(pieza)['cantidad']
        return posicion

    def minimax(self,jugador):
        computadora = "1"
        jugador2 = "1" if jugador == "0" else "0"
        
        if self.no_palos == 0:
            return {'cantidad': None, 'puntuacion': -1 if jugador2 == computadora else 1} 
        
        if jugador == computadora:
            mejor_resultado = {'cantidad': None, 'puntuacion': -999}
        else:
            mejor_resultado = {'cantidad': None, 'puntuacion': 999}
        

        for i in range(self.min, min(self.max, self.no_palos)+1):
            self.no_palos -= i 
            tempVal = self.minimax(jugador2)
            self.no_palos += i

            tempVal['cantidad'] = i
            
            if jugador == computadora:
                if tempVal['puntuacion'] > mejor_resultado['puntuacion']:
                    mejor_resultado = tempVal
            else:
                if tempVal['puntuacion'] < mejor_resultado['puntuacion']:
                    mejor_resultado = tempVal

        return mejor_resultado

    def juego(self):
        resultado = 0
        while self.no_palos > 0:    
            self.imprimirPalos()
            while True:
                resultado = int(input(f"\nIngresa la cantidad de palos a quitar entre el {self.min} y el {self.max} "))        
                if self.max >= resultado >= self.min and resultado <= self.no_palos:
                    break; 
            self.quitarPalos(resultado)
            print(f"El jugador ha quitado {resultado}") 
            if self.no_palos == 0:
                print("\nLa computadora ha ganado!")
                break
            self.imprimirPalos()   
            computadora = self.turnoComputadora();
            self.quitarPalos(computadora)
            print(f"\nLa computadora ha quitado {computadora}")
            if self.no_palos == 0:
                print("\nEl jugador ha ganado")
            if self.no_palos < self.max:
                self.max = self.no_palos

            

numero_palos = random.randint(10,20)
tablero = palos_juego(numero_palos)

tablero.juego()
