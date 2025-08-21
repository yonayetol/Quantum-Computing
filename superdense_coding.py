from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector 

def superdense_coding_protocol(message): 
     
    qc = QuantumCircuit(2, 2)
    
    qc.h(0)
    qc.cx(0, 1)
     
    if message == "00": pass
    elif message == "01": qc.x(0)
    elif message == "10": qc.z(0)
    elif message == "11": 
        qc.x(0)
        qc.z(0)
    
    # Step 3: Bob performs Bell measurement
    # Apply inverse of Bell state creation
    qc.cx(0, 1)
    qc.h(0)
    
    qc.measure([0, 1], [1, 0])

    
    return qc

def run_superdense_coding_examples():     
    print("=== Superdense Coding Protocol Examples ===\n")
    
    messages = ["00", "01", "10", "11"]
    
    for message in messages:
        print(f"Encoding message: {message}")
        
        qc = superdense_coding_protocol(message)
        
        backend = Aer.get_backend('qasm_simulator')
        job = backend.run(qc, shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        most_common_result = max(counts, key=counts.get)
        
        print(f"  Circuit output: {most_common_result}")
        print(f"  Counts: {counts}")
        print(f"  Decoded message: {most_common_result}")
        print(f"  Success: {'✓' if most_common_result == message else '✗'}")
        print()

def explain_superdense_coding(): 
    
    print("=== Superdense Coding Protocol Explanation ===\n")
    
    print("Problem:")
    print("Alice wants to send 2 classical bits to Bob using only 1 qubit")
    print("(plus a pre-shared Bell pair)")
    print()
    
    print("Classical Solution:")
    print("- Requires 2 bits to send 2 bits")
    print("- No compression possible")
    print()
    
    print("Quantum Solution:")
    print("- Send only 1 qubit to transmit 2 bits!")
    print("- Uses pre-shared entanglement (Bell pair)")
    print()
    
    print("Protocol Steps:")
    print("1. Alice and Bob share Bell pair |Φ⁺⟩ = (|00⟩ + |11⟩)/√2")
    print("2. Alice encodes 2 bits by applying operation to her qubit:")
    print("   - 00: Identity (I)")
    print("   - 01: Pauli-X")
    print("   - 10: Pauli-Z")
    print("   - 11: Pauli-X then Pauli-Z")
    print("3. Alice sends her qubit to Bob")
    print("4. Bob performs Bell measurement to decode")
    print()
    
    print("Key Quantum Phenomena:")
    print("- Entanglement: Bell pair enables non-local correlations")
    print("- Quantum gates: Different operations create orthogonal states")
    print("- Measurement: Bell measurement distinguishes all 4 states")

def create_bell_pair(): 
    print("=== Bell Pair Creation ===\n")
    
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    
    state = Statevector.from_instruction(qc)
    
    print("Bell pair |Φ⁺⟩ = (|00⟩ + |11⟩)/√2")
    print(f"State vector: {state}")
    print() 

def visualize_circuit(): 
    
    print("=== Circuit Visualization ===\n")
    
    qc = superdense_coding_protocol("01")
    print("Superdense Coding Circuit (encoding '01'):")
    print(qc) 

if __name__ == "__main__":
    explain_superdense_coding()
    print("\n" + "="*50 + "\n")
    create_bell_pair()
    print("\n" + "="*50 + "\n")
    visualize_circuit()
    print("\n" + "="*50 + "\n")
    run_superdense_coding_examples()
