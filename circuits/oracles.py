from qiskit import QuantumCircuit

def oracle_balanced(qc: QuantumCircuit, n_qubits: int) -> QuantumCircuit:
    '''This is a balanced oracle that XORs the first 2 qubits in the register, using the last qubit as the target.'''
    # Apply CNOT gates to flip the target qubit based on the first two qubits
    for q in range(2):
        qc.cx(q, n_qubits - 1)
    # The target qubit is now in a state that depends on the first two qubits
    return qc


def oracle_constant(qc: QuantumCircuit, n_qubits: int) -> QuantumCircuit:
    '''This is a constant oracle that doesn't change the target qubit.'''
    return qc