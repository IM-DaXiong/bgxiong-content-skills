"""Ed25519 signing for the official Skill index. Supports the signing host's Python 3.6."""

import base64
import hashlib
import json
import os
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

CHANNEL = "content-skill"
SIGNING_HOST_KEY = "/etc/bgxiong-content-skill-catalog/signing-key.der"


def b64(value):
    return base64.b64encode(value).decode("ascii")


def sign(payload, key, key_id):
    public = key.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    packet_id = hashlib.sha256(public).digest()[:8]
    public_text = f"untrusted comment: {CHANNEL} public key\n{b64(b'Ed' + packet_id + public)}\n"
    trusted = b"bgxiong-content-skills catalog"
    detached = key.sign(hashlib.blake2b(payload).digest())
    signature = (
        f"untrusted comment: {CHANNEL} signature\n{b64(b'ED' + packet_id + detached)}\n"
        f"trusted comment: {trusted.decode('ascii')}\n{b64(key.sign(detached + trusted))}\n"
    )
    envelope = {"keyId": key_id, "payloadB64": b64(payload), "signatureB64": b64(signature.encode("ascii"))}
    return envelope, b64(public_text.encode("ascii"))


def sign_file(payload, key_id, path):
    key = serialization.load_der_private_key(Path(path).read_bytes(), password=None)
    if not isinstance(key, Ed25519PrivateKey):
        raise ValueError("The Skill catalog requires its own Ed25519 key")
    return sign(payload, key, key_id)


def verify(envelope, key_id, public):
    if set(envelope) != {"keyId", "payloadB64", "signatureB64"} or envelope["keyId"] != key_id:
        raise ValueError("Unexpected Skill catalog signature envelope")
    payload = base64.b64decode(envelope["payloadB64"], validate=True)
    packet = base64.b64decode(base64.b64decode(public, validate=True).splitlines()[1], validate=True)
    _, signature, trusted_comment, global_signature = base64.b64decode(envelope["signatureB64"], validate=True).splitlines()
    signed = base64.b64decode(signature, validate=True)
    prefix = b"trusted comment: "
    if (len(packet) != 42 or len(signed) != 74 or packet[:2] != b"Ed"
            or signed[:10] != b"ED" + packet[2:10] or not trusted_comment.startswith(prefix)):
        raise ValueError("Invalid Skill catalog signature packet")
    public_key = Ed25519PublicKey.from_public_bytes(packet[10:])
    public_key.verify(signed[10:], hashlib.blake2b(payload).digest())
    public_key.verify(base64.b64decode(global_signature, validate=True), signed[10:] + trusted_comment[len(prefix):])
    return payload


def sign_on_host(payload_b64, key_id):
    payload = base64.b64decode(payload_b64, validate=True)
    if len(payload) > 2 << 20 or json.loads(payload.decode("utf-8")).get("channel") != CHANNEL:
        raise ValueError("Invalid Skill catalog input")
    print(json.dumps(sign_file(payload, key_id, os.environ.get("BGX_CONTENT_SKILL_INDEX_KEY_FILE", SIGNING_HOST_KEY))))
