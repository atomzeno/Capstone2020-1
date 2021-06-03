#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit import *
#import numpy as np
# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()

get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


# Create a Quantum Circuit
n=21
circ = QuantumCircuit(n, n)
circ.barrier(range(n))
circ.draw()


# In[11]:


def newandgate(nqubits):
    #qc = QuantumCircuit(len(nqubits))
    circ.h(nqubits[2])
    circ.cx(nqubits[1], nqubits[3])
    circ.cx(nqubits[2], nqubits[0])
    circ.cx(nqubits[2], nqubits[1])
    circ.cx(nqubits[0], nqubits[3])
    circ.tdg(nqubits[0])
    circ.tdg(nqubits[1])
    circ.t(nqubits[2])
    circ.t(nqubits[3])
    circ.cx(nqubits[0], nqubits[3])
    circ.cx(nqubits[2], nqubits[1])
    circ.cx(nqubits[2], nqubits[0])
    circ.cx(nqubits[1], nqubits[3])
    circ.h(nqubits[2])
    circ.s(nqubits[2])
    #circ.barrier(range(n))
    #qc.draw()
    #U_s = qc.to_gate()
    #U_s.name = "AND4gate"
    #return U_s


# In[12]:


def newandplusgate(nqubits):
    #qc = QuantumCircuit(len(nqubits))
    circ.reset(nqubits[2])


# In[13]:


#1th line :
circ.barrier(range(21))
#2th line :
circ.cx(2,15)
circ.cx(2,16)
circ.cx(3,13)
circ.cx(4,14)
circ.barrier(range(21))
#3th line :
newandgate([1,16,8,17])
newandgate([2,13,5,18])
newandgate([3,14,6,19])
newandgate([4,15,7,20])
circ.barrier(range(21))
#4th line :
circ.cx(2,15)
circ.cx(2,16)
circ.cx(3,13)
circ.cx(4,14)
circ.barrier(range(21))
#5th line :
circ.cx(2,9)
circ.cx(3,9)
circ.cx(4,9)
circ.cx(3,10)
circ.cx(4,10)
circ.cx(4,11)
circ.cx(8,11)
circ.cx(1,12)
circ.cx(2,12)
circ.cx(3,12)
circ.cx(4,12)
circ.barrier(range(21))
#6th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(21))
#7th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(21))
#8th line :
circ.cx(1,2)
circ.barrier(range(21))
#9th line :
newandplusgate([4,5,9])
newandplusgate([1,6,10])
newandplusgate([2,7,11])
newandplusgate([3,8,12])
circ.barrier(range(21))
#10th line :
circ.cx(1,2)
circ.barrier(range(21))
#11th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(21))
#12th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(21))
#13th line :
circ.cx(5,9)
circ.cx(9,5)
circ.cx(6,10)
circ.cx(10,6)
circ.cx(7,11)
circ.cx(11,7)
circ.cx(8,12)
circ.cx(12,8)
circ.barrier(range(21))
#14th line :
circ.cx(1,7)
circ.cx(7,1)
circ.cx(2,8)
circ.cx(8,2)
circ.barrier(range(21))
#15th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(21))
#16th line :
newandplusgate([1,2,9])
newandplusgate([3,4,10])
newandplusgate([5,6,11])
newandplusgate([7,8,12])
circ.barrier(range(21))
#17th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(21))
#18th line :
circ.cx(7,1)
circ.cx(1,7)
circ.cx(8,2)
circ.cx(2,8)
circ.barrier(range(21))
#19th line :
circ.barrier(range(21))


# In[14]:


circ.draw()


# In[ ]:




