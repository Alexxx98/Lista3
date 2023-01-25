from base64 import b64encode


def encrypt(sentence: str) -> str:
    # Convert sentence to bytes via ASCII
    sentence_bytes = sentence.encode('ascii')

    # Convert to 6 bits bytes (base64 bytes)
    b64_bytes = b64encode(sentence_bytes)

    # return encrypted sentence with ASCII
    return b64_bytes.decode('ascii')