from qiskit import QuantumCircuit
from math import pi

def apply_qft(qc: QuantumCircuit, qubits: list[int] = [], do_swaps: bool = True) -> None:
    '''This function applies a Quantum Fourir Transform to an existing quantum circuit, transforming
    a quantum state from the computational basis into the fourir basis.

    :param qc: Quantum circuit on which to apply the transform
    :param qubits: List of qubit indexes affected by the fourir transform. empty by default, which the function treats as affecting the whole circuit.
    :param do_swaps: boolean indicating whether to do swaps at the end of the circuit. default value is true
    '''

    if not qubits:
        qubits = [i for i in range(qc.num_qubits)]
    n = len(qubits)

    for i in range(n):
        qc.h(qubits[i])
        for j in range(i+1,n):
            theta = (2*pi) / 2 ** (j-i)
            qc.cp(theta, qubits[j], qubits[i])
    
    if do_swaps:
        for i in range(n//2):
            qc.swap(qubits[i], qubits[n-i-1])





