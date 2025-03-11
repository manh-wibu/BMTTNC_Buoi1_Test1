class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, text, key):
        rails = [[] for _ in range(key)]
        rail_index = 0
        direction = 1 
        for char in text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
        encrypted_text = ''.join(''.join(rail) for rail in rails)
        return encrypted_text
    
    def rail_fence_decrypt(self, text, key):
        rail_lenghts = [0] * key
        rail_index = 0
        direction = 1

        for _ in range(len(text)):
            rail_lenghts[rail_index] +=1
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lenghts:
            rails.append(text[start: start + length])
            start += length
        
        decrypted_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(text)):
            decrypted_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index] [1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
        return decrypted_text