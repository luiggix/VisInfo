#!/usr/bin/env python
# coding: utf-8

# # Paletas Brewer
# Cisneros Aguilar Sara Kenia\
# Diaz Moreno Rodrigo

# In[ ]:


from IPython.display import clear_output
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


def menu_principal(): 
    """
    Despliega el menú principal y retorna la opción elegida por el 
    usuario recibiendo un número entero como entrada
    """
    print("0) Salir")
    print("1) Paleta Normal")
    print("2) Paleta colorblind friendly")
    opc=input("Ingresa la opcion: ")
    clear_output()
    return opc


# In[ ]:


def submenu():
    """
    Despliega el submenú y retorna la opción elegida por el 
    usuario recibiendo un número entero como entrada
    """
    print("1) Paleta Divergente")
    print("2) Paleta Secuencial")
    print("3) Paleta Cualitativa")
    opc=input("Ingresa la opcion: ")
    clear_output()
    return opc


# In[ ]:


def divergente():
    """
    Despliega las opciónes para escoger una paleta tipo divergente y retorna la opción elegida por el 
    usuario recibiendo un núúmero entero como entrada
    """
    print("1) Escoger paleta")
    print("2) Crear paleta")
    opc=input("Ingresa la opcion: ")
    clear_output()
    return opc


# In[ ]:


def paleta_div():
    """
    Muestra las diferentes combinaciones de color para una paleta de tipo divergente, 
    regresando la combinacion escogida, mediante un número entero como entrada.
    """
    lista=["BrBG","RdBu_r","coolwarm","YlGnBu"]
    plt.figure(1)
    sns.palplot(sns.color_palette("BrBG", 7))
    plt.title("1) Paleta BrBG")
    plt.figure(2)
    sns.palplot(sns.color_palette("RdBu_r", 7))
    plt.title("2) Paleta RdBu_r")
    plt.figure(3)
    sns.palplot(sns.color_palette("coolwarm", 7))
    plt.title("3) Paleta coolwarm")
    plt.figure(4)
    sns.palplot(sns.color_palette("YlGnBu", 7))
    plt.title("4) Paleta YlGnBu")
    plt.show()
    opc=int(input("Ingresa el numero de la opcion: "))
    sns.set_palette(lista[opc-1])


# In[ ]:


def creacion_div():
    """
    Configura una paleta de tipo divergente basado en colores del conjunto hus1

    Parametros:
    c1 -- primer color (en grados del sistema de colores hus1)
    c2 -- segundo color (en grados del sistema de colores hus1)
    s  -- saturacíon del color 
    l  -- luminocidad del color
    """
    c1=int(input("Ingrese el grado del color 1: "))
    c2=int(input("Ingrese el grado del color 2: "))
    s=int(input("Ingrese la saturacion: "))
    l=int(input("Ingrese la luminocidad: "))
    color=sns.diverging_palette(c1, c2, s=s, l=l, n=7)
    sns.palplot(color)
    plt.title("Paleta creada")
    sns.set_palette(color)


# In[ ]:


def secuencial():
    """
    Despliega las opciónes para escoger una paleta tipo secuencial y retorna la opción elegida por el 
    usuario recibiendo un número entero como entrada
    """
    print("1) Escoger paleta")
    print("2) Crear paleta")
    opc=input("Ingresa la opcion: ")
    clear_output()
    return opc


# In[ ]:


def paleta_sec():
    """
    Muestra las diferentes combinaciones de color para una paleta de tipo secuencial, 
    regresando la combinacion escogida, mediante un número entero como entrada.
    """
    lista=["Blues","BuGn","Oranges","Greys"]
    plt.figure(1)
    sns.palplot(sns.color_palette("Blues",7))
    plt.title("1) Paleta Blues")
    plt.figure(2)
    sns.palplot(sns.color_palette("BuGn",7))
    plt.title("2) Paleta BuGn")
    plt.figure(3)
    sns.palplot(sns.color_palette("Oranges", 7))
    plt.title("3) Paleta Oranges")
    plt.figure(4)
    sns.palplot(sns.color_palette("Greys", 7))
    plt.title("4) Paleta Greys")
    plt.show()
    opc=int(input("Ingresa el numero de la opcion: "))
    sns.set_palette(lista[opc-1])


# In[ ]:


def creacion_sec():
    """
    Configura una paleta de tipo secuencial basado en colores del conjunto hus1

    Parametros:
    c1 -- color (en grados del sistema de colores hus1)
    l  -- luminocidad de la paleta
    """
    c1=int(input("Ingrese el grado del color: "))
    l=int(input("Ingrese la luminocidad: "))
    l=l/100
    color=sns.cubehelix_palette(7, start=c1, rot=0, light=l, reverse=False)
    sns.palplot(color)
    plt.title("Paleta creada")
    sns.set_palette(color)


# In[ ]:


def cualitativo():
    """
    Despliega las opciónes para escoger una paleta tipo cualitativo y retorna la opción elegida por el 
    usuario recibiendo un número entero como entrada
    """
    print("1) Escoger paleta")
    print("2) Crear paleta")
    opc=input("Ingresa la opcion: ")
    clear_output()
    return opc


# In[ ]:


def paleta_cual():
    """
    Muestra las diferentes combinaciones de color para una paleta de tipo cualitativo, 
    regresando la combinacion escogida, mediante un número entero como entrada.
    """
    lista=["pastel","Paired","Set1","Set2"]
    plt.figure(1)
    sns.palplot(sns.color_palette("pastel",7))
    plt.title("1) Paleta pastel")
    plt.figure(2)
    sns.palplot(sns.color_palette("Paired",7))
    plt.title("2) Paleta Paired")
    plt.figure(3)
    sns.palplot(sns.color_palette("Set1", 7))
    plt.title("3) Paleta Set1")
    plt.figure(4)
    sns.palplot(sns.color_palette("Set2", 7))
    plt.title("4) Paleta Set2")
    plt.show()
    opc=int(input("Ingresa el numero de la opcion: "))
    sns.set_palette(lista[opc-1])


# In[ ]:


def creacion_cual():
    """
    Configura una paleta de tipo cualitativo
    
    Parámetros:
    l -- lista de colores en formato hexadecimal
    """
    l=input("Ingrese los colores en formato hexadecimal, separados por espacios: ")
    color=sns.color_palette(l.split())
    sns.palplot(color)
    plt.title("Paleta creada")
    sns.set_palette(color)


# In[ ]:


def run():
    """
    Permite ingresar a un menú de selección de paletas de color
    
    Estructura general:

    0 -- termina el programa
    1 -- opciones para paletas dirigidas a personas sin discapacidad visual
    2 -- configura la paleta de colores dirirgida a personas con discapacidad visual
    """
    salir=False
    while not(salir):
        opcion=menu_principal()

        if opcion=="0":# Salir
            salir=True

        if opcion== "1":#Paleta Normal
            op=submenu()

            if op == "1":#Paleta Divergente
                opc=divergente()

                if opc== "1":# Escoger paleta
                    paleta_div()
                    print("Paleta Seleccionada")
                    break

                if opc== "2":#Crear paleta
                    creacion_div()
                    print("Paleta Seleccionada")
                    break
            if op=="2":#Paleta Secuencial
                opc=secuencial()

                if opc=="1":#Escoger paleta
                    paleta_sec()
                    print("Paleta Seleccionada")
                    break
                if opc=="2":#Crear paleta
                    creacion_sec()
                    print("Paleta Seleccionada")
                    break

            if op=="3":#Paleta Cualitativa
                opc=cualitativo()

                if opc=="1":#Escoger paleta
                    paleta_cual()
                    print("Paleta Seleccionada")
                    break
                if opc=="2":#Crear paleta
                    creacion_cual()
                    print("Paleta Seleccionada")
                    break
        if opcion=="2":#Paleta colorblind
            color=sns.color_palette("colorblind",7)
            sns.set_palette(color)
            sns.palplot(color)
            plt.title("Paleta colorblind")
            print("Paleta Seleccionada")
            break
            
    print("¡Vuelva pronto!")

