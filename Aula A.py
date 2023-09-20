"""
Funções decoradoras recebem uma função como parametro e decoram/modificam/configura ela, retornando uma nova, para ser
usada no lugar
"""
from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        star_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - star_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f} para ser executada')
        return resultado
    return interna


@velocidade  # Função decoradora
def demora():
    for i in range(10):
        sleep(1)
        print(i)


demora()
