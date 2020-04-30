import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class calibracion():
    
    #aqui establecemos todos los parametros para nuestra grafica
    def __init__(self, datos, tamano_figura = (16, 8), columnas = 1, titulo = "Ploteo de calibracion", 
                 ejes_graficas = [], etiquetas = [], marca = None):
        self.tamano_figura = tamano_figura
        self.columnas = columnas
        self.titulo = titulo
        self.datos = datos
        
        self.ejes_graficas = ejes_graficas
        self.etiquetas = etiquetas
        self.marca = marca
        self.ejex = ("Tiempo almacenado ") 
        self.ejey= ("Masa dentro o fuera") 
    #Calcular la cantidad de filas para que las gráficas quepan en las columnas definidas.
    def __get_row_number(self):
      
           
        
        n = len(self.datos)
        if n >= self.columnas:
            return (n // self.columnas)
        return 1
    
    #asignamos los nombres por default de tiempo almacenado para el eje x y masa adentro o afuera 
    
    def __fill_name_list(self):
        
        
        n = len(self.datos)
        m = len(self.ejes_graficas)
        if n > m:
            for i in range(n-m):
                self.ejes_graficas.append(("Tiempo almacenado".format(i+m+1),"Masa dentro o fuera".format(i+m+1)))
        

    #Si el usuario no asigna un valor o nombre a las etiquetas de la grafica se asignara por default el nimbre y 
    #aumentara el numero segun se fueron metiendo 
    def __fill_graph_names(self):
       
        n = len(self.datos)
        m = len(self.etiquetas)
        if n > m:
            for i in range(n-m):
                self.etiquetas.append("Grafica{}".format(i+m+1))
    
    
    
    #funcion principal para plotear    
    def plot_line(self):
        self.fig = plt.figure(figsize = self.tamano_figura)
        self.filas = self.__get_row_number()
        self.__fill_name_list()
        self.__fill_graph_names()
        i = 1
        for tupla in zip(self.datos, self.ejes_graficas):
            ax = self.fig.add_subplot(self.filas, self.columnas, i)
            ax.set_xlabel(tupla[1][0])
            ax.set_ylabel(tupla[1][1])
            ax.grid(b = True)
            color_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            mfc_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            if self.marca:
                lines = ax.plot(tupla[0][0], tupla[0][1], color = color_tuple, marker = self.marca, mec = mfc_tuple, mfc = mfc_tuple)
            lines = ax.plot(tupla[0][0], tupla[0][1], color = color_tuple)
            ax.set_title(self.etiquetas[i - 1])
            i += 1
            
        self.fig.suptitle(self.titulo, fontsize = 20)
        self.fig.tight_layout()
        self.fig.subplots_adjust(top=0.88)
        plt.show()
    
    #podemos hacer lineas sobrepuestas es decir varias lineas dentro de un mismo cuadro de grafica 
    def plot_line_overlapped(self):
        self.fig = plt.figure(figsize = self.tamano_figura)
        plt.grid(b = True)
        self.__fill_name_list()
        self.__fill_graph_names()
        i = 1
        for tupla in zip(self.datos, self.ejes_graficas):
            color_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            mfc_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            if self.marca:
                plt.plot(tupla[0][0], tupla[0][1], color = color_tuple, marker = self.marca, mec = mfc_tuple, mfc = mfc_tuple)
            plt.plot(tupla[0][0], tupla[0][1], color = color_tuple)
        plt.title(self.titulo, fontsize = 20)
        plt.xlabel(self.ejex,fontsize = 18)
        plt.ylabel(self.ejey,fontsize = 18)
        plt.legend(self.etiquetas)
        plt.show()
        
class budgets():
    
    #aqui establecemos todos los parametros para nuestra grafica
    def __init__(self, datos, tamano_figura = (16, 8), columnas = 1, titulo = "Presupuestos Celulares", 
                 ejes_graficas = [], etiquetas = [], marca = None):
        self.tamano_figura = tamano_figura
        self.columnas = columnas
        self.titulo = titulo
        self.datos = datos  
        self.ejes_graficas = ejes_graficas
        self.etiquetas = etiquetas
        self.marca = marca
        self.ejex = ("Mes-Año") 
        self.ejey= ("Acre-Pie") 
        
    #Calcular la cantidad de filas para que las gráficas quepan en las columnas definidas.
    def __get_row_number(self):
        n = len(self.datos)
        if n >= self.columnas:
            return (n // self.columnas)
        return 1
    
    #asignamos los nombres por default de tiempo almacenado para el eje x y masa adentro o afuera 
    
    def __fill_name_list(self):
        
        
        n = len(self.datos)
        m = len(self.ejes_graficas)
        if n > m:
            for i in range(n-m):
                self.ejes_graficas.append(("Mes-Año".format(i+m+1),"Acre-Pie".format(i+m+1)))
        

    #Si el usuario no asigna un valor o nombre a las etiquetas de la grafica se asignara por default el nimbre y 
    #aumentara el numero segun se fueron metiendo 
    def __fill_graph_names(self):
       
        n = len(self.datos)
        m = len(self.etiquetas)
        if n > m:
            for i in range(n-m):
                self.etiquetas.append("Grafica{}".format(i+m+1))
    
    
    
    #funcion principal para plotear    
    def plot_line(self):
        self.fig = plt.figure(figsize = self.tamano_figura)
        self.filas = self.__get_row_number()
        self.__fill_name_list()
        self.__fill_graph_names()
        i = 1
        for tupla in zip(self.datos, self.ejes_graficas):
            ax = self.fig.add_subplot(self.filas, self.columnas, i)
            ax.set_xlabel(tupla[1][0])
            ax.set_ylabel(tupla[1][1])
            ax.grid(b = True)
            color_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            mfc_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            if self.marca:
                lines = ax.plot(tupla[0][0], tupla[0][1], color = color_tuple, marker = self.marca, mec = mfc_tuple, mfc = mfc_tuple)
            lines = ax.plot(tupla[0][0], tupla[0][1], color = color_tuple)
            ax.set_title(self.etiquetas[i - 1])
            i += 1
            
        self.fig.suptitle(self.titulo, fontsize = 20)
        self.fig.tight_layout()
        self.fig.subplots_adjust(top=0.88)
        plt.show()
    
    #podemos hacer lineas sobrepuestas es decir varias lineas dentro de un mismo cuadro de grafica 
    def plot_line_overlapped(self):
        self.fig = plt.figure(figsize = self.tamano_figura)
        plt.grid(b = True)
        self.__fill_name_list()
        self.__fill_graph_names()
        i = 1
        for tupla in zip(self.datos, self.ejes_graficas):
            color_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            mfc_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            if self.marca:
                plt.plot(tupla[0][0], tupla[0][1], color = color_tuple, marker = self.marca, mec = mfc_tuple, mfc = mfc_tuple)
            plt.plot(tupla[0][0], tupla[0][1], color = color_tuple)
        plt.title(self.titulo, fontsize = 20)
        plt.xlabel(self.ejex,fontsize = 18)
        plt.ylabel(self.ejey,fontsize = 18)
        plt.legend(self.etiquetas)
        plt.show()

class farm():
    
    #aqui establecemos todos los parametros para nuestra grafica
    def __init__(self, datos, tamano_figura = (16, 8), columnas = 1, titulo = "Presupuesto de granja", 
                 ejes_graficas = [], etiquetas = [], marca = None):
        self.tamano_figura = tamano_figura
        self.columnas = columnas
        self.titulo = titulo
        self.datos = datos  
        self.ejes_graficas = ejes_graficas
        self.etiquetas = etiquetas
        self.marca = marca
        self.ejex = ("Hectareas ") 
        self.ejey= ("Costo") 
        
    #Calcular la cantidad de filas para que las gráficas quepan en las columnas definidas.
    def __get_row_number(self):
        n = len(self.datos)
        if n >= self.columnas:
            return (n // self.columnas)
        return 1
    
    #asignamos los nombres por default de tiempo almacenado para el eje x y masa adentro o afuera 
    
    def __fill_name_list(self):
        
        
        n = len(self.datos)
        m = len(self.ejes_graficas)
        if n > m:
            for i in range(n-m):
                self.ejes_graficas.append(("Hectareas".format(i+m+1),"Costo".format(i+m+1)))
        

    #Si el usuario no asigna un valor o nombre a las etiquetas de la grafica se asignara por default el nimbre y 
    #aumentara el numero segun se fueron metiendo 
    def __fill_graph_names(self):
       
        n = len(self.datos)
        m = len(self.etiquetas)
        if n > m:
            for i in range(n-m):
                self.etiquetas.append("Grafica{}".format(i+m+1))
    
    
    
    #funcion principal para plotear    
    def plot_line(self):
        self.fig = plt.figure(figsize = self.tamano_figura)
        self.filas = self.__get_row_number()
        self.__fill_name_list()
        self.__fill_graph_names()
        i = 1
        for tupla in zip(self.datos, self.ejes_graficas):
            ax = self.fig.add_subplot(self.filas, self.columnas, i)
            ax.set_xlabel(tupla[1][0])
            ax.set_ylabel(tupla[1][1])
            ax.grid(b = True)
            color_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            mfc_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            if self.marca:
                lines = ax.plot(tupla[0][0], tupla[0][1], color = color_tuple, marker = self.marca, mec = mfc_tuple, mfc = mfc_tuple)
            lines = ax.plot(tupla[0][0], tupla[0][1], color = color_tuple)
            ax.set_title(self.etiquetas[i - 1])
            i += 1
            
        self.fig.suptitle(self.titulo, fontsize = 20)
        self.fig.tight_layout()
        self.fig.subplots_adjust(top=0.88)
        plt.show()
    
    #podemos hacer lineas sobrepuestas es decir varias lineas dentro de un mismo cuadro de grafica 
    def plot_line_overlapped(self):
        self.fig = plt.figure(figsize = self.tamano_figura)
        plt.grid(b = True)
        self.__fill_name_list()
        self.__fill_graph_names()
        i = 1
        for tupla in zip(self.datos, self.ejes_graficas):
            color_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            mfc_tuple = tuple(map(tuple,np.random.rand(1,3)))[0]
            if self.marca:
                plt.plot(tupla[0][0], tupla[0][1], color = color_tuple, marker = self.marca, mec = mfc_tuple, mfc = mfc_tuple)
            plt.plot(tupla[0][0], tupla[0][1], color = color_tuple)
        plt.title(self.titulo, fontsize = 20)
        plt.xlabel(self.ejex,fontsize = 18)
        plt.ylabel(self.ejey,fontsize = 18)
        plt.legend(self.etiquetas)
        plt.show()


class parselas:
    #creamos la figura principal 
    def __init__(self, n_x_m, alto_x_ancho = [3,3], titulo = 'Título principal'):
        
        # Separamos la tupla de dimensiones en dos entes por separado.
        self.n = n_x_m[0]
        self.m = n_x_m[1]
        # Separamos la tupla de cuánto se alejan cada subplot del otro respecto a una altura y anchura
        h_pad = alto_x_ancho[0]
        w_pad = alto_x_ancho[1]

        # Inicializamos la figura desde matplotlib con un tamaño especial para usar en Jupyter. Se coloca el
        # título establecido desde un principio y a una altura considerable para no intervenir con lso gráficos.
        fig = plt.figure(figsize = (10,6))
        fig.suptitle(titulo, y = 1.05)
        
        # Se crean los ejes deseados, al igual que se impone la distancia entre subplots.
        self.ax = fig.subplots(self.n, self.m)
        fig.tight_layout(h_pad = h_pad, w_pad = w_pad)
        
        # Creamos el objeto que nos permitirá mannipular a los gráficos de manera cómoda.
        if self.n == 1 and self.m == 1:
            self.matriz_obj = 0
        else:
            self.matriz_obj = np.zeros((self.n,self.m), dtype = "object")
            
            
    def plot_area(self, coord, obj_graf, x, y, **kwargs):
       
        # Se arregla el problema que surge al intentar invocar una figura con un solo subplot o de 2x1 o 1x2.
        self.coord = coord
        if self.n == 1 and self.m == 1:
            self.matriz_obj = obj_graf(self.ax, x, y)
        elif self.n == 1 or self.m == 1:
            self.ax.shape = (self.n, self.m)
            self.matriz_obj[self.coord] = obj_graf(self.ax[self.coord], x, y)
        else:
            self.matriz_obj[self.coord] = obj_graf(self.ax[self.coord], x, y)
        # Se regresa el objeto Figura como tal, ya que hasta este punto no se grafica aún. 
        return self
    
    
    def show(self):
       
        # Ejecuta un for sobre nuestro arreglo de objetos.
        for _,matriz in np.ndenumerate(self.matriz_obj):
            # No hace nada si no se ha puesto nada en determinado sector de la figura
            if matriz == 0:
                pass
            else:
            # Invoca el método dibujar() que está en la clase de la gráfica que se quiera dibujar.
                matriz.dibujar()
                
    def set_axes(self,coord, **kwargs):
       
        # Aquí se toma el ente kwargs y se asigna a una variables del objeto en cuestión
        self.diccionario = kwargs
        # Se usan las características introducidas en el diccionario.
        self.ax[coord].set_xlabel(self.diccionario['xlabel'])
        self.ax[coord].set_ylabel(self.diccionario['ylabel'])
        self.ax[coord].set_xlim(self.diccionario['xlim'])
        self.ax[coord].set_ylim(self.diccionario['ylim'])
        self.ax[coord].grid('grid')
        self.ax[coord].set_xticks(self.diccionario['ticks']['xtick_major'])
        self.ax[coord].set_yticks(self.diccionario['ticks']['ytick_major'])
        self.ax[coord].set_xticks(self.diccionario['ticks']['xtick_minor'], minor = True)
        self.ax[coord].set_yticks(self.diccionario['ticks']['ytick_minor'], minor = True)

        self.ax[coord].spines['right'].set_visible(self.diccionario['spines']['right'])
        self.ax[coord].spines['left'].set_visible(self.diccionario['spines']['left'])
        self.ax[coord].spines['top'].set_visible(self.diccionario['spines']['top'])
        self.ax[coord].spines['bottom'].set_visible(self.diccionario['spines']['bottom'])

class Area_plot:
    #Dibujamos las figuras 
    def __init__(self, axes, x, y):
        
        # Simplemente se toman los parámetros de la clase y los volvemos Atributos
        self.ax = axes
        self.x = x
        self.y = y
              
        
    def dibujar(self):
        
        self.ax.stackplot(self.x, self.y)
