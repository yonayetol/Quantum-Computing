from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector
import numpy as np

def deutsch_jozsa_algorithm(oracle_type="balanced"): 
     
    n_qubits = 3 
    
    qc = QuantumCircuit(n_qubits, n_qubits-1)
     
    qc.x(n_qubits-1)
     
    for i in range(n_qubits): qc.h(i)
     
    if oracle_type == "constant_zero":  pass

    elif oracle_type == "constant_one": qc.cx(n_qubits-2, n_qubits-1)

    elif oracle_type == "balanced": 
        qc.cx(0, n_qubits-1)
        qc.cx(1, n_qubits-1)
     
    for i in range(n_qubits-1): qc.h(i)
    
    for i in range(n_qubits-1): qc.measure(i, i)
    
    return qc

def run_deutsch_jozsa_examples(): 
    
    print("=== Deutsch-Jozsa Algorithm Examples ===\n")
    
    oracle_types = ["constant_zero", "constant_one", "balanced"]
    
    for oracle_type in oracle_types:
        print(f"Testing {oracle_type.replace('_', ' ').title()} Oracle:")
        
        qc = deutsch_jozsa_algorithm(oracle_type)
        
        backend = Aer.get_backend('qasm_simulator')
        job = backend.run(qc, shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        most_common_result = max(counts, key=counts.get)
        
        is_constant = all(bit == '0' for bit in most_common_result) or all(bit == '1' for bit in most_common_result)
        
        print(f"  Circuit output: {most_common_result}")
        print(f"  Counts: {counts}")
        print(f"  Function is: {'CONSTANT' if is_constant else 'BALANCED'}")
        print()

def explain_deutsch_jozsa(): 
    
    print("=== Deutsch-Jozsa Algorithm Explanation ===\n")
    
    print("Problem:")
    print("Given a function f: {0,1}^n -> {0,1}, determine if it is:")
    print("- Constant: f(x) = 0 for all x OR f(x) = 1 for all x")
    print("- Balanced: f(x) = 0 for exactly half of inputs, f(x) = 1 for other half")
    print()
    
    print("Classical Solution:")
    print("- Requires 2^(n-1) + 1 queries in worst case")
    print("- Must check more than half of all possible inputs")
    print()
    
    print("Quantum Solution:")
    print("- Requires only 1 query!")
    print("- Uses quantum superposition and interference")
    print()
    
    print("How it works:")
    print("1. Initialize |0⟩^⊗n ⊗ |1⟩")
    print("2. Apply Hadamard gates to create superposition")
    print("3. Apply oracle (black box function)")
    print("4. Apply Hadamard gates again")
    print("5. Measure: all |0⟩ = constant, any |1⟩ = balanced")
    print()
    
    print("Key Quantum Phenomena:")
    print("- Superposition: All possible inputs evaluated simultaneously")
    print("- Interference: Destructive interference cancels out balanced functions")
    print("- Phase kickback: Oracle's effect propagates to input qubits")

def visualize_circuit(): 
    print("=== Circuit Visualization ===\n")
    
    qc = deutsch_jozsa_algorithm("balanced")
    print("Deutsch-Jozsa Circuit (balanced oracle):")
    print(qc) 
     
if __name__ == "__main__":
    explain_deutsch_jozsa()
    print("\n" + "="*50 + "\n")
    visualize_circuit()
    print("\n" + "="*50 + "\n")
    run_deutsch_jozsa_examples()
