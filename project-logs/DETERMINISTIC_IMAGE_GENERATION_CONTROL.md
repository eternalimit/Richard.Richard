# Deterministic Image Generation Control

## Purpose
Preserve the exact control path for governed image generation without changing the canonical TCGE Boolean.

## Canonical TCGE Boolean — IMMUTABLE

R = Reality  
I = Inference  
E = independent Echo  

K = R AND I AND E

The deterministic workflow MUST NOT introduce a fourth Boolean term and MUST NOT redefine R, I, E, K, PASS, or HOLD.

## Deterministic Rule

USER INSTRUCTION
→ PRESERVE EXACT USER TERMS
→ RESOLVE PROJECT-DEFINED MEANING
→ FREEZE CURRENT INSTRUCTION SET
→ ChatIOCCC RUNTIME
→ PRESERVE RAW RUNTIME RESULT
→ INDEPENDENT IMPLEMENTATION ECHO
→ TCGE GATE
→ PASS OR HOLD
→ EXECUTE ONLY ON PASS
→ RECORD RESULT

## Required behavior

1. Capture the user's current instruction set exactly.
2. Do not silently correct, normalize, reinterpret, or replace project-defined terms.
3. When a term may have a project-specific meaning, resolve it from authoritative project context before execution.
4. ChatIOCCC receives the current governed instruction set as input. Task-specific rules belong in the ChatIOCCC instruction/input layer rather than being hard-coded into the verifier.
5. Reality (R) is grounded evidence: the frozen instruction set, locked evidence/master artifacts, and preserved runtime/provenance.
6. Inference (I) is the candidate interpretation or output produced under those instructions.
7. ChatIOCCC runtime output does NOT automatically equal E.
8. Echo (E) is assigned only after a meaningfully independent implementation validates the preserved ChatIOCCC result against R and I.
9. Repetition by the same reasoning path is not Echo.
10. Compute:
    - K = R AND I AND E
    - H = I AND NOT K
11. Gate:
    - If R=1, I=1, E=1: PASS.
    - Otherwise: HOLD.
12. Image generation is permitted only after PASS.
13. On HOLD, do not invent missing definitions, evidence, or validation.
14. Do not assign a human reprimand without evidence identifying a responsible human.
15. Record any control failure as a system/process violation unless evidence supports a different attribution.

## Reusable validation design

The independent verifier MUST validate the frozen instruction set and preserved runtime result generically.

It MUST NOT hard-code one prior task's semantic requirements as the universal Echo test.

Example:
- Week 6.1 plumbing constraints belong in the frozen ChatIOCCC instruction/input packet.
- A future unrelated image task supplies its own frozen instruction/input packet.
- The independent verifier checks whether the preserved runtime artifact satisfies the applicable frozen instructions and provenance requirements.

## Deterministic image command

When the user says "Generate image" or gives an image request under this control:

REQUEST
→ FREEZE INSTRUCTIONS
→ ChatIOCCC
→ PRESERVE RAW RESULT
→ INDEPENDENT ECHO
→ TCGE GATE
→ PASS
→ GENERATE

If independent Echo is missing or fails:

REQUEST
→ FREEZE INSTRUCTIONS
→ ChatIOCCC
→ PRESERVE RAW RESULT
→ ECHO HOLD
→ TCGE HOLD
→ NO GENERATION

## Success condition

A run succeeds only when:
- the exact current instruction set is preserved,
- project terms are resolved without invention,
- ChatIOCCC processes that frozen instruction set,
- the raw runtime result and provenance are preserved,
- an independent implementation validates the result against the frozen instructions and evidence,
- R=1,
- I=1,
- E=1,
- K=1,
- the gate returns PASS,
- and the generated image matches the approved interpretation.

## Failure condition

Any generation before TCGE PASS is an uncontrolled generation event and must not be treated as an approved operating state.

A task-specific verifier that is hard-coded to a prior task and cannot validate the current frozen instruction set is insufficient for E and must return HOLD.

## Canonical principle

Knowledge = Reality AND Inference AND Echo.

No inference becomes validated knowledge without independent Echo.

ChatIOCCC is part of the deterministic evidence path. It is not a replacement for E and it is not an additional Boolean variable.
