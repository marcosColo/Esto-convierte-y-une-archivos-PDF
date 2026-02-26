La app tiene dos funciones principales que son convertir archivos de texto en varios formatos a formato PDF, la segunda funcion es tomar varios archivos PDF y unirlos en uno solo

Uso dos bibliotecas que son:
  - PuMuPDF: https://github.com/pymupdf/PyMuPDF
      Es la biblioteca principal sobre la que esta formada el proyecto. por ahora uso la funcion de convertir texto e imagenes a PDF
      pero la biblioteca tiene muchas funciones que implementare con el tiempol
    
  - PyPDF: https://github.com/py-pdf/pypdf
      En menor medida uso esta biblioteca. Por ahora solo uso la funcion de unir PDF pero tambien tiene muchas funcionalides para editar estos archivos

Con el tiempo ire agregando las siguientes funcionalidades:
  - Poder navegar entre los ficheros del equipo ya que ahora si o si los archivos a convertir o unir tienen que estar en el escritorio
  - Interfaz grafica
  - Poder convertir imagenes a PDF, por ahora solo convierte texto
  - Convertir varios archivos de imagenes y texto y unirlos con una sola accion del usuario.
      Actualmente los conversores tienen un limite de archivos a convertir por dia de forma gratuita. Mi idea es crear la aplicacion y que sea instalada y usada de forma local
      asi evito el gasto de mantener un servidor, gracias a esto la aplicacion puede entregarse gratis y sin limites para las personas que la necesiten
