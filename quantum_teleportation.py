from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace, Operator
import numpy as np

def _fix_global_phase(state_vec: np.ndarray) -> np.ndarray:
    """Return a copy with global phase chosen so first nonzero amplitude is real and positive."""
    v = state_vec.astype(complex).copy()
    for amp in v:
        if np.abs(amp) > 1e-12:
            v *= np.exp(-1j * np.angle(amp))
            break
    return v

def _amp_str(z: complex) -> str:
    magnitude = np.abs(z)
    phase = np.angle(z)
    return f"{magnitude:.3f}∠{phase:.2f}"

def _dm_to_statevector(dm) -> np.ndarray:
    """Extract the principal eigenvector of a 2x2 density matrix and fix global phase."""
    vals, vecs = np.linalg.eigh(dm.data)
    v = vecs[:, int(np.argmax(vals))]
    return _fix_global_phase(v)

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

    # Target state prepared on q0 (what we aim to recover on q2)
    target = QuantumCircuit(1)
    target.h(0)
    target.t(0)
    target_vec = _fix_global_phase(Statevector.from_instruction(target).data)

    print("Alice outcomes and Bob's recovered state (after required corrections):")

    # Simulate all 4 possible measurement outcomes for Alice
    # Reshape statevector into tensor with axes (q2, q1, q0)
    psi = state.data.reshape(2, 2, 2)
    for meas_q0 in [0, 1]:
        for meas_q1 in [0, 1]:
            # Project onto Alice's outcome (q0=meas_q0, q1=meas_q1) and extract Bob's 2-amplitude vector
            bob_vec = psi[:, meas_q1, meas_q0].astype(complex)

            # Apply Bob's required corrections: Z if q0==1, X if q1==1
            if meas_q0 == 1:
                bob_vec[1] *= -1
            if meas_q1 == 1:
                bob_vec = bob_vec[::-1]

            # Normalize and fix global phase for readability
            norm = np.linalg.norm(bob_vec)
            if norm > 0:
                bob_vec = bob_vec / norm
            bob_vec = _fix_global_phase(bob_vec)

            teleported_str = f"{_amp_str(target_vec[0])}|0> + {_amp_str(target_vec[1])}|1>"
            got_str = f"{_amp_str(bob_vec[0])}|0> + {_amp_str(bob_vec[1])}|1>"
            print(f"Alice (q0={meas_q0}, q1={meas_q1}) -> teleported: {teleported_str} | Bob: {got_str}")

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

if __name__ == "__main__":
    visualize_circuit()
    quantum_teleportation()
