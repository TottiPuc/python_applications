# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:37:55 2019

@author: dayan
"""

class DistProbab:
    """Distribucion discreta de probabilidad
    Varname = variable aleatoria de entrada 
    freqs = pares de frecuencias pasados como diccionarios """
    
    def __init__(self, varname='?', freqs=None):
    	""" la Distribución de probabilidad será normalizada si freqs son pasados como parametros """
    	self.prob = {}
    	self.varname = varname
    	self.values = []
    	if freqs:
    		for (v,p) in freqs.items():
    			self[v] = p
    			self.normalize()

    def normalize(self):
    	""" Caso las frecuencias seas pasadas como argumento se normalizan y se verifica si la suma total es 1 """
    	total = sum(self.prob.values())
    	if not isclose(total,1.0):
    		for val in self.prob:
    			self.prob[val]/= total
    	return self



        
    