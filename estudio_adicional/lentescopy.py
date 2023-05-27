import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def magnificacion(d, imagen):
    magnificacion = d/imagen
    altura_imagen= h*magnificacion
    return(altura_imagen)

def grafica_lente_convergente(f, d, h, foco, imagen):
    fig, ax = plt.subplots()
    
    # Crear Wedges{cuñás}
    div = 7
    R = (4*(6**2+5**2)**(1/2))/div
    wedge_1 = mpatches.Wedge((-(R/2)+d, 0), R, 0, 360, color='magenta', alpha = 0)
    wedge_2 = mpatches.Wedge(((R/2)+d, 0), R, 0, 360, color='aquamarine')
    
    # Agregar el Wedge al gráfico
    ax.add_patch(wedge_1)
    ax.add_patch(wedge_2)

    # Agregar las líneas con alto valor de zorder
    plt.axvline(x=0, color='k', zorder=10)  # Línea vertical
    plt.axhline(y=0, color='k', zorder=10)  # Línea horizontal

    # Recortar una cuña con la otra para mostrar la intersección
    wedge_2.set_clip_path(wedge_1)
    
    ax.set_aspect('equal')  # Para asegurar que se grafique simetricamente
    plt.title('sistema de lente convergente.')
    plt.grid(True)
    plt.legend()
    
    #agrego los rayos
    rayos_incidentes(f, d, h, foco,imagen)
    
def grafica_lente_divergente(f, d, h, foco, imagen):
    fig, ax = plt.subplots()

    # Crear Wedges{cuñas}
    wedge_1 = mpatches.Wedge((-57+d, 0), 55, 0, 360, color='white', alpha = 1)
    wedge_2 = mpatches.Wedge((57+d, 0), 55, 0, 360, color='white')

    #crear cuadrado
    cuadrado_1 = plt.Polygon([[-20+d,-24.8], [-20+d,24.8], [20+d,24.8], [20+d,-24.8]], color = 'blue')

    # Agregar el Wedge al gráfico
    ax.add_patch(cuadrado_1)
    ax.add_patch(wedge_1)
    ax.add_patch(wedge_2)

    # Agregar las líneas con alto valor de zorder
    plt.axvline(x=0, color='k', zorder=10)  # Línea vertical
    plt.axhline(y=0, color='k', zorder=10)  # Línea horizontal

    ax.set_aspect('equal')  # Para asegurar que se grafique simetricamente
    plt.title('sistema de lente divergente.')
    plt.grid(True)

    #agrego los rayos
    rayos_incidentes(f, d, h, foco,imagen)

def rayos_incidentes(f, d, h, foco,imagen):
    if h != 0:
        #rayo paralelo
        plt.plot([0, d], [h, h], color = 'red', linewidth = 1)

        # pendiente del rayo que pasa por el foco
        x1, y1 = [0, foco[0]], [h, 0]
        m = (y1[1] - y1[0]) / (x1[1] - x1[0])
        # rayo que pasa por el foco
        x2 = [0, d]
        y2 = [h, h + m * (x2[1] - x2[0])]
        plt.plot(x2, y2, color='green', linewidth=1)

        #recta que pasa por el centro
        plt.plot([0, d], [h, 0], color='blue', linewidth=1)

    else:
        if d == f:
            plt.plot([0, d], [0, 0], color='red', linewidth=1)
            plt.plot([0, d], [0, 14], color='green', linewidth=1)
            plt.plot([0, d], [0, -14], color='blue', linewidth=1)

    #eje "x" y eje "y"
    plt.axvline(x=0, color='k', zorder=10)  # Línea vertical
    plt.axhline(y=0, color='k', zorder=10)  # Línea horizontal
    
    #punto focal
    plt.plot(d-f, 0, marker = 'o', color = 'k')
    plt.plot(d+f, 0, marker = 'o', color = 'k')

    #agrego rayos emergentes
    rayos_emergentes(f, d, h, foco, imagen)

    plt.show()

def rayos_emergentes(f, d, h, foco, imagen):
    if h != 0:
        #rayo que pasa por el foco emerge paralelo
        plt.plot([d, d+imagen], [-h, -h], color = 'green', linewidth = 1)

        # pendiente del rayo que emerge por el foco
        x1, y1 = [0, foco[0]], [h, 0]
        m = -(y1[1] - y1[0]) / (x1[1] - x1[0])
        # rayo que emerge por el foco
        x2 = [d, d + imagen]
        y2 = [h, h - m * (x2[1] - x2[0])]
        plt.plot(x2, y2, color='red', linewidth=1)

        #recta que pasa por el centro sigue por el centro hata la imagen
        plt.plot([d, d+imagen], [0, -h], color='blue', linewidth=1)

    else:
        if d == f:
            plt.plot([d, d+f], [14, 0], color='red', linewidth=1)
            plt.plot([d, d+f], [0, 0], color='green', linewidth=1)
            plt.plot([d, d+f], [-14, 0], color='blue', linewidth=1)

    #punto focal
    plt.plot(d-f, 0, marker = 'o', color = 'k')
    plt.plot(d+f, 0, marker = 'o', color = 'k')
    plt.show()

f = 5#int(input('ingrese el foco de el lente\n')) #distancia focal
d = 10#int(input('a que distancia esta el lente del objeto?\n')) #a que distancia esta el lente?
h = 3#int(input('a que altura respecto al eje axial esta ubicado el objeto?\n')) #altura de el lente
foco = [d-f, 0] #coordenada del foco
imagen = 1/((1/f)-(1/d))

grafica_lente_convergente(f, d, h, foco, imagen)

# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# def grafica_lente_divergente(f, d, h, foco, imagen):
#     fig, ax = plt.subplots()

#     # Crear Wedges
#     div = 7
#     R = (4*(6**2+5**2)**(1/2))/div
#     wedge_1 = mpatches.Wedge((-(R/2)+d, 0), R, 0, 360, color='yellow', alpha = 0.5)
#     wedge_2 = mpatches.Wedge(((R/2)+d, 0), R, 0, 360, color='yellow', alpha = 0.5)

#     #crear cuadrado
#     cuadrado_1 = plt.Polygon([[-3.89+d,-3.89], [-3.89+d,3.89], [3.89+d,3.89], [3.89+d,-3.89]], color = 'blue')

#     # Agregar el Wedge al gráfico
#     ax.add_patch(cuadrado_1)
#     ax.add_patch(wedge_1)
#     ax.add_patch(wedge_2)

#     # Agregar las líneas con alto valor de zorder
#     plt.axvline(x=0, color='k', zorder=10)  # Línea vertical
#     plt.axhline(y=0, color='k', zorder=10)  # Línea horizontal

#     #autoescala
#     ax.autoscale(tight=True)
#     ax.set_aspect('equal')  # Para asegurar que se grafique simetricamente

#     plt.title('sistema de lente divergente.')
#     plt.grid(True)
#     plt.show()

# f = 5#int(input('ingrese el foco de el lente\n')) #distancia focal
# d = 10#int(input('a que distancia esta el lente del objeto?\n')) #a que distancia esta el lente?
# h = 3#int(input('a que altura respecto al eje axial esta ubicado el objeto?\n')) #altura de el lente
# foco = [d-f, 0] #coordenada del foco
# imagen = 1/((1/f)-(1/d))

# grafica_lente_divergente(f, d, h, foco, imagen)
