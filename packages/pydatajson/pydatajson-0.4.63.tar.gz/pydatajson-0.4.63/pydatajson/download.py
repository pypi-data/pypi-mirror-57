# -*- coding: utf-8 -*-

"""Módulo 'download' de pydatajson

Contiene métodos para descargar archivos a través del protocolo HTTP.
"""

from __future__ import unicode_literals, print_function, with_statement
from __future__ import absolute_import

import requests
import time
import sys

DEFAULT_TRIES = 3
RETRY_DELAY = 1


def download(url, tries=DEFAULT_TRIES, retry_delay=RETRY_DELAY):
    """
    Descarga un archivo a través del protocolo HTTP, en uno o más intentos.

    Args:
        url (str): URL (schema HTTP) del archivo a descargar.
        tries (int): Intentos a realizar (default: 3).
        retry_delay (int o float): Tiempo a esperar, en segundos, entre cada
            intento.
        try_timeout (int o float): Tiempo máximo a esperar por intento.
        proxies (dict): Proxies a utilizar. El diccionario debe contener los
            valores 'http' y 'https', cada uno asociados a la URL del proxy
            correspondiente.

    Returns:
        bytes: Contenido del archivo
    """
    timeout = 2
    for i in range(1, tries + 1):
        try:
            return requests.get(url, timeout=timeout ** i,
                                verify=False).content
        except requests.TooManyRedirects as e:
            raise e
        except Exception as e:
            download_exception = e
    raise download_exception


def download_to_file(url, file_path, **kwargs):
    """
    Descarga un archivo a través del protocolo HTTP, en uno o más intentos, y
    escribe el contenido descargado el el path especificado.

    Args:
        url (str): URL (schema HTTP) del archivo a descargar.
        file_path (str): Path del archivo a escribir. Si un archivo ya existe
            en el path especificado, se sobrescribirá con nuevos contenidos.
        kwargs: Parámetros para download().
    """
    content = download(url, **kwargs)
    with open(file_path, "wb") as f:
        f.write(content)


if __name__ == '__main__':
    download_to_file(sys.argv[1], sys.argv[2])
