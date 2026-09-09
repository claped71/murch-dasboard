"""MV: correct the 12B termination count and publish the junction-box side.

Source: Sep 8 MV Termination Production Control, Breakdown tab (46 units - 23
inverters + 23 MVJBs). Anchored replaces; any drift exits non-zero and the
workflow commits nothing. Hashes checked afterwards against expected.sha256.

RULE: any commit that changes data.js must bump the ?v= on its script tag in the
same commit, or browsers keep serving the cached old file.
"""
import io, sys


def sub(s, old, new, what):
    if s.count(old) != 1:
        sys.exit('ANCHOR FAILED (%d matches): %s' % (s.count(old), what))
    return s.replace(old, new, 1)


d = io.open('data.js', encoding='utf-8').read()

d = sub(d,
    "By line: 11A inverter-side 24 of 24 done, 11A junction boxes 0 of 30; 11B inverter-side 18 of 30, boxes 0 of 42; 12A and 12B at zero.",
    "<strong>The 264 split 114 inverter-side + 150 box-side, and every one of the 45 completed is inverter-side: "
    "NOT ONE TERMINATION HAS BEEN MADE ON ANY OF THE 23 MV JUNCTION BOXES — 0 of 150, 57% of the scope untouched on all four lines.</strong> "
    "By line (inverter-side / box-side): <strong>11A 24 of 24 ✔ / 0 of 30</strong>; 11B 18 of 30 / 0 of 42; 12A 0 of 30 / 0 of 39; "
    "<strong>12B 3 of 30 (INV-15) / 0 of 39</strong>. The 23 junction boxes are one per power block — 5 on 11A, 6 each on 11B, 12A and 12B; "
    "Topland is still distributing them and installation has not started.",
    'MV terminations component note')

d = sub(d,
    "11A inverter-side is done (24 of 24) but every MV junction box on the project is at zero (0 of 30 on 11A, 0 of 42 on 11B); 11B inverter-side 18 of 27 with INV-13 and INV-14 untouched; 12A and 12B at zero.",
    "11A inverter-side is done (24 of 24) but <strong>every one of the 23 MV junction boxes on the project is at zero — 0 of 150 box-side terminations</strong> "
    "(0 of 30 on 11A, 0 of 42 on 11B, 0 of 39 on 12A and on 12B); 11B inverter-side 18 of 30 with INV-13 and INV-14 untouched; 12A at zero and 12B 3 of 30 (INV-15).",
    'MV chain risk note')

d = sub(d,
    " L4: { harness: 0, boxes: 0, homerun: 0, trunk: 0, connInv: 0, connBox: 0, connMV: 0 },",
    " L4: { harness: 0, boxes: 0, homerun: 0, trunk: 0, connInv: 0, connBox: 0, connMV: 3 },",
    'lineas L4 connMV')
io.open('data.js', 'w', encoding='utf-8').write(d)

h = io.open('index.html', encoding='utf-8').read()
OLD = '<script src="data.js?v=20260909f"></script>'
if h.count(OLD) != 1:
    sys.exit('ANCHOR FAILED (%d matches): data.js script tag' % h.count(OLD))
io.open('index.html', 'w', encoding='utf-8').write(
    h.replace(OLD, '<script src="data.js?v=20260909g"></script>', 1))

print('MV junction-box side published; 12B corrected to 3; cache-buster 20260909g')
