from flask import Flask, request, jsonify
# Import thêm class Transposition
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
transposition_cipher = TranspositionCipher()
# --- THÊM ROUTE CHO TRANSPOSITION TẠI ĐÂY ---
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.json
    message = data.get('message', '')
    key = data.get('key', '')
    
    ciphertext = transposition_cipher.encrypt(message, key)
    return jsonify({'ciphertext': ciphertext})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.json
    ciphertext = data.get('ciphertext', '')
    key = data.get('key', '')
    
    plaintext = transposition_cipher.decrypt(ciphertext, key)
    return jsonify({'plaintext': plaintext})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)