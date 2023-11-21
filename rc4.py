import os

def generate_random_key(key_size):
    return os.urandom(key_size)

def rc4_encrypt(data, key):
    S = list(range(256))
    j = 0
    out = []

    # Key-scheduling algorithm
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-random generation algorithm
    i = j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])

    return bytes(out)

def rc4_decrypt(data, key):
    return rc4_encrypt(data, key)

if __name__ == "__main__":
    key = generate_random_key(32)
    print("Key: ", key)
    print("Key length: ", len(key))
    data = b"Hello World!"
    print("Data: ", data)
    encrypted_data = rc4_encrypt(data, key)
    print("Encrypted data: ", encrypted_data)
    decrypted_data = rc4_decrypt(encrypted_data, key)
    print("Decrypted data: ", decrypted_data)
    assert data == decrypted_data, "Data and decrypted data are not the same!"