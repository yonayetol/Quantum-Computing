from qiskit import QuantumCircuit
from qiskit_aer import Aer 
from math import pi
import random


def chsh_quantum_circuit(alice_input, bob_input): 
    
    qc = QuantumCircuit(2, 2) 

    qc.h(0)
    qc.cx(0, 1)
    
    if alice_input != 0: qc.ry(-pi/2, 0)
    
    if bob_input == 0: qc.ry(-pi/4, 1)  
    else: qc.ry(pi/4, 1)     
    
    qc.measure([0,1], [0,1])
    
    return qc

def run_chsh_game_trials(n_trials=1000): 
    
    print("=== CHSH Game (Bell Inequality Test) ===\n")
    
    classical_wins = 0
    quantum_wins = 0
    
    print(f"Running {n_trials} trials...\n")
    
    for trial in range(n_trials):
        alice_input = random.randint(0, 1)
        bob_input = random.randint(0, 1) 

        alice_output_classical, bob_output_classical = 0, 0 

        classical_wins += (alice_output_classical ^ bob_output_classical) == (alice_input & bob_input)
        
        qc = chsh_quantum_circuit(alice_input, bob_input)
        
        # Execute on simulator
        backend = Aer.get_backend('qasm_simulator')
        job = backend.run(qc, shots=1000)
        result = job.result()
        counts = result.get_counts()
         
        quantum_result = list(counts.keys())[0]
        alice_output_quantum = int(quantum_result[0])
        bob_output_quantum = int(quantum_result[1])
        
        quantum_wins += (alice_output_quantum ^ bob_output_quantum) == (alice_input & bob_input) 
        
    # Calculate win rates
    classical_win_rate = classical_wins / n_trials
    quantum_win_rate = quantum_wins / n_trials
    
    print(f"Results after {n_trials} trials:")
    print(f"Classical strategy win rate: {classical_win_rate:.3f} ({classical_wins}/{n_trials})")
    print(f"Quantum strategy win rate:   {quantum_win_rate:.3f} ({quantum_wins}/{n_trials})")
    print()
    
    # Check for Bell inequality violation
    print("Bell Inequality Analysis:")
    print(f"Classical bound: ≤ 0.75")
    print(f"Quantum prediction: ≈ 0.854")
    print(f"Observed quantum: {quantum_win_rate:.3f}")
    
    if quantum_win_rate > 0.75:
        print("✓ Bell inequality violated! Quantum entanglement confirmed.")
    else:
        print("✗ No Bell inequality violation observed.")
    
    return classical_win_rate, quantum_win_rate

def explain_chsh_game():
    """Explain the CHSH game and Bell inequality"""
    
    print("=== CHSH Game Explanation ===\n")
    
    print("Game Setup:")
    print("1. Alice and Bob are separated and cannot communicate")
    print("2. Each receives a random bit (0 or 1)")
    print("3. Each must output a bit (0 or 1)")
    print("4. They win if: Alice_output ⊕ Bob_output = Alice_input ∧ Bob_input")
    print()
    
    print("Winning Conditions:")
    print("Inputs (x,y) | Required Output (a⊕b) | Winning combinations")
    print("(0,0)        | 0                     | (0,0), (1,1)")
    print("(0,1)        | 0                     | (0,0), (1,1)")
    print("(1,0)        | 0                     | (0,0), (1,1)")
    print("(1,1)        | 1                     | (0,1), (1,0)")
    print()
    
    print("Classical Strategy:")
    print("- Alice and Bob can agree on strategy beforehand")
    print("- Best deterministic strategy: both always output 0")
    print("- Win rate: 75% (wins 3 out of 4 cases)")
    print("- Bell's inequality: ⟨A₀B₀⟩ + ⟨A₀B₁⟩ + ⟨A₁B₀⟩ - ⟨A₁B₁⟩ ≤ 2")
    print()
    
    print("Quantum Strategy:")
    print("- Share entangled Bell pair |Φ⁺⟩")
    print("- Alice measures in Z basis if input=0, X basis if input=1")
    print("- Bob measures in Z basis if input=0, X basis if input=1")
    print("- Win rate: ≈85.4% (violates Bell inequality)")
    print("- Bell's inequality: ⟨A₀B₀⟩ + ⟨A₀B₁⟩ + ⟨A₁B₀⟩ - ⟨A₁B₁⟩ ≤ 2√2")

def demonstrate_measurement_bases(): 
    
    print("=== Measurement Bases Demonstration ===\n")
    
    bases = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    print("Bell state measurements in different bases:")
    for alice_input, bob_input in bases:
        qc = chsh_quantum_circuit(alice_input, bob_input)
        
        # Execute multiple shots to see distribution
        backend = Aer.get_backend('qasm_simulator')
        job = backend.run(qc, shots=1000)
        result = job.result()
        counts = result.get_counts()
        
        print(f"Alice input={alice_input}, Bob input={bob_input}: {counts}")
        

# Calculate expectation values for Bell parameter
# S = ⟨A₀B₀⟩ + ⟨A₀B₁⟩ + ⟨A₁B₀⟩ - ⟨A₁B₁⟩


def visualize_circuit(): 
    
    print("=== Circuit Visualization ===\n")
    
    qc = chsh_quantum_circuit(1, 1)
    print("CHSH Circuit (Alice input=1, Bob input=1):")
    print(qc)
    

if __name__ == "__main__":
    explain_chsh_game()
    print("\n" + "="*50 + "\n")
    demonstrate_measurement_bases()
    print("\n" + "="*50 + "\n") 
    visualize_circuit()
    print("\n" + "="*50 + "\n")
    run_chsh_game_trials(1000)
