import math

class TranspositionCipher:
    def encrypt(self, text, key):
        try:
            key = int(key)
        except ValueError:
            return text
        
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    def decrypt(self, ciphertext, key):
        try:
            key = int(key)
        except ValueError:
            return ciphertext
            
        num_of_columns = math.ceil(len(ciphertext) / key)
        num_of_rows = key
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)
        
        plaintext = [''] * num_of_columns
        row = 0
        col = 0
        
        for symbol in ciphertext:
            plaintext[col] += symbol
            col += 1
            if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
                col = 0
                row += 1
        return ''.join(plaintext)