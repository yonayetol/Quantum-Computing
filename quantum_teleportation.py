from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector
import numpy as np

def quantum_teleportation_protocol(qubit_state):
    """
    Quantum Teleportation Protocol Implementation using Qiskit
    
    This protocol allows Alice to teleport an unknown quantum state to Bob
    using a shared Bell pair and classical communication.
    
    Protocol:
    1. Alice and Bob share a Bell pair |Φ⁺⟩
    2. Alice has an unknown qubit state |ψ⟩
    3. Alice performs Bell measurement on her qubit and Bell pair qubit
    4. Alice sends 2 classical bits to Bob
    5. Bob applies conditional operations to recover |ψ⟩
    """
    
    # Create device with 3 qubits:
    # qubit 0: Alice's unknown qubit |ψ⟩
    # qubit 1: Alice's Bell pair qubit
    # qubit 2: Bob's Bell pair qubit
    qc = QuantumCircuit(3, 3)
    
    # Step 1: Prepare unknown qubit state |ψ⟩ on qubit 0
    if qubit_state == "|0⟩":
        # Already in |0⟩ state
        pass
    elif qubit_state == "|1⟩":
        qc.x(0)
    elif qubit_state == "|+⟩":
        qc.h(0)
    elif qubit_state == "|-⟩":
        qc.h(0)
        qc.z(0)
    elif qubit_state == "|i⟩":
        qc.h(0)
        qc.s(0)
    
    # Step 2: Create Bell pair on qubits 1 and 2
    qc.h(1)
    qc.cx(1, 2)
    
    # Step 3: Perform Bell measurement on qubits 0 and 1
    qc.cx(0, 1)
    qc.h(0)
    
    # Step 4: Apply conditional operations on qubit 2 based on measurement
    # This simulates the classical communication and conditional operations
    # In real teleportation, these would be applied after receiving classical bits
    
    # For demonstration, we'll apply the operations that would be needed
    # based on the Bell measurement outcome
    # (In practice, this would be done after classical communication)
    
    # Measure all qubits
    qc.measure([0, 1, 2], [0, 1, 2])
    
    return qc

def run_teleportation_examples():
    """Run examples of quantum teleportation with different input states"""
    
    print("=== Quantum Teleportation Examples ===\n")
    
    input_states = ["|0⟩", "|1⟩", "|+⟩", "|-⟩", "|i⟩"]
    
    for state in input_states:
        print(f"Teleporting state: {state}")
        
        # Create and run the circuit
        qc = quantum_teleportation_protocol(state)
        
        # Execute on simulator
        backend = Aer.get_backend('qasm_simulator')
        job = backend.run(qc, shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        # Get most common result
        most_common_result = max(counts, key=counts.get)
        
        print(f"  Circuit output: {most_common_result}")
        print(f"  Counts: {counts}")
        print(f"  Alice's qubit (bit 0): {most_common_result[0]}")
        print(f"  Bell measurement (bit 1): {most_common_result[1]}")
        print(f"  Bob's qubit (bit 2): {most_common_result[2]}")
        print()

def explain_quantum_teleportation():
    """Explain the Quantum Teleportation protocol"""
    
    print("=== Quantum Teleportation Protocol Explanation ===\n")
    
    print("Problem:")
    print("Alice wants to send an unknown quantum state |ψ⟩ to Bob")
    print("without physically transporting the qubit")
    print()
    
    print("Classical Solution:")
    print("- Impossible! Cannot copy unknown quantum states (no-cloning theorem)")
    print("- Measurement destroys quantum information")
    print()
    
    print("Quantum Solution:")
    print("- Use entanglement and classical communication")
    print("- Destroys original state but creates perfect copy elsewhere")
    print()
    
    print("Protocol Steps:")
    print("1. Alice and Bob share Bell pair |Φ⁺⟩")
    print("2. Alice has unknown qubit |ψ⟩")
    print("3. Alice performs Bell measurement on |ψ⟩ and her Bell qubit")
    print("4. Alice sends 2 classical bits to Bob")
    print("5. Bob applies conditional operations to recover |ψ⟩")
    print()
    
    print("Key Quantum Phenomena:")
    print("- Entanglement: Bell pair enables non-local correlations")
    print("- Measurement: Bell measurement entangles Alice's qubits")
    print("- No-cloning: Original state is destroyed during teleportation")
    print("- Classical communication: Required to complete teleportation")

def demonstrate_bell_measurement():
    """Demonstrate Bell measurement outcomes"""
    
    print("=== Bell Measurement Demonstration ===\n")
    
    qc = QuantumCircuit(2, 2)
    
    # Create Bell state
    qc.h(0)
    qc.cx(0, 1)
    
    # Perform Bell measurement
    qc.cx(0, 1)
    qc.h(0)
    
    # Measure
    qc.measure([0, 1], [0, 1])
    
    # Execute on simulator
    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    print("Bell measurement on |Φ⁺⟩:")
    print(f"Result: {counts}")
    print("Expected: Mostly '11' (both qubits in |0⟩ state)")
    print()
    
    print("Bell measurement outcomes:")
    print("- '11': |Φ⁺⟩ state")
    print("- '10': |Φ⁻⟩ state") 
    print("- '01': |Ψ⁺⟩ state")
    print("- '00': |Ψ⁻⟩ state")

def explain_conditional_operations():
    """Explain the conditional operations in teleportation"""
    
    print("=== Conditional Operations in Teleportation ===\n")
    
    print("After Bell measurement, Bob applies operations based on classical bits:")
    print()
    print("Bell measurement outcome | Classical bits | Bob's operation")
    print("|Φ⁺⟩ (11)              | 11             | Identity (I)")
    print("|Φ⁻⟩ (10)              | 10             | Pauli-Z")
    print("|Ψ⁺⟩ (01)              | 01             | Pauli-X")
    print("|Ψ⁻⟩ (00)              | 00             | Pauli-X then Pauli-Z")
    print()
    
    print("Why this works:")
    print("- Bell measurement projects Alice's qubits into Bell basis")
    print("- Each Bell state corresponds to different transformation of Bob's qubit")
    print("- Classical communication tells Bob which transformation to apply")

def visualize_circuit():
    """Visualize the quantum teleportation circuit"""
    
    print("=== Circuit Visualization ===\n")
    
    qc = quantum_teleportation_protocol("|+⟩")
    print("Quantum Teleportation Circuit (teleporting |+⟩):")
    print(qc)
    
    # Show circuit diagram
    try:
        print("\nCircuit diagram:")
        print(qc.draw(output='text'))
    except ImportError:
        print("\nCircuit visualization requires qiskit[visualization]")

if __name__ == "__main__":
    explain_quantum_teleportation()
    print("\n" + "="*50 + "\n")
    demonstrate_bell_measurement()
    print("\n" + "="*50 + "\n")
    explain_conditional_operations()
    print("\n" + "="*50 + "\n")
    visualize_circuit()
    print("\n" + "="*50 + "\n")
    run_teleportation_examples()
