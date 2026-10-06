# Claude Echo Repeater

Purpose: provide a real second-model Echo path for Richard.Richard.

Flow:

```
Richard.Richard
  -> grounded evidence packet
  -> candidate answer
  -> Anthropic Claude independent review
  -> PASS/HOLD Echo receipt
  -> Richard.Richard final synthesis
```

The Echo is not allowed to become knowledge by agreement alone. It must test the
candidate against the supplied evidence.

## Input

```json
{
  "objective": "What is being verified?",
  "evidence": [
    {"id": "E1", "claim": "direct evidence", "source": "provenance"}
  ],
  "candidate": "First-model answer"
}
```

## Run

Set `ANTHROPIC_API_KEY` in the execution environment, then:

```bash
python integrations/claude_repeater/repeater.py --input packet.json
```

Optional model override:

```bash
ANTHROPIC_MODEL=claude-sonnet-4-5 python integrations/claude_repeater/repeater.py --input packet.json
```

## Verify without network

```bash
python integrations/claude_repeater/repeater.py --self-test
```

Expected:

```json
{"self_test": "PASS"}
```

## TCGE

- R: inspected source evidence is supplied in the packet.
- I: a candidate answer exists.
- E: Claude independently evaluates the candidate against the evidence.
- K = R AND I AND E.
- Any unresolved dependency returns HOLD.

## Security

Never commit `ANTHROPIC_API_KEY`. Store it only as a secret in the runtime or
GitHub Actions secret store.
