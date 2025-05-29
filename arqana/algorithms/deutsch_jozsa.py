from ..circuits.oracles import oracle_constant, oracle_balanced
from ..circuits.deutsch_jozsa_circuit import deutsch_jozsa_circuit
from qiskit import QuantumCircuit

def deutsch_jozsa_algorithm(n_input: int, oracle_type: str = "balanced") -> QuantumCircuit:
    '''Implements the Deutsch-Jozsa quantum algorithm

    :param oracle_type: String declaration of the type of oracle, balanced or constant
    :param n_input: Int giving the number of input bits to the function being tested
    
    :returns: A Quantum circuit implementing DJ, which can then be measured
    '''

    #Apply oracle to the circuit
    if oracle_type.lower() == "balanced":
        return deutsch_jozsa_circuit(n_input, oracle_balanced)
    elif oracle_type.lower() == "constant":
        return deutsch_jozsa_circuit(n_input, oracle_constant)
    else:
        raise ValueError("Oracle type must be constant or balanced.")
    