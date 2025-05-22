
from qiskit import QuantumCircuit
from typing import Callable

def deutsch_jozsa_circuit(n_input: int, oracle: Callable[[QuantumCircuit, int], QuantumCircuit]) -> QuantumCircuit:
    '''Creates a general Deutsch-Jozsa style circuit with general oracle

    :param oracle: A callable function object that modifies a quantum circuit, adding an oracle.
    :param n_input: Int giving the number of input bits to the function being tested
    
    :returns: A Quantum circuit implementing DJ, which can then be measured
    '''

    #Add 1 qubit for the target register
    n_qubits = n_input + 1

    #Initialise a quantum circuit with target qubit in state |1>, and a classical register
    qc = QuantumCircuit(n_qubits, n_qubits-1)
    qc.x(n_qubits-1)

    #Apply a hadamard gate to all qubits
    for q in range(n_qubits):
        qc.h(q)

    #Apply oracle to the circuit
        qc = oracle(qc)
    
    #apply hadamard to input register
    for q in range(n_qubits-1):
        qc.h(q)

    #Measure output to classical register
    input_list = [i for i in range(n_input)]
    qc.measure(input_list, input_list)

    return qc

    