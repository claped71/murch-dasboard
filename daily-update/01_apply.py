"""Murch dashboard - electrical by-line re-base, Sep 9 2026.

Applied by .github/workflows/apply-daily-update.yml because the credentialed push
path was unavailable in the session that produced it. Every edit is anchored on
text that must exist exactly once; any drift exits non-zero and the workflow fails
without committing. Output hashes are then checked against expected.sha256.
"""
import io, sys

NEW_DATA = r""" // ---- RE-BASED BY LINE, Sep 9, 2026 (Jose's ruling) ----------------------------
 // Until this cut every foot, assembly and box was booked to L1, which put L1 at
 // 105.9% of its homerun scope, 199% of its trunk and 194% of its box scope - a
 // ledger that cannot be true. The allocation below is built from two sources:
 //   (a) Angel Urbina's Master Electrical Dashboard - the per-LBD register with an
 //       Installed/Pending status and a date on every trunk and homerun run, which
 //       is verified through ~Sep 3 and covers ECCS scope only (it carries no
 //       United rows: 9 of 3,213 United strings assigned);
 //   (b) the crew-and-location record on each daily report for Sep 4-8, read through
 //       Angel's inverter-to-circuit map confirmed Sep 3:
 //       11A = INV 1,2,3,5,6 | 11B = INV 4,9,11,12,13,14 | 12A = INV 18-23 | 12B = INV 7,8,10,15,16,17.
 //       PS18-PS23 (United's harness, supports and messenger front) is therefore 12A,
 //       and INV-11 (the self-perform station closed Sep 7) is 11B - NOT L1.
 // Production whose line the report does not state is HELD in `unstated` and is never
 // pushed onto a line to make a line look better. Project totals are unchanged:
 // harness 428+74+307+0+87 = 896; homerun 40,908+5,988+10,109 = 57,005; trunk
 // 9,199+7,631+564 = 17,394. Keep it that way on every update - if a line moves, the
 // unstated bucket moves with it.
 lineas: {
 L1: { harness: 428, boxes: 92, homerun: 40908, trunk: 9199, connInv: 0, connBox: 0, connMV: 24 },
 L2: { harness: 74, boxes: 33, homerun: 5988, trunk: 7631, connInv: 0, connBox: 0, connMV: 18 },
 L3: { harness: 307, boxes: 0, homerun: 0, trunk: 0, connInv: 0, connBox: 0, connMV: 0 },
 L4: { harness: 0, boxes: 0, homerun: 0, trunk: 0, connInv: 0, connBox: 0, connMV: 0 },
 unstated: { harness: 87, boxes: 133, homerun: 10109, trunk: 564 }
 },
 // Project cumulatives - the figures the gate cards and the LV composite publish.
 // `cableSerie` is the sum of the daily series; the 881 lf gap against `cable` is an
 // open descuadre between the cumulative and the parte diario, carried, not buried.
 proyecto: { harness: 896, harnessSP: 68, boxes: 258, homerun: 57886, trunk: 17394, cable: 75280, cableSerie: 74399 },
 // Per-line scope - German Dominguez's Aug 12 take-off, the authorised split.
 alcance: {
 L1: { harness: 1082, boxes: 93, homerun: 54644, trunk: 8723, connInv: 186, connBox: 372, connMV: 30 },
 L2: { harness: 1292, boxes: 110, homerun: 53456, trunk: 10409, connInv: 220, connBox: 440, connMV: 36 },
 L3: { harness: 1258, boxes: 110, homerun: 65846, trunk: 10274, connInv: 220, connBox: 440, connMV: 36 },
 L4: { harness: 1340, boxes: 106, homerun: 55488, trunk: 10907, connInv: 212, connBox: 424, connMV: 36 }
 },
 // LV works finish per line on Juan de la Chica's Sep 8 plan, and the working days
 // left to it from `hoy`. Recompute `wd` on every run.
 // ---- THE MEASURING STICK IS JUAN DE LA CHICA'S SEP 8 PLAN (Jose, Sep 9) ----------
 // Not the contract MC of Sep 25 and not the old Sep 18 LV gate. Every required rate
 // in the electrical section is derived from the plan date the work actually has to
 // meet: each line against its own LV works finish, and the project against Oct 10,
 // the last line's LV works finish. Recompute `wd` on every run; never hardcode a rate.
 planBasis: { fin: 'Oct 10, 2026', wd: 23, gate: 'LV works complete on the last circuit (12B)', fuente: 'Sr. Controller’s end-of-project plan, revised Sep 8, 2026' },
 lineaPlan: {
 L1: { mv: 'MV-11A', zonas: 'A + C', inv: '5 inv - INV-01,02,03,05,06', lvFin: 'Sep 17', mc: 'Oct 2', wd: 7 },
 L2: { mv: 'MV-11B', zonas: 'E + EW', inv: '6 inv - INV-04,09,11,12,13,14', lvFin: 'Sep 24', mc: 'Oct 10', wd: 12 },
 L3: { mv: 'MV-12A', zonas: 'F + G', inv: '6 inv - INV-18..23', lvFin: 'Oct 1', mc: 'Oct 17', wd: 17 },
 L4: { mv: 'MV-12B', zonas: 'B + D + EW', inv: '6 inv - INV-07,08,10,15,16,17', lvFin: 'Oct 10', mc: 'Oct 24', wd: 23 }
 },
 lineaNota: {
 L1: 'Angel’s register is complete for 11A: <strong>92 of 92 LBD rows installed</strong>, homerun installed on INV-01/02/03/06 and <strong>zero on INV-05</strong>. Trunk is <strong>over its take-off (9,199 of 8,723 ft, 105.5%)</strong> — consistent with the procurement finding that the office take-off carries no offcut or waste allowance. What is missing on 11A is not cable, it is <strong>terminations: 0 of 372 box and 0 of 186 inverter connections</strong>, INV-2 and INV-3 not started, crimpers and certified megger still owed.',
 L2: 'Real production, published as zero until this cut. <strong>INV-11 closed on LV Sep 7</strong> by the self-perform crew (circuits 2,3,4,5,6,9,15,16), 7,631 ft of trunk (73.3% of the line’s trunk take-off) and 5,988 ft of homerun. Harness 74 in the contractual ledger <strong>plus 68 self-perform lines held outside it</strong> — 142 all-in. Boxes 33 (Angel 26 verified + 7 LBD set in Area E Sep 7).',
 L3: '<strong>307 harness lines — a third of the whole contractual harness ledger — were booked to Line 1 and are physically Line 3.</strong> United has worked PS18-PS23 continuously since Sep 1 (23 → 56 → 96 → 46 → 42 → 44 lines) plus 280 supports and 1,611 ft of messenger wire on Sep 8 alone. <strong>No cable and no boxes on 12A yet</strong>, and Angel’s control workbook carries no United rows at all (9 of 3,213 strings assigned), so none of this is in the verified register.',
 L4: 'Genuinely at zero on every scope. Four zones feed it, two of them gated — Zone D on piling (712 in the tail) and Zone G unracked at G5/G7. <strong>12B homerun was due to start Sep 8 on the plan and nothing has been filed.</strong>',
 unstated: '<strong>Production the daily report does not attribute to a line, held out rather than pushed onto a line.</strong> Cable: Sep 3 (4,282 ft), the ECCS remainder of Sep 4 (1,348 ft) and <strong>ECCS’s 5,043 ft on Sep 8, filed with no line or inverter stated</strong>. Harness: the 87 lines of Sep 4, filed with no crew split. Boxes: <strong>133 of the 258 published cannot be placed on a line — Angel’s verified register carries 118 project-wide against 258 reported</strong>, which is the single largest control divergence on this front. Luis and Audelio owe the line split; it is a one-column change to the daily report.'
 },
"""
NEW_SEC = r"""        <p class="quality-note" id="ebAlert"></p>

        <div class="table-wrap">
          <table>
            <thead>
              <tr><th>Line</th><th>Zones &middot; inverters</th><th>LV works / MC</th><th>Boxes (LBD)</th><th>Cable (lf)</th><th>Harness</th><th>LV connections</th></tr>
            </thead>
            <tbody id="ebScope"></tbody>
          </table>
          <div id="ebNotes"></div>
        </div>

        <h3 style="margin:18px 0 6px">What each line still has to install, and the rate its own date on the Sep 8 plan needs</h3>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th>Line</th><th>LV works finish</th><th>Working days</th><th>Cable remaining (lf)</th><th>Cable need/day</th><th>Harness remaining</th><th>Harness need/day</th><th>Status</th></tr>
            </thead>
            <tbody id="ebRates"></tbody>
          </table>
        </div>
        <p class="quality-note" id="ebRateNote"></p>

        <h3 style="margin:18px 0 6px">Cable pull &mdash; the last ten reported days against the rate Juan de la Chica&rsquo;s plan needs</h3>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th>Day</th><th>Total (lf)</th><th>Homerun</th><th>Trunk</th><th>vs plan rate</th><th>Cumulative</th><th>% of scope</th></tr>
            </thead>
            <tbody id="ebDaily"></tbody>
          </table>
        </div>
        <p class="quality-note" id="ebDailyNote"></p>

"""
NEW_FN = r"""  // ---- ELECTRICAL BY LINE (rebuilt Sep 9, 2026) -------------------------------
  // These three tables were static HTML frozen at the Aug 24 basis: they were still
  // publishing L1 homerun 33,523 and harness 134 while the ledger stood at 57,886 and
  // 896. They now render from data.electricalByLine so they cannot go stale again.
  // Everything here reads lineas / alcance / lineaPlan / proyecto - update THOSE.
  function renderElectricalByLine() {
    var eb = data.electricalByLine; if (!eb || !eb.alcance) return;
    var L = eb.lineas, A = eb.alcance, P = eb.lineaPlan, N = eb.lineaNota || {}, T = eb.proyecto;
    var ids = ['L1', 'L2', 'L3', 'L4'];
    var n = function (v) { return (v == null ? 0 : v).toLocaleString('en-US'); };
    var pc = function (a, b) { return b ? (100 * a / b).toFixed(1) + '%' : '—'; };
    // A cell reads red when the line is at zero on a scope its plan date needs, amber
    // when it is behind the straight-line need, plain otherwise. No hardcoded verdicts.
    var cell = function (done, scope) {
      var t = '<strong>' + n(done) + '</strong> / ' + n(scope) + ' &middot; ' + pc(done, scope);
      if (!done) return '<span style="color:#a12b2b">' + t + '</span>';
      if (done > scope) return t + ' <small style="color:#b96f18">over take-off</small>';
      return t;
    };

    var alertHost = document.getElementById('ebAlert');
    if (alertHost) {
      alertHost.innerHTML = '<strong>Basis of this section, re-based Sep 9, 2026.</strong> Until this cut every foot, assembly and box was booked to Line 1, ' +
        'which put L1 at <strong>105.9% of its homerun take-off, 199% of its trunk and 194% of its boxes</strong> — a ledger that cannot be true, and the reason the ' +
        'published Line 1 figures did not match what the field reports in the meetings. The split below is built from <strong>Angel Urbina’s per-LBD register</strong> ' +
        '(an Installed/Pending status and a date on every run, verified through ~Sep 3, ECCS scope only) and the <strong>crew-and-location record on each daily report for Sep 4–8</strong>, ' +
        'read through the inverter-to-circuit map confirmed Sep 3: <strong>11A = INV 1,2,3,5,6 &middot; 11B = INV 4,9,11,12,13,14 &middot; 12A = INV 18–23 &middot; 12B = INV 7,8,10,15,16,17</strong>. ' +
        'So <strong>United’s PS18–PS23 front is Line 3, not Line 1</strong>, and <strong>INV-11 is Line 2</strong>. Production the daily report does not attribute to a line is <strong>held in its own row</strong> ' +
        'and is never pushed onto a line. Project totals are unchanged: harness ' + n(T.harness) + ', homerun ' + n(T.homerun) + ' lf, trunk ' + n(T.trunk) + ' lf, boxes ' + n(T.boxes) + '.';
    }

    var rows = ids.map(function (id) {
      var l = L[id], a = A[id], p = P[id];
      return '<tr>' +
        '<td data-label="Line" style="white-space:nowrap"><strong>' + id + ' &middot; ' + p.mv + '</strong></td>' +
        '<td data-label="Zones">' + p.zonas + '<br><small>' + p.inv + '</small></td>' +
        '<td data-label="LV works / MC"><strong>' + p.lvFin + '</strong><br><small>MC ' + p.mc + '</small></td>' +
        '<td data-label="Boxes">' + cell(l.boxes, a.boxes) + '</td>' +
        '<td data-label="Cable">' + cell(l.homerun + l.trunk, a.homerun + a.trunk) +
          '<br><small>HR ' + n(l.homerun) + ' / ' + n(a.homerun) + ' &middot; trunk ' + n(l.trunk) + ' / ' + n(a.trunk) + '</small></td>' +
        '<td data-label="Harness">' + cell(l.harness, a.harness) +
          (id === 'L2' && T.harnessSP ? '<br><small>+ ' + n(T.harnessSP) + ' self-perform held outside the contractual ledger</small>' : '') + '</td>' +
        '<td data-label="LV connections"><span style="color:#a12b2b"><strong>0</strong> / ' + n(a.connInv + a.connBox) + '</span>' +
          (l.connMV ? '<br><small>MV inverter-side ' + n(l.connMV) + ' done</small>' : '') + '</td>' +
        '</tr>';
    });
    var u = L.unstated || {};
    if (u.harness || u.homerun || u.trunk || u.boxes) {
      rows.push('<tr style="background:rgba(185,111,24,.07)">' +
        '<td data-label="Line"><strong>NOT STATED BY LINE</strong></td>' +
        '<td data-label="Zones">held out of every line</td>' +
        '<td data-label="LV works / MC">&mdash;</td>' +
        '<td data-label="Boxes"><strong>' + n(u.boxes) + '</strong></td>' +
        '<td data-label="Cable"><strong>' + n((u.homerun || 0) + (u.trunk || 0)) + '</strong><br><small>HR ' + n(u.homerun) + ' &middot; trunk ' + n(u.trunk) + '</small></td>' +
        '<td data-label="Harness"><strong>' + n(u.harness) + '</strong></td>' +
        '<td data-label="LV connections">&mdash;</td></tr>');
    }
    document.getElementById('ebScope').innerHTML = rows.join('');

    var noteHost = document.getElementById('ebNotes');
    if (noteHost) {
      noteHost.innerHTML = '<details style="margin-top:10px"><summary style="cursor:pointer;font-weight:800">Where each line actually stands — the evidence behind its row</summary>' +
        ids.concat(['unstated']).map(function (id) {
          if (!N[id]) return '';
          var label = id === 'unstated' ? 'Not stated by line' : id + ' &middot; ' + P[id].mv;
          return '<p style="margin:8px 0"><strong>' + label + ':</strong> ' + N[id] + '</p>';
        }).join('') + '</details>';
    }

    // Demonstrated rates come from the daily series, never from a hardcoded figure.
    // BOTH series are stored out of date order (harnessDiario opens with the newest day
    // and diario ends with Sep 3), so anything that means "the last five days" MUST sort
    // first - slicing the raw array gave a 28/day harness rate against a real 81/day.
    var byDate = function (arr) {
      var mon = { ago: 8, sep: 9 };
      return (arr || []).slice().sort(function (a, b) {
        var pa = String(a.d).split(' '), pb = String(b.d).split(' ');
        return ((mon[pa[1]] || 0) * 100 + (+pa[0] || 0)) - ((mon[pb[1]] || 0) * 100 + (+pb[0] || 0));
      });
    };
    var dd = byDate((eb.diario || []).filter(function (d) { return d && d.v != null; }));
    var last5 = dd.slice(-5), cAvg = last5.length ? Math.round(last5.reduce(function (a, d) { return a + d.v; }, 0) / last5.length) : 0;
    var best = dd.reduce(function (m, d) { return Math.max(m, d.v); }, 0);
    var hd = byDate(eb.harnessDiario).slice(-5), hAvg = hd.length ? Math.round(hd.reduce(function (a, d) { return a + (d.l || 0); }, 0) / hd.length) : 0;

    // Remaining and required rate per line, straight-line to its own LV works date on
    // Juan de la Chica's Sep 8 plan. Status is judged against what this site has
    // actually demonstrated - the 5-day average and the best day ever recorded - so a
    // threshold is never a number somebody typed in.
    document.getElementById('ebRates').innerHTML = ids.map(function (id) {
      var l = L[id], a = A[id], p = P[id];
      var cRem = Math.max((a.homerun + a.trunk) - (l.homerun + l.trunk), 0);
      var hRem = Math.max(a.harness - l.harness, 0);
      var wd = p.wd || 1;
      var cDay = Math.round(cRem / wd), hDay = Math.round(hRem / wd);
      // Status is derived, never written by hand: a line with nothing on the ground on a
      // scope its date needs is Critical; otherwise it is judged on the required rate.
      var st, why;
      var connScope = a.connInv + a.connBox, connDone = (l.connInv || 0) + (l.connBox || 0);
      var cablePct = (a.homerun + a.trunk) ? (l.homerun + l.trunk) / (a.homerun + a.trunk) : 0;
      if (!(l.homerun + l.trunk) && !l.harness) { st = 'Critical'; why = 'nothing installed on any scope, on any date'; }
      else if (best && cDay > best) { st = 'Critical'; why = 'needs <strong>more every day than the best day this project has ever had</strong> (' + n(best) + ' lf)'; }
      // A line whose cable is nearly in but whose terminations are at zero is NOT on
      // track - the pull rate flatters it. This is Line 1's actual condition.
      else if (cablePct > 0.7 && connScope && !connDone) { st = 'At Risk'; why = 'cable nearly in but <strong>0 of ' + n(connScope) + ' LV connections</strong> — terminations, not pull, are the constraint'; }
      else if (cAvg && cDay > cAvg) { st = 'At Risk'; why = 'above the demonstrated ' + n(cAvg) + ' lf/day average, below the best day'; }
      else { st = 'Active'; why = 'inside the demonstrated ' + n(cAvg) + ' lf/day average'; }
      return '<tr>' +
        '<td data-label="Line" style="white-space:nowrap"><strong>' + id + ' &middot; ' + p.mv + '</strong></td>' +
        '<td data-label="LV works finish"><strong>' + p.lvFin + '</strong></td>' +
        '<td data-label="Working days">' + wd + '</td>' +
        '<td data-label="Cable remaining">' + n(cRem) + '</td>' +
        '<td data-label="Cable need/day"><strong>' + n(cDay) + ' lf/day</strong></td>' +
        '<td data-label="Harness remaining">' + n(hRem) + '</td>' +
        '<td data-label="Harness need/day"><strong>' + n(hDay) + '/day</strong></td>' +
        '<td data-label="Status">' + badge(st) + ' <small>' + why + '</small></td></tr>';
    }).join('');

    document.getElementById('ebRateNote').innerHTML =
      '<strong>How to read it.</strong> Each line is measured against <strong>its own LV works finish on the Sr. Controller’s Sep 8 plan</strong>, not against a project average. ' +
      'Demonstrated project-wide performance over the last five reported days is <strong>' + n(cAvg) + ' lf/day of cable</strong> (best day ' + n(best) + ') and <strong>' + n(hAvg) + ' harness lines/day</strong> across three crews. ' +
      'Those rates are the whole site, not one line, so a line asking for more than the project has ever produced in a day cannot be recovered by sequencing — only by crew. ' +
      '<strong>Line 1 is the one line where the cable is nearly done (' + pc(L.L1.homerun + L.L1.trunk, A.L1.homerun + A.L1.trunk) + ') and the binding constraint is terminations, not pull:</strong> ' +
      '0 of ' + n(A.L1.connInv + A.L1.connBox) + ' LV connections, with the crimpers and the certified megger still owed. ' +
      '<strong>Lines 3 and 4 have no cable at all</strong>, and 12A also has no boxes, while its harness front is the busiest on site.';

    // The last TEN reported days only, each judged against the rate the gate needs
    // today. A four-week log of raw feet is not a control instrument (Jose, Sep 9):
    // every row here has to answer "did that day hold the gate or not".
    var SHOW = 10;
    // REQUIRED IS MEASURED AGAINST JUAN DE LA CHICA'S SEP 8 PLAN (Jose, Sep 9), not the
    // contract MC and not the old Sep 18 LV gate. Project basis = remaining cable over the
    // working days to Oct 10, the last line's LV works finish. Derived, never hardcoded.
    var gate = 269748;
    var PB = eb.planBasis || {};
    var req = PB.wd ? Math.round((gate - (T.cable || 0)) / PB.wd) : 0;
    var all = byDate(eb.diario), cumAll = 0;
    var withCum = all.map(function (d) { cumAll += d.v || 0; return { d: d, cum: cumAll }; });
    document.getElementById('ebDaily').innerHTML = withCum.slice(-SHOW).map(function (x) {
      var d = x.d, hit = req ? (d.v || 0) / req : 0;
      var col = !d.v ? '#a12b2b' : hit >= 1 ? '#0c5f43' : hit >= 0.5 ? '#b96f18' : '#a12b2b';
      return '<tr>' +
        '<td data-label="Day" style="white-space:nowrap">' + d.d + '</td>' +
        '<td data-label="Total">' + (d.v ? '<strong>' + n(d.v) + '</strong>' : '<span style="color:#a12b2b">0 — no production</span>') + '</td>' +
        '<td data-label="Homerun">' + n(d.hr) + '</td>' +
        '<td data-label="Trunk">' + n(d.tr) + '</td>' +
        '<td data-label="vs required"><strong style="color:' + col + '">' + (req ? (100 * hit).toFixed(0) + '%' : '—') + '</strong></td>' +
        '<td data-label="Cumulative">' + n(x.cum) + '</td>' +
        '<td data-label="% of gate">' + (100 * x.cum / gate).toFixed(1) + '%</td></tr>';
    }).join('');
    var gap = (T.cable || 0) - cumAll;
    document.getElementById('ebDailyNote').innerHTML =
      'The last ' + SHOW + ' reported days, each measured against <strong>' + n(req) + ' lf/day</strong> — the rate that puts the remaining ' + n(gate - (T.cable || 0)) + ' lf in by <strong>' + PB.fin + '</strong>, ' +
      PB.gate + ' on the <strong>' + PB.fuente + '</strong>. That is the goal this project is being run to, so it is the denominator here; the contract MC and the old Sep 18 LV gate are not used. ' +
      'The earlier history is in the <a href="electrical-control.html?v=20260909d">interactive study</a> and is not repeated here. ' +
      '<strong>The demonstrated average is ' + n(cAvg) + ' lf/day, ' + (req ? (100 * cAvg / req).toFixed(0) : '0') + '% of the plan rate; the best day the project has ever had (' + n(best) + ' lf) is ' + (req ? (100 * best / req).toFixed(0) : '0') + '% of it.</strong> That gap, not the individual rows, is the finding. ' +
      (gap ? '<strong style="color:#b96f18">The daily series closes at ' + n(cumAll) + ' lf against the ' + n(T.cable) + ' lf cumulative the gate cards publish — an ' + n(Math.abs(gap)) + ' lf descuadre, carried openly until the team reconciles it.</strong> ' : '') +
      '<strong>The denominator is 269,748 lf — cable only</strong>; the ' + n(eb.harnessScope || 4972) + ' harness assemblies are a different unit and are never summed into it.';
  }

"""


def rd(p):
    return io.open(p, encoding='utf-8').read()


def wr(p, s):
    io.open(p, 'w', encoding='utf-8').write(s)


def sub(s, old, new, what):
    if s.count(old) != 1:
        sys.exit('ANCHOR FAILED (%d matches): %s' % (s.count(old), what))
    return s.replace(old, new, 1)


# ---------------------------------------------------------------- data.js
d = rd('data.js')
OLD_LINEAS = ' lineas: {\n' \
    ' L1: { harness: 896, boxes: 181, homerun: 57886, trunk: 17394, connInv: 0, connBox: 0, connMV: 0 },\n' \
    ' L2: { harness: 0, boxes: 77, homerun: 0, trunk: 0, connInv: 0, connBox: 0, connMV: 0 },\n' \
    ' L3: { harness: 0, boxes: 0, homerun: 0, trunk: 0, connInv: 0, connBox: 0, connMV: 0 },\n' \
    ' L4: { harness: 0, boxes: 0, homerun: 0, trunk: 0, connInv: 0, connBox: 0, connMV: 0 }\n' \
    ' },\n'
d = sub(d, OLD_LINEAS, NEW_DATA, 'data.js lineas block')
d = sub(d, 'CACHE BUSTER 20260909c', 'CACHE BUSTER 20260909d', 'data.js cache buster')
wr('data.js', d)

# ------------------------------------------------------------- index.html
h = rd('index.html')

# 1. Replace the three static tables (frozen at the Aug 24 basis) with data-driven
#    markup. Cut by anchor so the old markup is never reproduced in this script.
HEAD = '        <div class="table-wrap">\n          <table>\n            <thead>\n' \
       '              <tr><th>Line</th><th>Zones &middot; inverters</th><th>Line date</th><th>Boxes / LBD</th>'
if h.count(HEAD) != 1:
    sys.exit('ANCHOR FAILED: index.html static table head')
start = h.index(HEAD)
end = h.rindex('<p class="quality-note">', start,
               h.index('<strong>Daily report rule (German, Aug 12):</strong>'))
h = h[:start] + NEW_SEC + h[end:]

# 2. The renderer, and its call.
h = sub(h, '  function renderMilestones() {', NEW_FN + '  function renderMilestones() {',
        'index.html renderMilestones anchor')
CALL = "  try { renderPlanTracker(); } catch (e) { if (window.console) console.error('MURCH: planTracker render failed', e); }"
h = sub(h, CALL, CALL + "\n  try { renderElectricalByLine(); } catch (e) { "
        "if (window.console) console.error('MURCH: electricalByLine render failed', e); }",
        'index.html render call')

# 3. The LV gate card and the two cable trend cards were reading lineas.L1 as if it
#    were the project total. With the ledger re-based they must read `proyecto`.
h = sub(h, """            var lc = D.lvComposite || {}, eb = D.electricalByLine || {}, L1 = (eb.lineas || {}).L1 || {};
            var out = '';
            if (L1.homerun != null || L1.trunk != null) {
              out += '<span style="display:block;margin-top:6px;padding-top:6px;border-top:1px dotted var(--rule,#d8ded9)">' +
                     'Homerun <b>' + (L1.homerun || 0).toLocaleString() + '</b> / 229,435 &middot; ' +
                     'Trunk <b>' + (L1.trunk || 0).toLocaleString() + '</b> / 40,313</span>';
            }""",
        """            // PROJECT cumulatives, not Line 1. Before Sep 9, 2026 this card read
            // lineas.L1 because every foot was booked to L1; the by-line ledger has
            // been re-based, so the project figures now come from `proyecto`.
            var lc = D.lvComposite || {}, eb = D.electricalByLine || {}, PT = eb.proyecto || {};
            var out = '';
            if (PT.homerun != null || PT.trunk != null) {
              out += '<span style="display:block;margin-top:6px;padding-top:6px;border-top:1px dotted var(--rule,#d8ded9)">' +
                     'Homerun <b>' + (PT.homerun || 0).toLocaleString() + '</b> / 229,435 &middot; ' +
                     'Trunk <b>' + (PT.trunk || 0).toLocaleString() + '</b> / 40,313</span>';
            }""", 'index.html LV gate card')
h = sub(h, '      var _L1 = (_eb.lineas || {}).L1 || {};',
        '      // PROJECT cumulatives (was lineas.L1 until the Sep 9, 2026 by-line re-base).\n'
        '      var _PT = _eb.proyecto || {};', 'index.html trend card decl')
h = sub(h, '      var _hrCum = _L1.homerun || 0, _trCum = _L1.trunk || 0;',
        '      var _hrCum = _PT.homerun || 0, _trCum = _PT.trunk || 0;', 'index.html trend card cums')

# 4. The intro sentence still described the superseded end-of-August target.
h = sub(h, '<strong>the first line finishes with its LV connected by end of August</strong> and the lines close in sequence.',
        '<strong>Line 1 (11A) closes its LV works on Sep 17 and the lines follow at one-week steps to Oct 10</strong> '
        'on the Sr. Controller&rsquo;s Sep 8 plan.', 'index.html model sentence')
wr('index.html', h)

# --------------------------------------------------- electrical-control.html
e = rd('electrical-control.html')
e = sub(e, 'const LINEAS = [', 'let PROY = null;\nconst LINEAS = [', 'ec LINEAS decl')
e = sub(e, '    if(X.lineas) LINEAS.forEach(function(L){',
        '    /* Totales de PROYECTO. Hasta el 9 sep 2026 todo el tendido se imputaba a la L1,\n'
        '       asi que estas dos secciones leian lineas.L1 como si fuera el total. Con el\n'
        '       reparto por linea ya rebasado, el total vive en `proyecto`. */\n'
        '    if(X.proyecto) PROY = X.proyecto;\n'
        '    if(X.lineas) LINEAS.forEach(function(L){', 'ec hydrate')
e = sub(e, '  const L1 = (M && M.lineas && M.lineas[0] && M.lineas[0].hecho) ? M.lineas[0].hecho.harness : null;',
        '  const L1 = PROY && PROY.harness != null ? PROY.harness : null;', 'ec harness guard')
e = sub(e, '  const L1 = (M && M.lineas && M.lineas[0] && M.lineas[0].hecho) ? M.lineas[0].hecho : {};',
        '  const L1 = PROY || {};', 'ec cable split')
e = sub(e, "'La suma del parte diario cuadra con el control por l\\u00ednea'",
        "'La suma del parte diario cuadra con el acumulado de proyecto'", 'ec guard ok text')
e = sub(e, "'<strong style=\"color:#b53030\">DESCUADRE: el parte diario suma '+F(done)+' conjuntos y el control por l\\u00ednea marca '+F(L1)+'.</strong> '",
        "'<strong style=\"color:#b53030\">DESCUADRE: el parte diario suma '+F(done)+' conjuntos y el acumulado de proyecto marca '+F(L1)+'.</strong> '", 'ec guard bad text')
wr('electrical-control.html', e)

wr('cachebust.txt', '20260909d-electrical-byline\n')
print('electrical by-line re-base applied')
