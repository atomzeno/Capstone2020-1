#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[4]:


# Create a Quantum Circuit
n=15
circ = QuantumCircuit(n, 8)
circ.barrier(range(n))
circ.draw()


# In[5]:


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


# In[6]:


def newandplusgate(nqubits):
    #qc = QuantumCircuit(len(nqubits))
    circ.reset(nqubits[2])


# In[8]:


#1th line :
circ.barrier(range(15))
#2th line :
circ.cx(2,8)
circ.cx(3,8)
circ.cx(4,8)
circ.cx(3,9)
circ.cx(4,9)
circ.cx(6,9)
circ.cx(7,9)
circ.cx(4,10)
circ.cx(5,10)
circ.cx(6,10)
circ.cx(7,10)
circ.cx(1,11)
circ.cx(2,11)
circ.cx(3,11)
circ.cx(4,11)
circ.cx(5,11)
circ.cx(6,11)
circ.barrier(range(15))
#3th line :
circ.cx(11,12)
circ.cx(12,11)
circ.cx(10,11)
circ.cx(11,10)
circ.cx(9,10)
circ.cx(10,9)
circ.cx(8,9)
circ.cx(9,8)
circ.barrier(range(15))
#4th line :
circ.cx(5,8)
circ.cx(2,7)
circ.cx(1,6)
circ.cx(3,5)
circ.cx(2,5)
circ.cx(1,5)
circ.barrier(range(15))
#5th line :
circ.cx(12,14)
circ.cx(14,12)
circ.cx(11,13)
circ.cx(13,11)
circ.cx(10,12)
circ.cx(12,10)
circ.cx(9,11)
circ.cx(11,9)
circ.cx(8,10)
circ.cx(10,8)
circ.cx(7,9)
circ.cx(9,7)
circ.cx(6,8)
circ.cx(8,6)
circ.cx(5,7)
circ.cx(7,5)
circ.barrier(range(15))
#6th line :
circ.cx(1,6)
circ.cx(6,1)
circ.cx(2,1)
circ.cx(1,2)
circ.cx(3,2)
circ.cx(2,3)
circ.cx(4,3)
circ.cx(3,4)
circ.barrier(range(15))
#7th line :
circ.cx(3,4)
circ.cx(3,5)
circ.cx(3,6)
circ.barrier(range(15))
#8th line :
newandplusgate([3,7,11])
newandplusgate([4,8,12])
newandplusgate([5,9,13])
newandplusgate([6,10,14])
circ.barrier(range(15))
#9th line :
circ.cx(10,11)
circ.cx(11,10)
circ.cx(9,10)
circ.cx(10,9)
circ.cx(8,9)
circ.cx(9,8)
circ.cx(7,8)
circ.cx(8,7)
circ.barrier(range(15))
#10th line :
circ.cx(3,4)
circ.cx(3,5)
circ.cx(3,6)
circ.barrier(range(15))
#11th line :
circ.cx(3,4)
circ.cx(4,3)
circ.cx(2,3)
circ.cx(3,2)
circ.cx(1,2)
circ.cx(2,1)
circ.cx(6,1)
circ.cx(1,6)
circ.barrier(range(15))
#12th line :
circ.cx(2,10)
circ.cx(1,9)
circ.cx(3,8)
circ.cx(2,8)
circ.cx(1,8)
circ.cx(8,11)
circ.barrier(range(15))
#13th line :
circ.cx(2,5)
circ.cx(3,6)
circ.cx(1,7)
circ.barrier(range(15))
#14th line :
newandplusgate([2,6,8])
newandplusgate([1,3,9])
newandplusgate([7,5,10])
circ.barrier(range(15))
#15th line :
circ.cx(2,5)
circ.cx(3,6)
circ.cx(1,7)
circ.barrier(range(15))


# In[9]:


circ.draw()


# In[ ]:





# In[ ]:





# In[32]:


#check if this works well


# In[45]:


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


# In[46]:


# Create a Quantum Circuit
n=19
circ = QuantumCircuit(n, n)
circ.h(1)
circ.h(2)
circ.h(3)
circ.h(4)
circ.barrier(range(n))
circ.draw()


# In[47]:


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


# In[48]:


def newandplusgate(nqubits):
    #qc = QuantumCircuit(len(nqubits))
    circ.reset(nqubits[2])


# In[49]:


#1th line :
circ.barrier(range(19))
#2th line :
circ.cx(2,5)
circ.cx(3,6)
circ.cx(1,7)
circ.barrier(range(19))
#3th line :
newandgate([2,6,8,11])
newandgate([1,3,9,12])
newandgate([7,5,10,13])
circ.barrier(range(19))
#4th line :
circ.cx(2,5)
circ.cx(3,6)
circ.cx(1,7)
circ.barrier(range(19))
#5th line :
circ.cx(8,11)
circ.cx(1,8)
circ.cx(2,8)
circ.cx(3,8)
circ.cx(1,9)
circ.cx(2,10)
circ.barrier(range(19))
#6th line :
circ.cx(1,6)
circ.cx(6,1)
circ.cx(2,1)
circ.cx(1,2)
circ.cx(3,2)
circ.cx(2,3)
circ.cx(4,3)
circ.cx(3,4)
circ.barrier(range(19))
#7th line :
circ.cx(3,4)
circ.cx(3,5)
circ.cx(3,6)
circ.barrier(range(19))
#8th line :
circ.cx(8,7)
circ.cx(7,8)
circ.cx(9,8)
circ.cx(8,9)
circ.cx(10,9)
circ.cx(9,10)
circ.cx(11,10)
circ.cx(10,11)
circ.barrier(range(19))
#9th line :
newandgate([3,7,11,15])
newandgate([4,8,12,16])
newandgate([5,9,13,17])
newandgate([6,10,14,18])
circ.barrier(range(19))
#10th line :
circ.cx(3,4)
circ.cx(3,5)
circ.cx(3,6)
circ.barrier(range(19))
#11th line :
circ.cx(3,4)
circ.cx(4,3)
circ.cx(2,3)
circ.cx(3,2)
circ.cx(1,2)
circ.cx(2,1)
circ.cx(6,1)
circ.cx(1,6)
circ.barrier(range(19))
#12th line :
circ.cx(7,5)
circ.cx(5,7)
circ.cx(8,6)
circ.cx(6,8)
circ.cx(9,7)
circ.cx(7,9)
circ.cx(10,8)
circ.cx(8,10)
circ.cx(11,9)
circ.cx(9,11)
circ.cx(12,10)
circ.cx(10,12)
circ.cx(13,11)
circ.cx(11,13)
circ.cx(14,12)
circ.cx(12,14)
circ.barrier(range(19))
#13th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(1,6)
circ.cx(2,7)
circ.cx(5,8)
circ.barrier(range(19))
#14th line :
circ.cx(9,8)
circ.cx(8,9)
circ.cx(10,9)
circ.cx(9,10)
circ.cx(11,10)
circ.cx(10,11)
circ.cx(12,11)
circ.cx(11,12)
circ.barrier(range(19))
#15th line :
circ.cx(2,8)
circ.cx(3,8)
circ.cx(4,8)
circ.cx(3,9)
circ.cx(4,9)
circ.cx(6,9)
circ.cx(7,9)
circ.cx(4,10)
circ.cx(5,10)
circ.cx(6,10)
circ.cx(7,10)
circ.cx(1,11)
circ.cx(2,11)
circ.cx(3,11)
circ.cx(4,11)
circ.cx(5,11)
circ.cx(6,11)
circ.barrier(range(19))


# In[50]:


circ.barrier(range(n))


# In[51]:


circ.barrier(range(n))
circ.draw()


# In[52]:


#1th line :
circ.barrier(range(15))
#2th line :
circ.cx(2,8)
circ.cx(3,8)
circ.cx(4,8)
circ.cx(3,9)
circ.cx(4,9)
circ.cx(6,9)
circ.cx(7,9)
circ.cx(4,10)
circ.cx(5,10)
circ.cx(6,10)
circ.cx(7,10)
circ.cx(1,11)
circ.cx(2,11)
circ.cx(3,11)
circ.cx(4,11)
circ.cx(5,11)
circ.cx(6,11)
circ.barrier(range(15))
#3th line :
circ.cx(11,12)
circ.cx(12,11)
circ.cx(10,11)
circ.cx(11,10)
circ.cx(9,10)
circ.cx(10,9)
circ.cx(8,9)
circ.cx(9,8)
circ.barrier(range(15))
#4th line :
circ.cx(5,8)
circ.cx(2,7)
circ.cx(1,6)
circ.cx(3,5)
circ.cx(2,5)
circ.cx(1,5)
circ.barrier(range(15))
#5th line :
circ.cx(12,14)
circ.cx(14,12)
circ.cx(11,13)
circ.cx(13,11)
circ.cx(10,12)
circ.cx(12,10)
circ.cx(9,11)
circ.cx(11,9)
circ.cx(8,10)
circ.cx(10,8)
circ.cx(7,9)
circ.cx(9,7)
circ.cx(6,8)
circ.cx(8,6)
circ.cx(5,7)
circ.cx(7,5)
circ.barrier(range(15))
#6th line :
circ.cx(1,6)
circ.cx(6,1)
circ.cx(2,1)
circ.cx(1,2)
circ.cx(3,2)
circ.cx(2,3)
circ.cx(4,3)
circ.cx(3,4)
circ.barrier(range(15))
#7th line :
circ.cx(3,4)
circ.cx(3,5)
circ.cx(3,6)
circ.barrier(range(15))
#8th line :
newandplusgate([3,7,11])
newandplusgate([4,8,12])
newandplusgate([5,9,13])
newandplusgate([6,10,14])
circ.barrier(range(15))
#9th line :
circ.cx(10,11)
circ.cx(11,10)
circ.cx(9,10)
circ.cx(10,9)
circ.cx(8,9)
circ.cx(9,8)
circ.cx(7,8)
circ.cx(8,7)
circ.barrier(range(15))
#10th line :
circ.cx(3,4)
circ.cx(3,5)
circ.cx(3,6)
circ.barrier(range(15))
#11th line :
circ.cx(3,4)
circ.cx(4,3)
circ.cx(2,3)
circ.cx(3,2)
circ.cx(1,2)
circ.cx(2,1)
circ.cx(6,1)
circ.cx(1,6)
circ.barrier(range(15))
#12th line :
circ.cx(2,10)
circ.cx(1,9)
circ.cx(3,8)
circ.cx(2,8)
circ.cx(1,8)
circ.cx(8,11)
circ.barrier(range(15))
#13th line :
circ.cx(2,5)
circ.cx(3,6)
circ.cx(1,7)
circ.barrier(range(15))
#14th line :
newandplusgate([2,6,8])
newandplusgate([1,3,9])
newandplusgate([7,5,10])
circ.barrier(range(15))
#15th line :
circ.cx(2,5)
circ.cx(3,6)
circ.cx(1,7)
circ.barrier(range(15))


# In[53]:


circ.draw()


# In[54]:


for i in range(19):
    circ.measure(i, 18-i)


# In[55]:


# Use Aer's qasm_simulator
backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = execute(circ, backend_sim, shots=1024)

# Grab the results from the job.
result_sim = job_sim.result()


# In[56]:


counts = result_sim.get_counts(circ)
print(counts)


# In[57]:


from qiskit.visualization import plot_histogram
plot_histogram(counts)


# In[ ]:




