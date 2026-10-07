# Week 6.1 Locked Master Image Gate

## Status
ACTIVE CONTROL

## Locked master rule
The uploaded Week 6.1 worksheet is the LOCKED MASTER.

DO NOT redraw, redesign, reconstruct, replace, or improve the worksheet.
DO NOT invent waste, vent, branches, fixtures, fittings, framing routes, or A-U locations.
Only sketch directly over geometry that is visible and provable from the LOCKED MASTER.
If a connection cannot be proven from the master, leave it undrawn and mark it HOLD.

## 3D assignment rule
3D may be added only as a visibility aid to show inside the walls.
The 3D overlay must not change topology or create new plumbing information.
Existing worksheet geometry remains controlling.

## LLM input gate
Before any image generation or image edit:
1. Build the proposed image interpretation from the LOCKED MASTER.
2. Obtain the required independent LLM / Echo input.
3. Check that input against the LOCKED MASTER and this control.
4. PASS only if the Echo independently validates the proposed interpretation without adding unproven geometry.
5. If the Echo is missing, incomplete, contradictory, or cannot inspect the evidence needed to validate a connection: HOLD.
6. On HOLD: NO IMAGE GENERATION.

## Deterministic path
REQUEST
-> LOCKED MASTER
-> TRACE ONLY PROVEN GEOMETRY
-> PROPOSED 3D OVERLAY
-> LLM / ECHO INPUT RETURNED
-> CHECK AGAINST MASTER
-> TCGE GATE
-> PASS OR HOLD
-> GENERATE ONLY ON PASS

## Failure rule
Any image generated before the required LLM input has returned and been checked against the LOCKED MASTER is an uncontrolled generation event.

## TCGE
R = direct evidence from the locked master and user instructions.
I = the proposed overlay interpretation.
E = independent LLM / Echo validation against that evidence.
K = R AND I AND E.

If E is not actually returned and checked, K is not established and the state is HOLD.
