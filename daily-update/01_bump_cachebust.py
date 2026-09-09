"""Bump the asset cache-busters on index.html.

The Sep 9 by-line re-base changed data.js and electrical-control.html but left
index.html still requesting `data.js?v=20260909c`. Every browser that had already
loaded the dashboard therefore kept serving the CACHED old data.js, which has no
`alcance` / `proyecto` / `lineaPlan` — and renderElectricalByLine() returns early
when those are missing, so the whole electrical section came up unchanged or empty.

Rule for every future update: if data.js changes, the ?v= on its script tag changes
in the same commit.
"""
import io, sys


def rd(p):
    return io.open(p, encoding='utf-8').read()


def wr(p, s):
    io.open(p, 'w', encoding='utf-8').write(s)


h = rd('index.html')

OLD = '<script src="data.js?v=20260909c"></script>'
if h.count(OLD) != 1:
    sys.exit('ANCHOR FAILED (%d matches): data.js script tag' % h.count(OLD))
h = h.replace(OLD, '<script src="data.js?v=20260909d"></script>', 1)

# The interactive study changed in the same re-base, so its links get the same bump.
n = h.count('electrical-control.html?v=20260820a')
if n < 1:
    sys.exit('ANCHOR FAILED: electrical-control.html links')
h = h.replace('electrical-control.html?v=20260820a', 'electrical-control.html?v=20260909d')

wr('index.html', h)
print('cache-busters bumped: data.js 1, electrical-control.html %d' % n)
