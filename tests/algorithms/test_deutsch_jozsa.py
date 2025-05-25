from qiskit import QuantumCircuit
from arqana.algorithms.deutsch_jozsa import deutsch_jozsa_algorithm
from qiskit_aer import AerSimulator
from qiskit import transpile

def test_deutsch_jozsa_type():
    qc = deutsch_jozsa_algorithm(3,"balanced")
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 4

def test_deutsch_jozsa_balanced_counts():
    qc = deutsch_jozsa_algorithm(3,"balanced")
    backend = AerSimulator()
    qc = transpile(qc, backend)
    result = backend.run(qc).result()
    counts = result.get_counts()
    assert '011' in counts
    assert sum(counts.values()) == 1024


def test_deutsch_jozsa_constant_counts():
    qc = deutsch_jozsa_algorithm(3,"constant")
    backend = AerSimulator()
    qc = transpile(qc, backend)
    result = backend.run(qc).result()
    counts = result.get_counts()
    assert '000' in counts
    assert sum(counts.values()) == 1024
