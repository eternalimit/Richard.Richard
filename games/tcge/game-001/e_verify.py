#!/usr/bin/env python3
"""Independent TCGE Game 001 verifier; standard library only."""
import json,sys,collections,itertools,hashlib
from pathlib import Path
p=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('game_001.json'))
j=json.loads(p.read_text())
def board(x): return tuple(tuple(r) for r in x)
def step(x,c,r):
 y=[list(a) for a in x];y[r][c],y[r+1][c]=y[r+1][c],y[r][c];return board(y)
def moves(x):
 for c in range(4):
  for r in range(2):yield step(x,c,r)
start,target=board(j['initial_board']),board(j['target_board'])
assert target==((0,1,2,0),(1,2,0,1),(2,0,1,2))
assert all(sorted(x[r][c] for r in range(3))==[0,1,2] for x in (start,target) for c in range(4))
x=start
for m in j['solution_moves']:
 c,r=m['column_1_based']-1,m['upper_row_1_based']-1
 assert 0<=c<4 and 0<=r<2
 x=step(x,c,r)
assert x==target and len(j['solution_moves'])<=j['move_budget']
q=collections.deque([(start,0)]);seen={start};shortest=None
while q:
 x,d=q.popleft()
 if x==target:shortest=d;break
 for y in moves(x):
  if y not in seen:seen.add(y);q.append((y,d+1))
assert shortest==j['minimum_moves']==len(j['solution_moves'])==8
q=collections.deque([start]);seen={start}
while q:
 x=q.popleft()
 for y in moves(x):
  if y not in seen:seen.add(y);q.append(y)
assert len(seen)==j['reachable_states']==1296
print('E-VERIFY PASS | WIN 1, 2, 3 | shortest=8 | reachable_states=1296')
print('SHA-256:',hashlib.sha256(p.read_bytes()).hexdigest())
