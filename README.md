
# Intro
Una aplicación web que sirva para conocer todas las actividades culturales de la ciudad de Córdoba (y alrededores). Tiene que poder navegarse y buscarse fácilmente entre todo tipo de eventos culturales (teatro, recitales, exposiciones, muestras, etc), excluyendo el cine ya que existen buenas herramientas de búsqueda en cada una de las salas.

En el futuro, puede convertirse en un proyecto rentable a partir de la venta de publicidad.

## Potenciales usuarios (target)
Personas que asisten a eventos culturales en la ciudad de Córdoba, que utilizan frecuentemente internet. Principalmente jóvenes, desde el colegio secundario.

El foco se estima en gente de 18 a 40 años, de clase media/alta.
También accesible a mayores de 40 años que utilicen frecuentemente internet o email.

¿Quienes pueden estar interesados en el proyecto de forma tal que colaborarían con el contenido? ¿quién se puede beneficiar con el funcionamiento de la herramienta (más allá de los usuarios)?

1. Centros culturales
2. Establecimientos donde se desarrollen eventos culturales (boliches, clubes, salas, anfiteatros, etc.)
3. Productores culturales
4. Artistas, bandas de música, grupos de teatro
5. Críticos o escritores especializados en temas culturales

# Desarrollo

agendacultural_com_ar es el primer prototipo, usado como tutorial practicamente, para aprender Django. Este directorio va a ser borrado, pero todavía tiene cosas
que pueden ser útiles.

## Arquitectura general

### Backend

Projecto Django que provea una API REST (mediante DRF).

### Frontend

SPA (_single page app_) basada en https://github.com/ajaxray/marionette-boilerplate


### Data

La idea es generar gran parte de los datos mediante el _scrapping_ de páginas existentes (diarios, etc). Para esto usaría Scrapy

Los datos _escrapeados_ entrarían a una fase de revisión, donde manualmente se pueden modificar y publicar.

Se puede definir una métrica de _confianza_ sobre un dato escrapeado para, eventualmente, publicarlo directamente.


## Wish list

Las funciones que debería tener el sistema son:
 - Listados: de eventos, lugares, artistas, etc. Con filtros configurables (cronológicos, geográficos, por tags, etc).
 - Calendario: un calendario donde se reflejen cronológicamente los eventos. Se puede configurar para ver un año, mes, semana, día o período particular. Con una típica vista de calendario. Debe proveer capacidades de exportación (para integrarlo en GCal, otras aplicaciones de calendario, bajarlo a un excel, etc).
 - Búsqueda general: se ingresa un término y se devuelven todas las entidades que lo poseen.
 - Próximos eventos: lo más próximo a realizarse
 - Eventos destacados: por algún motivo.
 - Búsqueda por proximidad: buscar los eventos ordenados por cercanía a un punto geográfico.
 - Subscripción: alguien solicita registrarse. Puede solicitar acceso como productor (o algo así) lo que le permite cargar datos (lugares, artistas, eventos, etc). Alguien de staff además de ser productor, puede cambiar el estado de las entidades (o sea publicar, cancelar, etc.). Finalmente los administradores pueden hacer todo lo posible.
 - Administración: los usuarios productores tienen una interfaz especial para la administración (ABM) de entidades: o sea que cada entidad puede crearse, modificarse, copiarse, etc.
 - Newsletter semanal: con los próximos eventos de la semana, enviado automáticamente, a los usuarios que se hayan suscripto.
 - Recordatorios: Un usuario puede suscribirse para recibir recordatorios o alarmas, relacionados con eventos, lugares (cada vez que se carga un evento para ese lugar), artistas (cada vez que el artista protagoniza algún evento), etc.
 - Integración con FB: un usr puede registrarse con su cuenta de FB y recibe notificaciones.
 - Carga automática de datos: que se cargen eventos automáticamente a partir de otros sitios conocidos, actualizados (por ej de la página de La Voz, Cocina de Culturas, La fábrica, etc). Esto incluye una etapa de revisión manual, donde un usuario autorizado controla los datos obtenidos, elimina duplicados, completa información, etc y finalmente publica.
 - App para el celu.
