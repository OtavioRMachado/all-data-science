# Numpy.

## É de comer?
Infelizmente, ainda não.

O Numpy é uma biblioteca de Python que serve para lidar com arrays multidimensionais/matrizes, já que o array nativo da linguagem aceita apenas os unidimensionais.

Ou seja, se você quer criar uma matriz, já não pode fazer com o array tradicional de Python.

Além disso, ele traz diversas funções prontas que trazem informações úteis dessa matriz, que serão abordadas mais abaixo.

## Muito bom. Como eu utilizo issaê?
Primeiro, [instale](https://scipy.org/install.html).

Depois, você pode utilizar o numpy importando a biblioteca no seu código:

`import numpy`

### Criando Arrays ([doc](https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html))

#### 1. Com valores já definidos:
Para criar um array com valores já definidos, você pode utilizar o seguinte:

`numpy.array([[1,2], [3,4]])`

Você ainda pode definir valores como **número mínimo de dimensões**, **tipo dos valores do array**, etc.

`numpy.array([1], ndmin=2)`

#### 2. Vazio

Você pode preencher seu array com zeros, uns ou deixar não-inicializado, contendo lixo. 

`numpy.zeros((3,4))` || `numpy.ones((2, 1, 3))` || `np.empty((2,3))`

### 3. Com uma sequência de números

Você pode criar um array cujos elementos obedecem uma regra de sequência da seguinte forma:

`numpy.arange(10, 30, 5)`, onde:

10 é o valor inicial

30 é o valor final

5 é o passo





