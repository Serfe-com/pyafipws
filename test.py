#!/usr/bin/python3
import sys
import os
from .wsaa import WSAA
from .wsfev1 import WSFEv1

# --- Configuración de AFIP ---
CUIT = 30718185676
SERVICE = "wsfe"
WSDL_FE = "https://servicios1.afip.gov.ar/wsfev1/service.asmx?WSDL"

CERT = "/home/geronimo/afip.crt"      # tu .crt
PRIVATEKEY = "/home/geronimo/afip.key"      # tu .key
CACERT = "/home/geronimo/projects/pyafipws/conf/afip_ca_info.crt"      # raíz AFIP
CACHE = "/tmp/pyafipws_cache"            # carpeta temporal para WSAA

# --- Conectarse a WSFEv1 ---
wsfe = WSFEv1()
wsfe.Cuit = CUIT
wsfe.Token = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8c3NvIHZlcnNpb249IjIuMCI+CiAgICA8aWQgc3JjPSJDTj13c2FhLCBPPUFGSVAsIEM9QVIsIFNFUklBTE5VTUJFUj1DVUlUIDMzNjkzNDUwMjM5IiBkc3Q9IkNOPXdzZmUsIE89QUZJUCwgQz1BUiIgdW5pcXVlX2lkPSIyNzk0MjUzOTM3IiBnZW5fdGltZT0iMTc3MjYzMzEzMSIgZXhwX3RpbWU9IjE3NzI2NzYzOTEiLz4KICAgIDxvcGVyYXRpb24gdHlwZT0ibG9naW4iIHZhbHVlPSJncmFudGVkIj4KICAgICAgICA8bG9naW4gZW50aXR5PSIzMzY5MzQ1MDIzOSIgc2VydmljZT0id3NmZSIgdWlkPSJTRVJJQUxOVU1CRVI9Q1VJVCAzMDcxODE4NTY3NiwgQ049b2Rvb19mYWN0dXJhY2lvzIFuX2NvcnJldGFqZS5hciIgYXV0aG1ldGhvZD0iY21zIiByZWdtZXRob2Q9IjIyIj4KICAgICAgICAgICAgPHJlbGF0aW9ucz4KICAgICAgICAgICAgICAgIDxyZWxhdGlvbiBrZXk9IjMwNzE4MTg1Njc2IiByZWx0eXBlPSI0Ii8+CiAgICAgICAgICAgIDwvcmVsYXRpb25zPgogICAgICAgIDwvbG9naW4+CiAgICA8L29wZXJhdGlvbj4KPC9zc28+Cg=="
wsfe.Sign = "mnbpiNB7J6synA6kmOUPyGqZqRYlU0D1Wic7jCMh/aiEHu5lnSqi8OXN6yXwgnZX8aeBaHayEAeJOnB3NfDzPtBKtjR5zc6vRBB4xNDm/SBGBwurLzGTo/0pCrx/FynP3AMEGQPnlFthLS6+kEe09yGjPEPEYEMQIlcfH84NnJY="
wsfe.Conectar(CACHE, WSDL_FE)

# --- Probar ParamGetCotizacion ---
codigo_moneda = "DOL"  # Dólar oficial, por ejemplo
try:
    res = wsfe.ParamGetCotizacion(codigo_moneda)
    print("Respuesta de cotización:", res)
except KeyError as e:
    print("KeyError capturado:", e)
    print("Última request:\n", wsfe.LastRequest)
    print("Última response:\n", wsfe.LastResponse)
except Exception as e:
    print("Error inesperado:", e)