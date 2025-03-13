from flask import Flask,  request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher 
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypt_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypt_text})

vigenere_cipher = VigenereCipher()

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypt_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypt_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypt_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypt_text})

railfence_cipher = RailFenceCipher()

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypt_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({"encrypted_message": decrypt_text})

playfair_cipher = PlayFairCipher()

@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"encrypted_message": playfair_matrix})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypt_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({"encrypted_message": encrypt_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypt_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({"encrypted_message": decrypt_text})

transposition_cipher = TranspositionCipher()

@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypt_text = transposition_cipher.transposition_encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypt_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypt_text = transposition_cipher.transposition_decrypt(cipher_text, key)
    return jsonify({"encrypted_message": decrypt_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

