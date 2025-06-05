from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from arqana.circuits.qft import apply_qft, apply_iqft
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

def test_inverse_qft_type():
    n = 3
    qc = QuantumCircuit(3)
    apply_qft(qc)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 3


def test_inverse_qft_identity():
    n = 3
    qc = QuantumCircuit(3)
    qc_identity = qc.copy()
    apply_qft(qc)
    apply_iqft(qc)
    assert Operator(qc).equiv(Operator(qc_identity)) #Test that applyinf qft then iqft is functionally equivilent to the identity

