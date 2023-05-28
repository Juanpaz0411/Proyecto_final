import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Lentes:
    def __init__(self, **kwargs):
        self.diccionario = kwargs
        
        opciones = {'f': 'foco', 'd': 'distancia de objeto', 'imagen': 'distancia imagen'}
        
        for clave, descripcion in opciones.items():
            if clave not in self.diccionario:
                print(f'Falta el valor de {descripcion}')
        
        if not any(opcion in self.diccionario for opcion in opciones):
            print('No se proporcionaron valores.')

    def calcular_faltante(self):
        resultado = {}
        
        try:
            if 'f' not in self.diccionario:
                d = self.diccionario['d']
                imagen = self.diccionario['imagen']
                f = 1 / (1 / d + 1 / imagen)
                resultado['f'] = f
                resultado['d'] = self.diccionario['d']
                resultado['imagen'] = self.diccionario['imagen']
                resultado['h'] = self.diccionario['h']
                print(f'el foco es: {f}')
            
            if 'd' not in self.diccionario:
                f = self.diccionario['f']
                imagen = self.diccionario['imagen']
                d = (f * imagen) / (imagen - f)
                resultado['f'] = self.diccionario['f']
                resultado['d'] = d
                resultado['imagen'] = self.diccionario['imagen']
                resultado['h'] = self.diccionario['h']
                print(f'El objeto está a: {d}')
            
            if 'imagen' not in self.diccionario:
                f = self.diccionario['f']
                d = self.diccionario['d']
                imagen = (f * d) / (d - f)
                resultado['f'] = self.diccionario['f']
                resultado['d'] = self.diccionario['d']
                resultado['imagen'] = imagen
                resultado['h'] = self.diccionario['h']
                print(f'la imagen esta a: {imagen}')
            
        except ZeroDivisionError:
            if 'd' not in self.diccionario:
                resultado['f'] = self.diccionario['f']
                resultado['d'] = 'oo'
                resultado['imagen'] = self.diccionario['imagen']
                resultado['h'] = self.diccionario['h']
                print(f'El objeto está ubicado muy lejos del lente, ya que la imagen está ubicada en el foco: {f}')
            if 'imagen' not in self.diccionario:
                resultado['f'] = self.diccionario['f']
                resultado['d'] = self.diccionario['d']
                resultado['imagen'] = 0
                resultado['h'] = self.diccionario['h']
                print(f'La imagen está en el infinito ya que el objeto está en el foco: {d}')

        return resultado
    
    def magnificacion(self, diccionario):
        f = diccionario['f']
        d = diccionario['d']
        imagen = diccionario['imagen']
        h = diccionario['h']

        magnificacion = -imagen / d
        altura_imagen = h * magnificacion
        print(f'La magnificación es: {magnificacion}')

        if f>0:
            self.grafica_lente_convergente(f, d, h, imagen, altura_imagen)
        elif f<0:
            self.grafica_lente_divergente(f, d, h, imagen, altura_imagen)
    
    def rayos_incidentes(self, f, d, h,imagen):
        #rayo paralelo
        plt.plot([-abs(d), 0], [h, h], color = 'red', linewidth = 2.5)

        # pendiente del rayo que pasa por el foco
        x1, y1 = [-abs(d), -abs(f)], [h, 0]
        try:
            m_f = (y1[1] - y1[0]) / (x1[1] - x1[0])
        except ZeroDivisionError:
            m_f=-500
            print('imagen en el infinito')

        # rayo que pasa por el foco
        x2 = [-abs(d), 0]
        y2 = [h, h + m_f * (x2[1] - x2[0])]
        plt.plot(x2, y2, color='green', linewidth=2.5)

        # recta vertical en x=d
        x3 = [0,0]
        y3 = [-50, 50]
        plt.plot(x3, y3, color='k', linewidth=0.5, linestyle = '--')

        # cálculo de la intersección
        xi = 0
        yi = y2[0] + m_f * (xi - x2[0])
        interseccion = [xi, yi]

        # pendiente de la recta que pasa por el centro
        x1, y1 = [0, d], [h, 0]
        try:
            m_c = (y1[1] - y1[0]) / (x1[1] - x1[0])
        except ZeroDivisionError:
            m_c = float('inf')
            print('Pendiente infinita')

        # recta que pasa por el centro
        x2 = [-d, 0]
        y2 = [h, h + m_c * (x2[1] - x2[0])]
        plt.plot(x2, y2, color='blue', linewidth=2.5)
        
        #punto focal
        plt.plot(-abs(f), 0, marker = 'o', color = 'k')
        plt.plot(abs(f), 0, marker = 'o', color = 'k')

        # vector de altura h ubicado en el origen
        plt.quiver(-abs(d), 0, 0, h, angles='xy', scale_units='xy', scale=1, color='yellow')

        #agrego rayos emergentes
        self.rayos_emergentes(f, d, h, imagen, interseccion, m_c)

        plt.show()


    def rayos_emergentes(self, f, d, h, imagen, list, m_centro):
        #rayo que pasa por el foco emerge paralelo
        plt.plot([0, d+100], [list[1], list[1]], color = 'green', linewidth = 2.5)

        #proyeccion del rayo que pasa por el foco emerge paralelo
        plt.plot([-200, 200], [list[1], list[1]], color = 'green', linewidth = 2.5, linestyle = '--')
        
        # pendiente del rayo que emerge por el foco
        x1, y1 = [0, f], [h, 0]
        try:
            m = -(y1[1] - y1[0]) / (x1[1] - x1[0])
        except ZeroDivisionError:
            m=-500
            print('imagen en el infinito')

        # rayo que emerge por el foco
        x2 = [0, d + 50]
        y2 = [h, h - m * (x2[1] - x2[0])]
        plt.plot(x2, y2, color='red', linewidth=2.5)

        # proyeccion del rayo que emerge por el foco
        x4 = [-200, 200]
        y4 = [h - m * (x4[0]), h - m * (x4[1])]
        plt.plot(x4, y4, color='red', linewidth=2.5, linestyle = '--')

        # rayo que emerge por el centro
        x_c= [0, d+50]
        y_c = [0, m_centro * (x_c[1] - x_c[0])]
        plt.plot(x_c, y_c, color='blue', linewidth=2.5)
        
        # proyeccion de el rayo que emerge por el centro
        x5 = [-200, 200]
        y5 = [ m_centro * (x5[0]), 0 + m_centro * (x5[1])]
        plt.plot(x5, y5, color='blue', linewidth=2.5, linestyle = '--')

        # Ecuación de la línea que emerge por el foco
        m1 = (y4[1] - y4[0]) / (x4[1] - x4[0])
        b1 = y4[0] - m1 * x4[0]

        # Ecuación del rayo que emerge por el centro
        m2 = (y5[1] - y5[0]) / (x5[1] - x5[0])
        b2 = y5[0] - m2 * x5[0]

        # Resolviendo para x
        try:
            x_intersect = (b2 - b1) / (m1 - m2)
            # Resolviendo para y
            y_intersect = m1 * x_intersect + b1

        except ZeroDivisionError:
            x_intersect = 0
            # Resolviendo para y
            y_intersect = 0

        #vector altura de la imagen
        plt.quiver(x_intersect, 0, 0, y_intersect, angles='xy', scale_units='xy', scale=1)
        print(f'la altura del objeto: {h}\n',f'altura de la imagen: {y_intersect}' if y_intersect != 0 else '') 

        #punto focal
        plt.show()

class LenteDivergente(Lentes):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = []

    def calcular_faltante(self):
        return super().calcular_faltante()
    
    def magnificacion(self, diccionario):
        return super().magnificacion(diccionario)
    

    def grafica_lente_divergente(self, f, d, h, imagen, altura_imagen):
        fig, ax = plt.subplots()

        # Crear Wedges
        div = 7
        R = (4*(6**2+5**2)**(1/2))/div
        wedge_1 = mpatches.Wedge((-R-0.5, 0), R, 0, 360, color='white')
        wedge_2 = mpatches.Wedge((R+0.5, 0), R, 0, 360, color='white')

        #crear cuadrado
        cuadrado_1 = plt.Polygon([[-3.85,-3.85], [-3.85,3.85], [3.85,3.85], [3.85,-3.85]], color = 'blue', alpha = 0.6)

        # Agregar el Wedge al gráfico
        ax.add_patch(cuadrado_1)
        ax.add_patch(wedge_1)
        ax.add_patch(wedge_2)

        # Agregar las líneas con alto valor de zorder
        # plt.axvline(x=0, color='k', zorder=10, linewidth=0.7)  # Línea vertical
        plt.axhline(y=0, color='k', zorder=10, linewidth=0.7)  # Línea horizontal

        #escala
        # ax.autoscale(tight=True)
        ax.set_aspect('equal')  # Para asegurar que se grafique simetricamente
        plt.title('sistema de lente divergente.')

        if d > 4*h :
            ax.set_xlim(-5-abs(f) , 5+abs(f))
        else:
            ax.set_xlim(-3-abs(imagen) if abs(imagen)+1 > abs(d) else -3-abs(d)  , 3+abs(imagen) if abs(imagen) > abs(d) else 3+abs(d)) if abs(imagen) <= 3*abs(h) else ax.set_xlim(-3-abs(d),3+abs(d)) 
        
        ax.set_ylim(-abs(h)-3 if abs(altura_imagen) < h else -3-abs(altura_imagen)  , abs(h)+3 if abs(altura_imagen) < h else 3+abs(altura_imagen)) if abs(altura_imagen)<=3*abs(imagen) else ax.set_ylim(-h-2, h+2)
    
        #agrego los rayos
        self.rayos_incidentes(f, d, h, imagen)

    def rayos_incidentes(self, f, d, h,imagen):
        #rayo paralelo
        plt.plot([-abs(d), 0], [h, h], color = 'red', linewidth = 2.5)

        # pendiente del rayo que pasa por el foco
        x1, y1 = [-abs(d), abs(f)], [h, 0]
        try:
            m_f = (y1[1] - y1[0]) / (x1[1] - x1[0])
        except ZeroDivisionError:
            m_f=-500
            print('imagen en el infinito')

        # rayo que pasa por el foco
        x2 = [-abs(d), 0]
        y2 = [h, h + m_f * (x2[1] - x2[0])]
        plt.plot(x2, y2, color='green', linewidth=2.5)

        # recta vertical en x=d
        x3 = [0,0]
        y3 = [-50, 50]
        plt.plot(x3, y3, color='k', linewidth=0.5, linestyle = '--')

        # cálculo de la intersección
        xi = 0
        yi = y2[0] + m_f * (xi - x2[0])
        interseccion = [xi, yi]

        # pendiente de la recta que pasa por el centro
        x1, y1 = [0, d], [h, 0]
        try:
            m_c = (y1[1] - y1[0]) / (x1[1] - x1[0])
        except ZeroDivisionError:
            m_c = float('inf')
            print('Pendiente infinita')

        # recta que pasa por el centro
        x2 = [-d, 0]
        y2 = [h, h + m_c * (x2[1] - x2[0])]
        plt.plot(x2, y2, color='blue', linewidth=2.5)
        
        #punto focal
        plt.plot(-abs(f), 0, marker = 'o', color = 'k')
        plt.plot(abs(f), 0, marker = 'o', color = 'k')

        # vector de altura h ubicado en el origen
        plt.quiver(-abs(d), 0, 0, h, angles='xy', scale_units='xy', scale=1, color='yellow')

        #agrego rayos emergentes
        self.rayos_emergentes(f, d, h, imagen, interseccion, m_c)

        plt.show()
    def rayos_emergentes(self, f, d, h, imagen, list, m_centro):
        return super().rayos_emergentes(f, d, h, imagen, list, m_centro)


class LenteConvergente(Lentes):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = []

    def calcular_faltante(self):
        resultado = super().calcular_faltante()
        # Imprimir el diccionario
        self.magnificacion(resultado)
        return resultado

    def magnificacion(self, diccionario):
        return super().magnificacion(diccionario)

    def grafica_lente_convergente(self,f, d, h, imagen, altura_imagen):
        fig, ax = plt.subplots()
        # Crear Wedges{cuñás}
        div = 7
        R = (4*(6**2+5**2)**(1/2))/div
        wedge_1 = mpatches.Wedge((-(R/2), 0), R, 0, 360, color='magenta', alpha = 0)
        wedge_2 = mpatches.Wedge(((R/2), 0), R, 0, 360, color='aquamarine')
        
        # Agregar el Wedge al gráfico
        ax.add_patch(wedge_1)
        ax.add_patch(wedge_2)

        # Agregar las líneas con alto valor de zorder
        # plt.axvline(x=0, color='k', zorder=10)  # Línea vertical
        plt.axhline(y=0, color='k', zorder=10, linewidth=0.7)  # Línea horizontal

        # Recortar una cuña con la otra para mostrar la intersección
        wedge_2.set_clip_path(wedge_1)
        
        #escala
        # ax.autoscale(tight=True)
        ax.set_aspect('equal')  # Para asegurar que se grafique simetricamente
        plt.title('sistema de lente convergente.')

        if d > 4*h :
            ax.set_xlim(-5-abs(f) , 5+abs(f))
        else:
            ax.set_xlim(-3-abs(imagen) if abs(imagen)+1 > abs(d) else -3-abs(d)  , 3+abs(imagen) if abs(imagen) > abs(d) else 3+abs(d)) if abs(imagen) <= 3*abs(h) else ax.set_xlim(-3-abs(d),3+abs(d)) 
        
        ax.set_ylim(-abs(h)-3 if abs(altura_imagen) < h else -3-abs(altura_imagen)  , abs(h)+3 if abs(altura_imagen) < h else 3+abs(altura_imagen)) if abs(altura_imagen)<=3*abs(imagen) else ax.set_ylim(-h-2, h+2)
    
        #agrego los rayos
        self.rayos_incidentes(f, d, h, imagen)

    def rayos_incidentes(self, f, d, h, imagen):
        return super().rayos_incidentes(f, d, h, imagen)
    
    def rayos_emergentes(self, f, d, h, imagen, list, m_centro):
        return super().rayos_emergentes(f, d, h, imagen, list, m_centro)

'''se usara la siguiente seccion de codigo para la presentación'''
def valor_faltante():
    diccionario = {}
    print('manejar una sola unidad (mm, cm, m), solo puede faltar uno de los tres datos foco, distancia de objeto, distancia de imagen')
    try:
        f = 10#input('ingrese el foco del lente (deje en blanco si falta):\n')
        if f:
            diccionario['f'] = float(f)
        d = 5#input('ingrese la distancia del lente al objeto (deje en blanco si falta):\n')
        if d:
            diccionario['d'] = abs(float(d))
        imagen = -10#input('ingrese la distancia de la imagen al objeto (deje en blanco si falta):\n')
        if imagen:
            diccionario['imagen'] = float(imagen)
        h = 4#input('ingrese la altura del objeto (deje en blanco si falta):\n')
        if h:
            diccionario['h'] = float(h)
        return diccionario
    except ValueError:
        print('Ingrese valores válidos')
        return valor_faltante()
    
# def valor_faltante():
#     diccionario = {}
#     print('manejar una sola unidad (mm, cm, m)')

#     opciones = [('f', 'Ingrese el foco del lente (deje en blanco si falta): '),
#                ('d', 'Ingrese la distancia del lente al objeto (deje en blanco si falta): '),
#                ('imagen', 'Ingrese la imagen del objeto (deje en blanco si falta): '), 
#                ('h','Ingrese la altura del objeto: ')]

#     for clave, mensaje in opciones:
#         while True:
#             valor = input(mensaje)
#             if valor:
#                 try:
#                     diccionario[clave] = float(valor)
#                     break
#                 except ValueError:
#                     print('Ingrese un valor numérico válido.')
#             else:
#                 break
    
#     return diccionario
    
diccionario = valor_faltante()
lente = LenteConvergente(**diccionario) if diccionario['f'] > 0 else LenteDivergente(**diccionario)
if len(diccionario) == 3:
    lente.calcular_faltante()
elif len(diccionario) == 4:
    lente.magnificacion(diccionario)
else:
    print('error, se necesitan minimo dos 3 datos para la ejecucion del programa')