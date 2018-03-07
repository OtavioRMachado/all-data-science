# -*- coding: UTF-8 -*-
import numpy as np

# Gera 15 valores no formato [3][5].
a = np.arange(15).reshape(3, 5)

# Mostra as dimensões do array
print a.shape

# Mostra o número de dimensões
print a.ndim

# Mostra o tipo dos elementos
print a.dtype.name

# Mostra o número de elementos. É o mesmo que o produto de a.shape.
print a.size

# Mostra o tamanho ocupado por cada elemento do array
print a.itemsize

# Mostra o tipo do array
type(a)

