#!/usr/bin/env python3
"""HALLMARK.FAMILY.001 — private code-only BCC stages 2/3/4/E.
No artwork, image bytes, original master, or external publishing.
"""
import hashlib
import json
from pathlib import Path

IDENTITY = {"project": "HALLMARK.FAMILY.001", "recipient": "Kourtney", "family": ["Richard", "Kourtney", "Nolan"]}
MESSAGE = "I went searching for answers. I came home to love."
TRIT_ROWS = ("0120", "1201", "2012")
STAGES = ("2.identity", "3.encoding", "4.provenance", "E.verify")

def encode_byte(value):
    if not 0 <= value <= 255:
        raise ValueError("8-bit byte out of range")
    out = []
    for _ in range(12):
        value, rem = divmod(value, 3)
        out.append(str(rem))
    return "".join(reversed(out))

def decode_trits(trits):
    if len(trits) != 12 or any(c not in "012" for c in trits):
        raise ValueError("expected exactly 12 base-3 digits")
    value = int(trits, 3)
    if value > 255:
        raise ValueError("12-trit value is not an 8-bit byte")
    return value

def build_receipt():
    source = MESSAGE.encode("utf-8")
    encoded = [encode_byte(b) for b in source]
    assert bytes(decode_trits(t) for t in encoded) == source
    assert len(TRIT_ROWS) == 3 and all(len(r) == 4 and set(r) <= set("012") for r in TRIT_ROWS)
    assert all(decode_trits(encode_byte(b)) == b for b in range(256))
    return {
        "schema": "hallmark.family.001.code-receipt.v1",
        "identity": IDENTITY,
        "stages": STAGES,
        "message": MESSAGE,
        "bcc_display_rows": list(TRIT_ROWS),
        "bcc_display_is_message_encoding": False,
        "byte_encoding": "unsigned byte, 12-trit zero-padded base-3, most-significant trit first",
        "message_utf8_hex": source.hex(),
        "message_utf8_sha256": hashlib.sha256(source).hexdigest(),
        "message_byte_count": len(source),
        "message_byte_trits": encoded,
        "verification": {
            "utf8_round_trip": "PASS",
            "all_256_byte_round_trips": "PASS",
            "display_grid_syntax": "PASS",
            "independent_verification": "NOT PERFORMED",
            "image_verification": "NOT PERFORMED",
        },
        "origin_master": "UNCHANGED BY THIS SCRIPT",
        "publication": "NO PUBLICATION REQUESTED",
    }

if __name__ == "__main__":
    receipt = build_receipt()
    output = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    print(output, end="")
    print("receipt_sha256=" + hashlib.sha256(output.encode("utf-8")).hexdigest())
