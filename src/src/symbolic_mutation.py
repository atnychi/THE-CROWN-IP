# Symbolic key mutation logic

import random

class SymbolicMutator:
    def mutate_key(self, base_key):
        # Symbolic character shift mutation
        return ''.join(chr((ord(c) + random.randint(1, 5)) % 126) for c in base_key)
