from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace, Operator, state_fidelity
import numpy as np

def quantum_teleportation():
    """
    Simulates quantum teleportation of a qubit using entanglement.
    """
    print("--- Running Quantum Teleportation ---")

    # Step 1: Initialize 3 qubits (q0 = state to teleport, q1 = Alice's entanglement, q2 = Bob's entanglement)
    qc = QuantumCircuit(3)

    # Step 2: Prepare the state to teleport (Alice's qubit)
    qc.h(0)
    qc.t(0)
 
    # Step 3: Create entangled Bell pair between q1 (Alice) and q2 (Bob)
    qc.h(1)
    qc.cx(1, 2)

    # Step 4: Bell measurement on Alice's qubits
    qc.cx(0, 1)
    qc.h(0)

    # Step 5: Get the full statevector
    state = Statevector.from_instruction(qc)

    # Define correction operators (leftmost label targets highest-index qubit)
    X2 = Operator.from_label('XII')  # X on q2
    Z2 = Operator.from_label('ZII')  # Z on q2

    print("Teleported state of Bob's qubit for all measurement outcomes:")

    # Simulate all 4 possible measurement outcomes for Alice
    for meas_q0 in [0, 1]:
        for meas_q1 in [0, 1]:
            corrected_state = state.copy()

            # Apply X if Alice's q1 = 1
            if meas_q1 == 1:
                corrected_state = corrected_state.evolve(X2)

            # Apply Z if Alice's q0 = 1
            if meas_q0 == 1:
                corrected_state = corrected_state.evolve(Z2)

            # Reduce to Bob's qubit
            bob_state = partial_trace(corrected_state, [0, 1])
            print(f"Alice measures q0={meas_q0}, q1={meas_q1} -> Bob's qubit state:\n{bob_state}\n")

    print("-------------------------------------")

def visualize_circuit():
    """Print a text-based diagram of the teleportation circuit."""
    print("--- Teleportation Circuit (text diagram) ---")
    qc = QuantumCircuit(3)
    qc.h(0); qc.t(0)
    qc.h(1); qc.cx(1, 2)
    qc.cx(0, 1); qc.h(0)
    print(qc.draw(output='text'))
    print("-------------------------------------------")

def example_fidelity():
    """Example: teleport an arbitrary single-qubit state and report fidelity."""
    print("--- Example: Teleport arbitrary state and compute fidelity ---")
    # Prepare arbitrary state |psi> = Rz(phi) Ry(theta) |0>
    theta, phi = np.pi/3, np.pi/5

    # Build 1-qubit circuit for target
    target_circ = QuantumCircuit(1)
    target_circ.ry(theta, 0)
    target_circ.rz(phi, 0)
    target_state = Statevector.from_instruction(target_circ)

    # Build 3-qubit teleportation circuit up to Bell-measurement
    qc = QuantumCircuit(3)
    qc.ry(theta, 0)
    qc.rz(phi, 0)
    qc.h(1); qc.cx(1, 2)
    qc.cx(0, 1); qc.h(0)

    state = Statevector.from_instruction(qc)
    X2 = Operator.from_label('XII')
    Z2 = Operator.from_label('ZII')

    # Average fidelity over all Alice measurement outcomes (each occurs with prob 1/4)
    fidelities = []
    for meas_q0 in [0, 1]:
        for meas_q1 in [0, 1]:
            corrected = state
            if meas_q1 == 1:
                corrected = corrected.evolve(X2)
            if meas_q0 == 1:
                corrected = corrected.evolve(Z2)
            bob_dm = partial_trace(corrected, [0, 1])
            fid = state_fidelity(bob_dm, target_state)
            fidelities.append(fid)
            print(f"Outcome (q0={meas_q0}, q1={meas_q1}) fidelity: {fid:.6f}")

    print(f"Minimum fidelity over outcomes: {min(fidelities):.6f}")
    print("-------------------------------------------------------------")

if __name__ == "__main__":
    visualize_circuit()
    quantum_teleportation()
    example_fidelity()
