from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def deutsch_jozsa_algorithm(oracle): 
    n_qubits = oracle.num_qubits
    n_input = n_qubits - 1

    qc = QuantumCircuit(n_qubits, n_input)

    # Step 1: Initialize output qubit to |1>
    qc.x(n_qubits-1)
    qc.h(n_qubits-1)

    # Step 2: Apply Hadamard to input qubits
    for i in range(n_input):
        qc.h(i)

    # Step 3: Apply oracle using compose
    qc = qc.compose(oracle)

    # Step 4: Apply Hadamard again to input qubits
    for i in range(n_input):
        qc.h(i)

    # Step 5: Measure input qubits
    for i in range(n_input):
        qc.measure(range(n_input), range(n_input))

    return qc
 
oracle_const_0 = QuantumCircuit(3)   
oracle_const_1 = QuantumCircuit(3)  
oracle_const_1.x(2)

oracle_balanced = QuantumCircuit(3)
oracle_balanced.cx(0,2)
oracle_balanced.cx(1,2)

# -------------------------
# Run Deutsch-Jozsa
# -------------------------
backend = AerSimulator()
examples = {
    "constant_zero": oracle_const_0,
    "constant_one": oracle_const_1,
    "balanced_xor": oracle_balanced
}

for name, oracle in examples.items():
    qc = deutsch_jozsa_algorithm(oracle)
    result = backend.run(qc, shots=1000).result()
    counts = result.get_counts()
    most_common = max(counts, key=counts.get)
    function_type = "CONSTANT" if most_common == "00" else "BALANCED"
    print(f"{name}: measured {most_common}, classified as {function_type}")
    print("Circuit:")
    print(qc.draw(output='text'))
    print("\n" + "="*50 + "\n")
