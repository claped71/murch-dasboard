"""Apply the CM-workbook confirmations to the electrical by-line section.

data.js comes from byline2.patch (git apply - exact, fails loudly on any drift).
index.html needs only the cache-buster bump, done here as an anchored replace.

RULE: any commit that changes data.js must bump the ?v= on its script tag in the
same commit, or browsers keep serving the cached old file and the section renders
empty (renderElectricalByLine returns early when the new fields are absent).
"""
import io, subprocess, sys

r = subprocess.run(['git', 'apply', 'daily-update/byline2.patch'],
                   capture_output=True, text=True)
sys.stderr.write(r.stderr)
if r.returncode:
    sys.exit('PATCH FAILED: daily-update/byline2.patch did not apply')

h = io.open('index.html', encoding='utf-8').read()
OLD = '<script src="data.js?v=20260909d"></script>'
if h.count(OLD) != 1:
    sys.exit('ANCHOR FAILED (%d matches): data.js script tag' % h.count(OLD))
h = h.replace(OLD, '<script src="data.js?v=20260909e"></script>', 1)
io.open('index.html', 'w', encoding='utf-8').write(h)

print('CM workbook confirmations applied; cache-buster bumped to 20260909e')
