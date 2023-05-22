import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Crear el gráfico
fig, ax = plt.subplots()

# Establecer los límites del plano cartesiano
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Cargar la imagen del lente delgado
lente_img = mpimg.imread(r'C:\Users\USUARIO WINDOWS\programacion\proyecto_final\lentes_imagenes\lente_convergente.png')

# Crear la imagen del lente en el origen (0, 0)
lente = plt.imshow(lente_img, extent=[-1, 1, -1, 1])

# Función para mover y cambiar el tamaño del lente
def mover_lente(x, y, escala_x, escala_y):
    lente.set_extent([x - escala_x, x + escala_x, y - escala_y, y + escala_y])
    plt.draw()

# Ejemplo de movimiento y cambio de tamaño del lente
mover_lente(5, 5, 2, 1)  # Cambia los valores según tus necesidades

# Mostrar el gráfico
plt.show()
