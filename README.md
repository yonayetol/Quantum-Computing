# Quantum Computing Circuits with Qiskit

This repository contains implementations of four fundamental quantum computing algorithms and protocols using Qiskit. Each implementation demonstrates key quantum phenomena including superposition, entanglement, interference, and quantum measurement.

## 🚀 What's Implemented

### 1. **Deutsch-Jozsa Algorithm** (`deutsch_jozsa.py`)
- **Purpose**: Determines if a function is constant or balanced using only 1 quantum query
- **Classical Complexity**: O(2^(n-1) + 1) queries
- **Quantum Complexity**: O(1) query!
- **Key Quantum Phenomena**: Superposition, interference, phase kickback
- **How it works**: Creates superposition of all possible inputs, applies oracle function, uses interference to distinguish constant vs balanced functions

### 2. **Superdense Coding Protocol** (`superdense_coding.py`)
- **Purpose**: Transmit 2 classical bits using only 1 qubit (plus pre-shared entanglement)
- **Classical Limitation**: 2 bits needed to send 2 bits
- **Quantum Advantage**: 1 qubit can carry 2 bits of information
- **Key Quantum Phenomena**: Entanglement (Bell pairs), quantum gates, measurement
- **How it works**: Alice and Bob share Bell pair, Alice encodes 2 bits by applying one of 4 operations, Bob performs Bell measurement to decode

### 3. **Quantum Teleportation Protocol** (`quantum_teleportation.py`)
- **Purpose**: Transfer unknown quantum state from Alice to Bob without physical transport
- **Classical Impossibility**: Cannot copy unknown quantum states (no-cloning theorem)
- **Quantum Solution**: Use entanglement + classical communication
- **Key Quantum Phenomena**: Entanglement, Bell measurement, no-cloning, classical communication
- **How it works**: Alice performs Bell measurement on unknown qubit + Bell pair qubit, sends classical bits to Bob, Bob applies conditional operations

### 4. **CHSH Game (Bell Inequality Test)** (`chsh_game.py`)
- **Purpose**: Demonstrate quantum entanglement by violating Bell's inequality
- **Classical Strategy**: Maximum win rate = 75%
- **Quantum Strategy**: Maximum win rate ≈ 85.4%
- **Key Quantum Phenomena**: Entanglement, measurement bases, Bell inequality violation
- **How it works**: Alice and Bob share Bell pair, measure in different bases based on inputs, correlation violates classical bounds

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Dependencies
- `qiskit>=0.44.0` - Core quantum computing framework
- `qiskit-aer>=0.12.0` - Aer simulator backend
- `numpy>=1.21.0` - Numerical computing
- `matplotlib>=3.5.0` - Plotting and visualization

## 🎯 How to Run

### Run All Circuits
```bash
# Deutsch-Jozsa Algorithm
python deutsch_jozsa.py

# Superdense Coding Protocol
python superdense_coding.py

# Quantum Teleportation Protocol
python quantum_teleportation.py

# CHSH Game (Bell Inequality Test)
python chsh_game.py
```

### What Each Script Does
Each script provides:
1. **Explanation** of the algorithm/protocol
2. **Circuit visualization** showing the quantum gates
3. **Examples** demonstrating the protocol in action
4. **Results analysis** showing quantum vs classical behavior

## 🔬 Key Quantum Phenomena Demonstrated

### **Superposition**
- Qubits exist in linear combination of |0⟩ and |1⟩ states
- Demonstrated in: Deutsch-Jozsa (input superposition), all protocols (Hadamard gates)

### **Entanglement**
- Non-local correlations between qubits
- Demonstrated in: Bell pairs (superdense coding, teleportation, CHSH game)

### **Interference**
- Quantum amplitudes can constructively/destructively interfere
- Demonstrated in: Deutsch-Jozsa (destructive interference for balanced functions)

### **Measurement**
- Collapses quantum state to classical outcome
- Demonstrated in: All protocols (final measurements)

### **Quantum Gates**
- Single-qubit: H (Hadamard), X (Pauli-X), Z (Pauli-Z)
- Two-qubit: CNOT (controlled-X)
- Used throughout for state preparation and manipulation

## 📊 Understanding the Results

### Deutsch-Jozsa
- **Constant functions**: All measurements return |0⟩
- **Balanced functions**: Some measurements return |1⟩
- **Quantum advantage**: 1 query vs exponential classical queries

### Superdense Coding
- **Success**: Decoded message matches original 2-bit input
- **Entanglement**: Bell pair enables non-local correlations
- **Compression**: 1 qubit carries 2 bits of information

### Quantum Teleportation
- **Bell measurement**: Projects Alice's qubits into Bell basis
- **Classical communication**: Required to complete teleportation
- **State transfer**: Unknown state perfectly transferred to Bob

### CHSH Game
- **Classical bound**: Win rate ≤ 75%
- **Quantum bound**: Win rate ≤ 85.4%
- **Bell violation**: Observed correlation exceeds classical limit

## 🎓 Learning Objectives

After running these circuits, you should understand:

1. **Quantum vs Classical**: How quantum algorithms achieve exponential speedups
2. **Entanglement**: How non-local correlations enable quantum protocols
3. **Measurement**: How quantum measurement affects quantum states
4. **Quantum Gates**: How basic quantum operations manipulate qubits
5. **Protocols**: How quantum mechanics enables impossible classical tasks

## 🔍 Troubleshooting

### Common Issues
- **Import errors**: Ensure all dependencies are installed
- **Circuit execution**: Circuits use Aer simulator for reliable results
- **Visualization**: Text-based circuit diagrams work without additional packages

### Performance Notes
- All circuits run on quantum simulator (not real hardware)
- Results are deterministic for demonstration purposes
- Real quantum computers would show noise and decoherence

## 📚 Further Reading

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Quantum Computing for Everyone](https://mitpress.mit.edu/books/quantum-computing-everyone)
- [Quantum Information and Computation](https://www.cambridge.org/core/books/quantum-information-and-computation)

## 🤝 Contributing

Feel free to:
- Improve circuit implementations
- Add more quantum algorithms
- Enhance explanations and documentation
- Report bugs or issues

---

**Note**: These implementations are educational and demonstrate quantum computing principles. For production use, consider error correction, noise mitigation, and real quantum hardware constraints.
