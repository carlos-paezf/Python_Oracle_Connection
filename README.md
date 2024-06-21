# Proyecto de Conexión a Oracle con Python

Este proyecto demuestra cómo establecer una conexión simple y una conexión de pool a una base de datos Oracle utilizando Python. Utiliza las variables de entorno para manejar las credenciales de forma segura y proporciona una funcionalidad para medir el tiempo de ejecución de las funciones de conexión.

## Instalación

Asegúrate de tener Python instalado en tu sistema. Luego, instala las dependencias necesarias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo .env en el directorio raíz del proyecto con las siguientes variables de entorno:

```txt
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_TNS_SERVICE_NAME=tu_servicio_tns
```

Estas variables se utilizarán para configurar la conexión a la base de datos Oracle.

## Uso

Para ejecutar una conexión simple, simplemente ejecuta el script principal:

```bash
python main.py
```

Si prefieres utilizar una conexión de pool, ingresa `1` cuando se te solicite.

## Funciones de Conexión

`exec_simple_connection`: Establece una conexión simple a la base de datos y ejecuta una consulta.

`exec_pool_connection`: Crea un pool de conexiones y adquiere una conexión para ejecutar una consulta.

*¿Cuál es la diferencia entre usar cada forma de conexión?:*

1. **Gestión de Recursos**:

    *Simple Connection*: Cada vez que se llama a exec_simple_connection, se establece una nueva conexión con la base de datos. Esto significa que se inicia y se cierra una conexión individual para cada operación, lo cual puede ser costoso en términos de recursos y tiempo si se realiza con frecuencia.

    *Pool Connection*: Al utilizar exec_pool_connection, se crea un conjunto (pool) de conexiones que se pueden reutilizar. Esto reduce la sobrecarga de establecer y cerrar conexiones, especialmente en aplicaciones con muchas operaciones de base de datos.

2. **Rendimiento**:

    *Simple Connection*: Puede ser más lenta si se necesita abrir y cerrar conexiones repetidamente, ya que cada nueva conexión requiere tiempo para establecerse.

    *Pool Connection*: Mejora el rendimiento al tener conexiones preestablecidas listas para ser utilizadas, lo que acelera el proceso de conexión cuando se necesita realizar una operación en la base de datos.

3. **Escalabilidad**:

    *Simple Connection*: No es ideal para aplicaciones que escalan o que tienen un alto volumen de transacciones, ya que cada transacción requiere una nueva conexión.

    *Pool Connection*: Es más escalable, ya que el pool maneja múltiples conexiones que pueden servir a un mayor número de solicitudes simultáneas.

4. **Confiabilidad**:

    *Simple Connection*: Si la conexión falla, se debe establecer una nueva, lo que puede llevar a una falla si el sistema de base de datos está sobrecargado o no disponible.

    *Pool Connection*: El pool puede proporcionar una conexión alternativa si una falla, lo que aumenta la confiabilidad de las operaciones de la base de datos.

5. **Configuración**:

    *Simple Connection*: Generalmente requiere menos configuración y es más directa, ideal para scripts o aplicaciones simples.

    *Pool Connection*: Requiere configuración adicional, como el número mínimo y máximo de conexiones en el pool, y es más adecuada para aplicaciones complejas o de nivel empresarial.

En resumen, la elección entre una conexión simple y una conexión de pool depende de las necesidades específicas de la aplicación. Si necesitas manejar un alto volumen de transacciones o requieres un rendimiento óptimo y escalabilidad, una conexión de pool es generalmente la mejor opción. Para tareas más simples y menos frecuentes, una conexión simple puede ser suficiente.

## Decorador measure_run_time

El decorador `measure_run_time` se utiliza para medir el tiempo de ejecución de las funciones de conexión. Se aplica a las funciones `exec_simple_connection` y `exec_pool_connection`.
