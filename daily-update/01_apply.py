"""Record the United Zones F/G explanation for the 133 unplaced boxes.

data.js comes from byline3.patch (git apply - exact, fails loudly on any drift).
index.html needs only the cache-buster bump, done here as an anchored replace.

RULE: any commit that changes data.js must bump the ?v= on its script tag in the
same commit, or browsers keep serving the cached old file and the section renders
empty (renderElectricalByLine returns early when the new fields are absent).
"""
import io, subprocess, sys

r = subprocess.run(['git', 'apply', 'daily-update/byline3.patch'],
                   capture_output=True, text=True)
sys.stderr.write(r.stderr)
if r.returncode:
    sys.exit('PATCH FAILED: daily-update/byline3.patch did not apply')

h = io.open('index.html', encoding='utf-8').read()
OLD = '<script src="data.js?v=20260909e"></script>'
if h.count(OLD) != 1:
    sys.exit('ANCHOR FAILED (%d matches): data.js script tag' % h.count(OLD))
h = h.replace(OLD, '<script src="data.js?v=20260909f"></script>', 1)
io.open('index.html', 'w', encoding='utf-8').write(h)

print('United F/G box explanation recorded; cache-buster bumped to 20260909f')
