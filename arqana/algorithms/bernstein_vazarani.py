from ..circuits.oracles import oracle_bv
from ..circuits.deutsch_jozsa_circuit import deutsch_jozsa_circuit
from qiskit import QuantumCircuit

def bernstein_vazarani_algorithm(s: str) -> QuantumCircuit:
    '''Implements the Bernstein-Vazarani quantum algorithm

    :param s: Bitstring s that should be found using the algorithm by querying the oracle.
    
    :returns: A Quantum circuit implementing BV, which can then be measured
    '''

    oracle = oracle_bv(s)
    return deutsch_jozsa_circuit(len(s), oracle)