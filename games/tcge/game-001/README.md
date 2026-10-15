# TCGE Game 001 — Three-Win Challenge

Richard Stein · All Rights Reserved · Public playable research prototype.

A proposed TCGE × TXGE game extension. ORIGIN.MASTER is not modified or disclosed.

## Start
```
2000
1222
0111
```
## Target
```
0120
1201
2012
```

## Play
Rows and columns use 1-based coordinates. One move swaps two vertically adjacent cells in a single column (rows 1 and 2, or rows 2 and 3). No horizontal swaps. Reach the target in **8 or fewer moves**.

## WIN WIN WIN
1. Player: reach the exact target with legal moves.
2. Strategy: prove that no solution takes fewer than 8 moves.
3. Evidence: run an independent verifier to check the moves and shortest-path proof.

`game_001.json` contains the canonical solution (spoiler). Run `python e_verify.py game_001.json` to replay and check it. The verifier uses BFS and enumerates all 1,296 reachable states.

The puzzle is a finite state-space game, **not** a Bitcoin transaction, real TXID, cryptographic hash inversion, or proof of greater complexity than Sudoku.

Original local game-data SHA-256 (private package variant): `396ad1a4415634d3accb041e1ca221f28a9a94c19bee80504ce66439b66e644e`. The public JSON is a separate redacted derivative; its bytes differ.

Public release authorized by owner. Private keys and private research files are excluded.
