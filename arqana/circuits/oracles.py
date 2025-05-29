from qiskit import QuantumCircuit
from typing import Callable

def oracle_balanced(qc: QuantumCircuit):
    '''This is a balanced oracle that XORs the first 2 qubits in the register, using the last qubit as the target.
    It modifies the circuit in place
    
    :param qc: Quantum circuit object to apply the oracle to'''
    # Apply CNOT gates to flip the target qubit based on the first two qubits
    for q in range(2):
        qc.cx(q, qc.num_qubits - 1)


def oracle_constant(qc: QuantumCircuit):
    '''This is a constant oracle that doesn't change the target qubit.
    It modifies the circuit in place
    
    :param qc: Quantum circuit object to apply the oracle to'''


def oracle_bv(s: str) -> Callable[[QuantumCircuit], None]:
    '''This is an oracle for bv that flips the target qubit if the corresponding bit in s is a 1
    It modifies the circuit in place
    
    :param s: hidden bitstring we are trying to find with the algorithm '''
    def builder(qc: QuantumCircuit):
        for q in range(qc.num_qubits - 1):
            if s[q] == '1':
                qc.cx(q, qc.num_qubits - 1)
    
    return builder