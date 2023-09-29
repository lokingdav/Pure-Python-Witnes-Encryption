import src.util as utils
import src.witenc as witenc
import src.signature as bls

# Example seed, used to generate private key. Always use
# a secure RNG with sufficient entropy to generate a seed (at least 32 bytes).
seed: bytes = bytes([0,  50, 6,  244, 24,  199, 1,  25,  52,  88,  192,
                        19, 18, 12, 89,  6,   220, 18, 102, 58,  209, 82,
                        12, 62, 89, 110, 182, 9,   44, 20,  254, 22])

sk, pk = bls.key_gen(seed)

tag: str = 'tag'
message: str = 'message to be encrypted'

signature = bls.sign(sk, tag)
# Verify the signature
ok: bool = bls.verify(pk, tag, signature)
assert ok

sk_str = utils.to_str(sk)
pk_str = utils.to_str(pk)
sig_str = utils.to_str(signature)

print("Private key: " + sk_str)
print("Public key: " + pk_str)
print("Signature: " + sig_str)

# Encrypt the message
ciphertext: str = witenc.enc(pk, tag, message)
print("Ciphertext\n" + ciphertext)
# Decrypt the message
decrypted_message: str = witenc.dec(signature, ciphertext)
assert message == decrypted_message
print("Decrypted message\n" + decrypted_message)
