from qiskit import QuantumCircuit
from arqana.circuits.qft import apply_qft
from qiskit_aer import AerSimulator
from qiskit import transpile

def test_qft_type():
    n = 3
    qc = QuantumCircuit(3)
    apply_qft(qc)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 3

def test_qft_uniform_superposition():
    n = 3
    qc = QuantumCircuit(3,3)
    apply_qft(qc)
    qc.measure(range(n),range(n))
    backend = AerSimulator()
    qc = transpile(qc, backend)
    result = backend.run(qc).result()
    counts = result.get_counts()
    assert len(counts) == 2**n
    assert sum(counts.values()) == 1024
