# TCGE Game 001 — Saved canonical gameplay

Initial state: `2000 / 1222 / 0111`  
Target state: `0120 / 1201 / 2012`  
Budget: 8 adjacent vertical swaps.

| Move | Column | Swap rows |
|---|---:|---|
| 1 | 1 | 1 ↔ 2 |
| 2 | 1 | 2 ↔ 3 |
| 3 | 1 | 1 ↔ 2 |
| 4 | 2 | 1 ↔ 2 |
| 5 | 2 | 2 ↔ 3 |
| 6 | 2 | 1 ↔ 2 |
| 7 | 3 | 1 ↔ 2 |
| 8 | 4 | 2 ↔ 3 |

This is a **canonical computer-generated solution**, not evidence of a human gameplay session.

Local verifier reported E-VERIFY PASS: legal path, shortest path 8, and 1,296 reachable states. Re-run `python e_verify.py game_001.json` for independent reproduction.

WIN WIN WIN = valid path + shortest-path proof + independent replay.
