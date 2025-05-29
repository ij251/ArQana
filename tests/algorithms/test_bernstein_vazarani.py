from qiskit import QuantumCircuit
from arqana.algorithms.bernstein_vazarani import bernstein_vazarani_algorithm
from qiskit_aer import AerSimulator
from qiskit import transpile

def test_bernstein_vazarani_type():
    s = '110'
    qc = bernstein_vazarani_algorithm(s)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 4

def test_bernstein_vazarani_s_counts():
    s = '110'
    qc = bernstein_vazarani_algorithm(s)
    backend = AerSimulator()
    qc = transpile(qc, backend)
    result = backend.run(qc).result()
    counts = result.get_counts()
    assert s[::-1] in counts #Qiskit uses different indexing of qubits
    assert sum(counts.values()) == 1024