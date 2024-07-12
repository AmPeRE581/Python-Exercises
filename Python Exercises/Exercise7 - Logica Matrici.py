import numpy as np

class TIBPALSimulator:
    def __init__(self, num_inputs, num_terms):
        self.num_inputs = num_inputs
        self.num_terms = num_terms
        # Creare una matrice di connessioni (num_terms x 2*num_inputs)
        self.and_matrix = np.zeros((num_terms, 2*num_inputs), dtype=bool)
        self.inputs = np.zeros(num_inputs, dtype=bool)
    
    def set_input(self, index, value):
        self.inputs[index] = value
    
    def program_and_term(self, term_index, connections):
        for conn in connections:
            self.and_matrix[term_index, conn] = True
    
    def compute_and_terms(self):
        and_terms = np.zeros(self.num_terms, dtype=bool)
        for i in range(self.num_terms):
            term = True
            for j in range(self.num_inputs):
                if self.and_matrix[i, j]:  # Ingresso non invertito
                    term = term and self.inputs[j]
                if self.and_matrix[i, j + self.num_inputs]:  # Ingresso invertito
                    term = term and not self.inputs[j]
            and_terms[i] = term
        return and_terms
    
    def compute_output(self, or_terms):
        and_terms = self.compute_and_terms()
        output = False
        for term in or_terms:
            output = output or and_terms[term]
        return output

# Esempio di utilizzo
simulator = TIBPALSimulator(num_inputs=3, num_terms=4)

# Configurazione degli ingressi
simulator.set_input(0, True)  # A
simulator.set_input(1, False) # B
simulator.set_input(2, True)  # C

# Programmazione della matrice AND
# Term 0: A AND B
simulator.program_and_term(0, [0, 1])        # A and B
# Term 1: NOT A AND C
simulator.program_and_term(1, [3, 2])        # NOT A and C
# Term 2: B AND NOT C
simulator.program_and_term(2, [1, 5])        # B and NOT C
# Term 3: A AND NOT B AND C
simulator.program_and_term(3, [0, 4, 2])     # A and NOT B and C

# Calcolo delle uscite logiche
# Output: (Term 0 OR Term 1)
output = simulator.compute_output([0, 1])
print(f"Output (A AND B) OR (NOT A AND C): {output}")

# Output: (Term 2 OR Term 3)
output = simulator.compute_output([2, 3])
print(f"Output (B AND NOT C) OR (A AND NOT B AND C): {output}")
