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


# In[3]:


# Create a Quantum Circuit
n=17
circ = QuantumCircuit(17, 8)
circ.h(1)
circ.h(2)
circ.h(3)
circ.h(4)
circ.barrier(range(n))
circ.draw()


# In[4]:


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


# In[5]:


def newandplusgate(nqubits):
    #qc = QuantumCircuit(len(nqubits))
    circ.reset(nqubits[2])


# In[6]:


#1th line :
circ.barrier(range(17))
#2th line :
circ.cx(1,7)
circ.cx(7,1)
circ.cx(2,8)
circ.cx(8,2)
circ.barrier(range(17))
#3th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(17))
#4th line :
newandgate([1,2,9,13])
newandgate([3,4,10,14])
newandgate([5,6,11,15])
newandgate([7,8,12,16])
circ.barrier(range(17))
#5th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(17))
#6th line :
circ.cx(7,1)
circ.cx(1,7)
circ.cx(8,2)
circ.cx(2,8)
circ.barrier(range(17))
#7th line :
circ.cx(9,5)
circ.cx(5,9)
circ.cx(10,6)
circ.cx(6,10)
circ.cx(11,7)
circ.cx(7,11)
circ.cx(12,8)
circ.cx(8,12)
circ.barrier(range(17))
#8th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(17))
#9th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(17))
#10th line :
circ.cx(1,2)
circ.barrier(range(17))
#11th line :
newandgate([4,5,9,13])
newandgate([1,6,10,14])
newandgate([2,7,11,15])
newandgate([3,8,12,16])
circ.barrier(range(17))
#12th line :
circ.cx(1,2)
circ.barrier(range(17))
#13th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(17))
#14th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(17))
#15th line :
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
circ.barrier(range(17))
#16th line :
circ.barrier(range(17))


# In[7]:


circ.barrier(range(14))
# map the quantum measurement to the classical bits
#circ.measure(range(14), range(14))
circ.measure(4, 7)
circ.measure(3, 6)
circ.measure(2, 5)
circ.measure(1, 4)
circ.measure(9, 3)
circ.measure(10,2)
circ.measure(11,1)
circ.measure(12,0)
# The Qiskit circuit object supports composition using
# the addition operator.
#drawing the circuit


# In[8]:


circ.draw()


# In[9]:


# Use Aer's qasm_simulator
backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = execute(circ, backend_sim, shots=1024)

# Grab the results from the job.
result_sim = job_sim.result()
counts = result_sim.get_counts(circ)
print(counts)


# In[10]:


from qiskit.visualization import plot_histogram
plot_histogram(counts)


# In[ ]:





# In[11]:


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


# In[12]:


# Create a Quantum Circuit
n=17
circ = QuantumCircuit(17, 17)
circ.h(1)
circ.h(2)
circ.h(3)
circ.h(4)
circ.barrier(range(n))
circ.draw()


# In[13]:


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


# In[14]:


def newandplusgate(nqubits):
    #qc = QuantumCircuit(len(nqubits))
    circ.reset(nqubits[2])


# In[15]:


#1th line :
circ.barrier(range(17))
#2th line :
circ.cx(1,7)
circ.cx(7,1)
circ.cx(2,8)
circ.cx(8,2)
circ.barrier(range(17))
#3th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(17))
#4th line :
newandgate([1,2,9,13])
newandgate([3,4,10,14])
newandgate([5,6,11,15])
newandgate([7,8,12,16])
circ.barrier(range(17))
#5th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(17))
#6th line :
circ.cx(7,1)
circ.cx(1,7)
circ.cx(8,2)
circ.cx(2,8)
circ.barrier(range(17))
#7th line :
circ.cx(9,5)
circ.cx(5,9)
circ.cx(10,6)
circ.cx(6,10)
circ.cx(11,7)
circ.cx(7,11)
circ.cx(12,8)
circ.cx(8,12)
circ.barrier(range(17))
#8th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(17))
#9th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(17))
#10th line :
circ.cx(1,2)
circ.barrier(range(17))
#11th line :
newandgate([4,5,9,13])
newandgate([1,6,10,14])
newandgate([2,7,11,15])
newandgate([3,8,12,16])
circ.barrier(range(17))
#12th line :
circ.cx(1,2)
circ.barrier(range(17))
#13th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(17))
#14th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(17))
#15th line :
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
circ.barrier(range(17))
#16th line :
circ.barrier(range(17))


# In[16]:


circ.barrier(range(14))


# In[17]:


#1th line :
circ.barrier(range(13))
#2th line :
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
circ.barrier(range(13))
#3th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(13))
#4th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(13))
#5th line :
circ.cx(1,2)
circ.barrier(range(13))
#6th line :
newandplusgate([4,5,9])
newandplusgate([1,6,10])
newandplusgate([2,7,11])
newandplusgate([3,8,12])
circ.barrier(range(13))
#7th line :
circ.cx(1,2)
circ.barrier(range(13))
#8th line :
circ.cx(1,5)
circ.cx(2,5)
circ.cx(3,5)
circ.cx(2,6)
circ.cx(3,6)
circ.cx(4,6)
circ.cx(3,7)
circ.barrier(range(13))
#9th line :
circ.cx(1,8)
circ.cx(2,8)
circ.cx(7,8)
circ.barrier(range(13))
#10th line :
circ.cx(5,9)
circ.cx(9,5)
circ.cx(6,10)
circ.cx(10,6)
circ.cx(7,11)
circ.cx(11,7)
circ.cx(8,12)
circ.cx(12,8)
circ.barrier(range(13))
#11th line :
circ.cx(1,7)
circ.cx(7,1)
circ.cx(2,8)
circ.cx(8,2)
circ.barrier(range(13))
#12th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(13))
#13th line :
newandplusgate([1,2,9])
newandplusgate([3,4,10])
newandplusgate([5,6,11])
newandplusgate([7,8,12])
circ.barrier(range(13))
#14th line :
circ.cx(8,1)
circ.cx(8,5)
circ.cx(3,2)
circ.cx(4,6)
circ.barrier(range(13))
#15th line :
circ.cx(7,1)
circ.cx(1,7)
circ.cx(8,2)
circ.cx(2,8)
circ.barrier(range(13))


# In[18]:


for i in range(1, 17):
    circ.measure(i, 16-i)
# map the quantum measurement to the classical bits
#circ.measure(range(14), range(14))
# The Qiskit circuit object supports composition using
# the addition operator.
#drawing the circuit


# In[19]:


circ.draw()


# In[20]:


# Use Aer's qasm_simulator
backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = execute(circ, backend_sim, shots=1024)

# Grab the results from the job.
result_sim = job_sim.result()
counts = result_sim.get_counts(circ)
print(counts)


# In[21]:


from qiskit.visualization import plot_histogram
plot_histogram(counts)

