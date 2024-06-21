import os
import time

from os.path import join, dirname
from dotenv import load_dotenv
from oracledb import connect, create_pool


# Loading environment variables from `.env` file.
load_dotenv(join(dirname(__file__), '.env'))


# Define environment variables
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_TNS_SERVICE_NAME = os.environ.get("DB_TNS_SERVICE_NAME")


def measure_run_time(func):
    """
    The `measure_run_time` function is a Python decorator that measures the execution time of a given
    function.
    
    :param func: The `func` parameter in the `measure_run_time` function is a function that you want to
    measure the execution time of. The `measure_run_time` function is a decorator that calculates the
    time taken for the provided function to execute and prints out the duration in seconds after the
    function has completed its
    :return: The `measure_run_time` function is returning the `wrap` function, which is a wrapper
    function that measures the execution time of the input function `func`.
    """
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'\n\n>>> La función {func.__name__} tardó {end_time - start_time} segundos en ejecución')
        return result
    return wrap


@measure_run_time
def exec_simple_connection():
    """
    The function `exec_simple_connection` establishes a connection to a database, executes a query to
    select all rows from a table named BRPS, and prints the results.
    """
    print("\n\n>>> Ejecutando simple connection", end="\n\n")
    
    connection = connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_TNS_SERVICE_NAME)
    with connection.cursor() as cursor:
        for row in cursor.execute("SELECT * FROM BRPS"):
            print(row)

    connection.close()


@measure_run_time
def exec_pool_connection():
    """
    The function `exec_pool_connection` creates a connection pool, acquires a connection from the pool,
    executes a query, and prints the results.
    """
    print("\n\n>>> Ejecutando pool connection", end="\n\n")
    
    pool = create_pool(user=DB_USER, password=DB_PASSWORD, dsn=DB_TNS_SERVICE_NAME, min=1, max=5, increment=1)
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            for result in cursor.execute("SELECT * FROM BRPS"):
                print(result)

    pool.close()


if __name__ == '__main__':
    option = input("Ingrese '1' para pool connection, o cualquier otra tecla para usar simple connection: ")

    if option == '1':
        exec_simple_connection()
    else:
        exec_pool_connection()
