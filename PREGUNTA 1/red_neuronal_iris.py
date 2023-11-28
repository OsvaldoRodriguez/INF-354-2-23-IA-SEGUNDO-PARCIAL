# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:23:27 2023
@author: Fury
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data
nroinputs = len(x)
inputs = np.random.randn(nroinputs, 5)
for i in range(len(x)):
  for j in range(len(x[i])):
    x[i,j] = x[i,j]

y2 = iris.target

inputs = np.array(inputs)
y = []
for x in y2:
  vec = [x]
  y.append(vec)
y = np.array(y)



class NeuralNet():
  def __init__(self, input_size, hidden_size, output_size):
    self.input_size = input_size
    self.hidden_size = hidden_size
    self.output_size = output_size

    self.W1 = np.random.randn(self.input_size, self.hidden_size) #crea un array de N x M elementos con valores aleatorios
    self.W2 = np.random.randn(self.hidden_size, self.output_size)
  
  def sigmoid(self, x):
    return 1 / (1 + (np.exp(-x)))

  def sigmoid_der (self, x):
    return x * (1 - x)

  def mse (self, output, target): #es una funcion para que ayude a representar graficamente
    return np.mean((output - target) ** 2) / 2

  def forward (self, X):
    self.z1 = np.dot(X, self.W1) #producto de la ENTRADA por la CAPA OCULTA
    self.a1 = self.sigmoid(self.z1) # funcion de activacion 

    self.z2 = np.dot(self.a1, self.W2) # producto de la CAPA OCULTA por la SALIDA
    self.output = self.sigmoid(self.z2) # funcion de activacion 
    return self.output

  def backpropagation(self, X, y, lr): #inputs, objetivo, taza de aprendizaje
    output = self.forward(X)

    error_output = output - y
    delta_out = error_output * self.sigmoid_der(output)
    derivative_W2 = np.dot(self.a1.T, delta_out)
    
    error_hidden = np.dot(delta_out, self.W2.T)
    delta_hidden = error_hidden * self.sigmoid_der(self.a1)
    derivative_W1 = np.dot(inputs.T, delta_hidden)

    #Descenso del gradiente
    self.W2 -= derivative_W2 * lr
    self.W1 -= derivative_W1 * lr
    
    return self.mse(output,y)
     


nn = NeuralNet(5,5,1)

print("antes: ")
print(nn.forward(inputs))
errors = []
error = 1
ephocs = 10001
for i in range(ephocs):
  error = nn.backpropagation(inputs, y, 0.7)
  errors.append(error)
  
print("Despues:")
print(nn.forward(inputs))

x_axis = range(0, len(errors))
plt.plot(x_axis, errors)
plt.show()