import os
import pytest
from tempfile import TemporaryDirectory
import random

import fileghost.fileghost as fg


def test_key_load() -> None:
    key1 = fg.keygen.generate()

    with TemporaryDirectory() as d:
        path = os.path.join(d, "key.json")
        key1.to_file(path)

        key2 = fg.keygen.from_file(path)

        assert key1._keys == key2._keys


def test_key_generates_unique() -> None:
    key1 = fg.keygen.generate()
    key2 = fg.keygen.generate()

    assert key1._keys != key2._keys


def test_invalid_key_creation() -> None:
    with pytest.raises(ValueError):
        fg.keygen([1, 2, 3])

    with pytest.raises(ValueError):
        fg.keygen([])

    with pytest.raises(ValueError):
        fg.keygen(list(range(257)))

    with pytest.raises(ValueError):
        fg.keygen(list(range(255)) + [1])


def test_encryption_roundtrip_a() -> None:
    key = fg.keygen.generate()

    data = b"Hello, world!"
    encrypted = key.encrypt(data)
    decrypted = key.decrypt(encrypted)

    assert data == decrypted


def test_encryption_roundtrip_b() -> None:
    key = fg.keygen.generate()

    # Create a random byte string of length 10_000
    random.seed(0)
    data = bytes((random.randint(0, 255)) for _ in range(10_000))
    encrypted = key.encrypt(data, disable_input_max_length=True)
    decrypted = key.decrypt(encrypted)

    assert data == decrypted
