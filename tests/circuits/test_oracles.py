from qiskit import QuantumCircuit
from arqana.circuits.oracles import oracle_balanced, oracle_constant, oracle_bv

def test_balanced_oracle():
    qc = QuantumCircuit(3)
    oracle_balanced(qc)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 3

def test_constant_oracle():
    qc = QuantumCircuit(3)
    qc2 = qc
    oracle_constant(qc)
    assert isinstance(qc, QuantumCircuit)
    assert qc == qc2

def test_bv_oracle():
    s = '110'
    qc = QuantumCircuit(3)
    oracle = oracle_bv(s)
    oracle(qc)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 3