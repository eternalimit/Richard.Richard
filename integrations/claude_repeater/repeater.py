#!/usr/bin/env python3
"""Richard.Richard Claude Echo repeater.

Sends a grounded evidence packet plus a candidate answer to Anthropic Claude
for independent review. The result is an Echo input, not automatic knowledge.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")
ANTHROPIC_VERSION = "2023-06-01"

SYSTEM = """You are the independent Echo validator in Richard.Richard.
Evaluate the candidate against the supplied evidence. Do not merely agree.
Return JSON only with keys:
verdict: PASS|HOLD,
validated_claims: array of strings,
rejected_claims: array of strings,
missing_evidence: array of strings,
corrections: array of strings,
reason: string.
PASS means the material inference is independently supported by the evidence.
HOLD means evidence is missing, contradictory, or the candidate overreaches.
Never invent evidence."""

def build_user_message(packet):
    required = ("objective", "evidence", "candidate")
    missing = [k for k in required if k not in packet]
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))
    return json.dumps({
        "objective": packet["objective"],
        "evidence": packet["evidence"],
        "candidate": packet["candidate"],
        "tcge": "K = R AND I AND E; otherwise HOLD"
    }, ensure_ascii=False)

def call_claude(packet, api_key, model=DEFAULT_MODEL):
    body = {
        "model": model,
        "max_tokens": 1600,
        "temperature": 0,
        "system": SYSTEM,
        "messages": [{"role": "user", "content": build_user_message(packet)}],
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": ANTHROPIC_VERSION,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Anthropic HTTP {e.code}: {detail}") from e
    text = "".join(
        block.get("text", "")
        for block in data.get("content", [])
        if block.get("type") == "text"
    ).strip()
    try:
        review = json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError("Claude returned non-JSON output") from e
    if review.get("verdict") not in ("PASS", "HOLD"):
        raise RuntimeError("Claude returned invalid verdict")
    return {
        "provider": "anthropic",
        "model": data.get("model", model),
        "message_id": data.get("id"),
        "review": review,
    }

def self_test():
    packet = {
        "objective": "Verify a test candidate",
        "evidence": [{"id": "E1", "claim": "2 + 2 = 4", "source": "test fixture"}],
        "candidate": "2 + 2 = 4",
    }
    assert "objective" in build_user_message(packet)
    try:
        build_user_message({"objective": "x"})
        raise AssertionError("missing-field test failed")
    except ValueError:
        pass
    print(json.dumps({"self_test": "PASS"}))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", help="JSON packet path; defaults to stdin")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return
    raw = open(args.input, "r", encoding="utf-8").read() if args.input else sys.stdin.read()
    packet = json.loads(raw)
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise SystemExit("HOLD: ANTHROPIC_API_KEY is not set")
    print(json.dumps(call_claude(packet, key, args.model), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
