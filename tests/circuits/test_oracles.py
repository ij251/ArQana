from qiskit import QuantumCircuit
from arqana.circuits.oracles import oracle_balanced, oracle_constant

def test_balanced_oracle_qubit_count():
    qc = QuantumCircuit(3)
    qc2 = oracle_balanced(qc, 3)
    assert isinstance(qc2, QuantumCircuit)
    assert qc2.num_qubits == 3

def test_constant_oracle_type():
    qc = QuantumCircuit(3)
    qc2 = oracle_constant(qc, 3)
    assert isinstance(qc2, QuantumCircuit)
    assert qc == qc2
