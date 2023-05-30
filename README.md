------------

<h1 align="center"> Sistema de lentes delgadas convergente y divergente.</h1>

------------
<p align="center">
  <img src="https://github.com/Juanpaz0411/Proyecto_final/blob/master/imagenes%20readme/portada.jpeg.jpeg" alt="portada" width="600" />
  <br>
</p>

#####  *Proyecto final de programación*
#####  *Juan jose paz hormiga*
##### *Universidad del Quindio*
##### *Programa de física*
##### *2023*

Este codigo gráfica un sistema de lentes ya sea convergente o divergente y ubica en el dos vectores, uno correspondiente a el objeto y otro correspondiente a la imagen, cada vector representa la dirección y el tamaño.

Lo que hace el codigo para cada caso se muestra en las siguientes imagenes:


<div align="center">
  <div style="display: inline-block; text-align: center;">
    <img src="https://github.com/Juanpaz0411/Proyecto_final/blob/master/imagenes%20readme/convergente.jpeg.jpeg" alt="Sistema de lente convergente" width="250" />
    <p><em>Sistema de lente convergente.</em></p>
  </div>
  <div style="display: inline-block; text-align: center;">
    <img src="https://github.com/Juanpaz0411/Proyecto_final/blob/master/imagenes%20readme/divergente.jpeg.jpeg" alt="Sistema de lente divergente." width="250" />
    <p><em>Sistema de lente divergente.</em></p>
  </div>
</div>

La forma de ejecutar este programa es a través de la función valor_faltante,  función la cual permite al usuario ingresar los valores de el lente y los guarda en un diccionario  el cual sera pasado como argumento a alguna de las clases.

Porteriormente dependiendo si el foco es negativo o positivo se ejecuta la siguiente sección de codigo la cual ejecuta la clase lente convergente o lente divergente de forma respectiva: 

	diccionario = valor_faltante()
	lente = LenteConvergente(**diccionario) if diccionario['f'] > 0 else LenteDivergente(**diccionario)
	if len(diccionario) == 3:
		lente.calcular_faltante()
	elif len(diccionario) == 4:
		lente.magnificacion(diccionario)
	else:
		print('error, se necesitan minimo dos 3 datos para la ejecucion del programa')
Cabe resaltar que en esa misma sección de codigo se ejecuta la función 'calcular_faltante()' si falta un dato de los cuatro datos necesarios para gráficar, de estar completos se ejecuta directamente 'magnificacion()' para calcular la altura de la imagen y la magnificación de el lente, a partir de aqui el resto de las funciones se ejecutan solas a través de llamadas en las funciones que le preceden. En caso de que los datos de el diccionario sean menores a 3 no se sigue ejecutando el codigo y se imprime una alerta de error.

El codigo consta de tres clases, una clase padre 'lentes' la cual tiene un constructor que hace que el argumento de los objetos de la clase sean diccionarios y unas funciones las cuales fueron importadas en las clases hijas 'lente_convergente' y 'lente_divergente', cada clase recibe como argumento un diccionario con los datos del lente: distancia focal, distancia del objeto, distancia de la imagen, altura de la imagen. En este diccionario es posible no ingresar uno de los primeros tres datos haciendo que la clase correspondiente calcule el valor faltante guardando los datos completos en un nuevo diccionario el cual se usara como argumento para poder graficar. 

Inicialmente se planeaba programar una cuarta clase 'par_de_lentes' la cual haria los calculos correspondientes y graficara todo lo asociado al sistema de lentes, por cuestion de tiempo no se termino.

<p align="center">
  <img src="https://github.com/Juanpaz0411/Proyecto_final/blob/master/imagenes%20readme/dos_lentes.jpeg.jpeg" alt="Dos lentesn" width="400" />.
  <br>
  <em>Sistema compuesto de dos lentes.</em>
</p>

Hay dos diferencias entre las clases 'lente_convergente' y 'lente_divergente', la primera radica en la imagen que simula el lente y la segunda radica en la fución rayo_emergente, en el caso de la funcion rayo emergente de el lente divergente la pendiente del rayo verde cambia debido a que se cabia el punto a través del cual se calcula.


Se uso el decorador 'show_function_name' para saber que funcion se está ejecutando.

	def show_function_name(func):
		'''
		Este es un decorador que dice que funcion se esta ejecutando.
		'''
		def wrapper(*args, **kwargs):
			print(f"Se está utilizando la función: {func.__name__}")
			return func(*args, **kwargs)
		return wrapper

