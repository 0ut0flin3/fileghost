import json
import os
import secrets
import sys


SEP = '__FIL3GH0ST__'.encode()
SEPARATOR = list(bytes(SEP))


class keygen:
    @classmethod
    def generate(cls) -> "keygen":
        '''
        Generates a new keygen object with random keys, based on the ``secrets`` module.
        '''
        keys = []

        numbers = set()
        while len(numbers) < 256:
            n = secrets.randbelow(256)

            if n not in numbers:
                numbers.add(n)
                keys.append(n)

        return cls(keys)

    @classmethod
    def from_file(cls, path: str) -> "keygen":
        '''
        Loads a keygen object from a file.
        '''
        with open(path, "r") as f:
            keys = json.loads(f.read())

        return cls(list(keys.values()))

    def __init__(self, keys: list) -> None:
        if set(keys) != set(range(256)):
            raise ValueError("Keystore must contain all numbers from 0 to 255")

        self._keys = keys
        self._keystore = dict(enumerate(self._keys))

    def to_keystore(self) -> dict:
        return self._keystore.copy()

    def to_byte_array(self) -> list:
        return self._keys.copy()

    def to_hex(self):
        return bytes(self._keys).hex()

    def to_int(self):
        return int(self.to_hex(), 16)

    def to_file(self, path: str) -> None:
        def write_keys() -> None:
            j = json.dumps(self.to_keystore())
            with open(path, "w") as f:
                f.write(j)

            print("Generated new keystore:", path)

        if os.path.exists(path):
            q = input('''This file already exists on specified path. Do you want to replace it?\nBe careful, if you replace it, all the files encrypted with that keystore will be lost forever.\nContinue? [\033[1mY\033[0m/\033[1mN\033[0m] ''')
            if q not in "yY":
                print("Aborted.")
                sys.exit()

        # path doesn't exist OR user wants to replace it
        write_keys()

    def encrypt(self, inp: bytes, disable_input_max_length: bool = False) -> list:
        print('\n')

        if not disable_input_max_length and len(inp) > 256:
            print("error: input cannot exceed 256 bytes")
            sys.exit()

        # Input is too short. Extend it with salt and random bytes.
        if len(inp) < 256:
            inp = list(inp)
            inp.extend(SEPARATOR)

            while len(inp) < 256:
                inp.append(secrets.randbelow(256))

            inp = bytes(inp)

        progress = 0
        enc_bytes = [self._keystore[n] for n in inp]

        # TODO: Consider user tqdm package instead of printing progress manually
        for i in range(len(enc_bytes)):
            enc_bytes[i] = enc_bytes[i] ^ self._keystore[i % 256]

            progress += 1
            percent = '{:.2%}'.format(progress / len(inp))
            print(f"Encrypted {progress} bytes of {len(inp)} total. [{percent}%]", end='\r')

        print('\n\nDone.\n')
        return enc_bytes

    def encrypt_file(self, path: str, disable_input_max_length=False) -> list:
        with open(path, "rb") as f:
            return self.encrypt(f.read(), disable_input_max_length)

    def decrypt(self, inp: bytes) -> bytes:

        for i in range(len(inp)):
            inp[i] = inp[i] ^ self._keystore[i % 256]

        progress = 0
        decr_bytes = []

        indices = list(range(256))

        for b in inp:
            assert 0 <= b <= 255

            decr_bytes.append(indices[self._keys.index(b)])

            progress += 1
            percent = '{:.2%}'.format(progress / len(inp))
            print(f"Decrypted {progress} bytes of {len(inp)} total. [{percent}%]", end='\r')

        print('\n\nDone.\n')
        decr_bytes=bytes(decr_bytes)

        sep_iloc = decr_bytes.find(SEP)
        if sep_iloc != -1:
            decr_bytes=decr_bytes[:decr_bytes.find(SEP)]
        return decr_bytes

    def decrypt_file(self, path: str) -> bytes:
        with open(path, "rb") as f:
            return self.decrypt(f.read())
