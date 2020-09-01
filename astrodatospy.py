#!/usr/bin/env python3
# Libreria basica de astrodatos

# Importar librerias
import numpy as np

def dummy():
  pass

def volumen_esfera(R):
  """ Funcion que calcula el volumen de una esfera
  input: Radio R
  output: volumen
  """
  volumen = (4/3)* pi * R**3
  return volumen
