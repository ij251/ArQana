from qiskit import QuantumCircuit
from arqana.circuits.oracles import oracle_balanced
from arqana.circuits.deutsch_josza_circuit import deutsch_jozsa_circuit

def test_deutsch_jozsa_circuit():
    qc = deutsch_jozsa_circuit(3, oracle_balanced)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 4
