# Build notes — news-image-20261120
## "The World in One Day — Friday 20 November 2026"

One-page newspaper image (1024×1024 JPEG) summing up the world news of
Friday 20 November 2026. 34 stories, all six continents, 13 illustrated
panels + 21 one-line briefs, a UTC timeline strip, a six-stat number strip,
a coloured region bar, a world map with pins for stories 1–13, and a
forensic date-check box.

Modelled directly on the 19 Nov r2 package
(`~/workspace/makefun/entries/newsimg-1119-pkg-r2/`), which scored 983,928 /
prize_rank #413 (cutoff 989,112) — the strongest news-image formula we have:
giant date masthead, tiered stories (13 with summaries + source tags, the
rest as one-liners), big-number strip, coloured region bar, world map,
forensic date-check naming excluded other-days' news.

## Size discipline (tie-break lesson from 1119 r2)

The 1119 r2 file was 384,717 bytes and lost size tie-breaks among 68 tied
entries. This package's artwork is **282,675 bytes at JPEG quality 80**
(1024×1024, sha256
9f8816c91179f231f91c9cbdc9f57e97c271a5c378c2e522d90a3a5b0d97de37) — well under
300KB, comfortably inside the 1 MiB limit, with no visible loss of
legibility on inspection. Rendered from `page.html` with headless Chromium
(chrome-headless-shell, 1024×1024 viewport) and converted PNG→JPEG with
Pillow; quality 85 gave 320,296 bytes, quality 80 gave 282,675.

## Layout fit

The first render overflowed: document height 1,478px against the 1,024px
canvas (regions bar and timeline wrapped to two lines, summaries ran to
three lines, briefs wrapped). Fixed by measurement-driven trimming:
shortened every summary to two lines, every brief to one rendered line
(bold city prefix included in the count), shrank art heights (leads 92→78,
medium 46→42), and tightened paddings. Final measured document height is
exactly 1,024px; the full page (map, all 21 briefs, date-check, footer)
renders inside the frame — visually verified.

## Story list with sources (all reporting of Fri 20 Nov 2026)

Panels (13):
1. Cyclone Akvan landfall near Gopalpur, Odisha — 70–80 km/h, gusting 90;
   no major damage/deaths; third cyclone in a month. IMD / Reuters.
2. COP31 final day — no final text, talks into overtime Saturday; draft
   omits fossil fuels; Panama threatened formal objection. AP.
3. UK–EU reset deal signed in Brussels — youth mobility 100,000/yr each
   way, food-trade checks scrapped, carbon markets linked from 2028;
   tuition fees unresolved. Reuters.
4. Three Kyiv bridges hit in a major Russian missile attack; five killed.
   BBC.
5. Anthropic slides day two — pre-market $87.66, −9.8% vs $97.17 close;
   European shares head for worst week since March. Reuters / Finnhub.
6. US shutdown looms as Iran war splits Congress; Trump seeks $350bn
   Pentagon funding. Reuters.
7. Prabowo meets Xi in Beijing — economy, investment, South China Sea.
   Reuters.
8. Indonesia asks Google to justify removing 19,000+ pro-government
   YouTube channels. Reuters.
9. India busts opioid ring shipping ~500,000 tablets to US buyers via
   messaging apps; six arrested. Reuters.
10. Seoul appeals court upholds Kakao founder Kim Beom-su's acquittal on
    SM Entertainment share-rigging charges. Reuters / Yonhap.
11. Deutsche Bank leaks — bank forwarded Trump's tax return by mistake;
    ~$582m Epstein-linked transactions flagged; shares down >10% on the
    week. Reuters Breakingviews.
12. GTA VI — 24.6m copies, est. $2.36bn in 24 hours (Sensor Tower);
    Metacritic 99. NME / AsiaToday.
13. Pancreatic cancer pill trial saw tumours vanish. BBC.

Briefs (14–34): 14 Iraq forces enter Kataib Hezbollah stronghold (Reuters);
15 Democrats probe Nvidia's Megaspeed sway (Reuters); 16 Europe ready for
Russia talks on ending the war (BBC); 17 White House removes cyber-security
chief (BBC); 18 consent-law calls after Young case (BBC); 19 Airbnb house
rules in force (BBC); 20 UK fridges secured from hackers (BBC);
21 stockpiling lifts retail sales after 'Be Ready' (BBC); 22 UK coldest
night of autumn, −10C (BBC); 23 Russell fastest in wet Las Vegas GP
practice (BBC); 24 UFC bans Fiorot three months (BBC); 25 Rams' Nacua
suspended for misconduct (BBC); 26 Wales face Slovenia in March play-off
(BBC); 27 Prince Harry would rejoin the army (BBC); 28 William and Kate
meet Modi as India tour ends (BBC); 29 UK to send Ukraine 1,000
long-range strike drones (BBC); 30 France unrest may cost insurers
€207m (Euronews); 31 stabbed Bradford councillor 'protecting a staff
member' (BBC); 32 rand at one-year low amid coalition talks (Reuters);
33 Musk 'pretty foolish' over midterm spending (Reuters); 34 analysis:
Shenzhen summit masks each bilateral limit (Reuters Breakingviews).

Regions: Asia-Pacific 7 · Europe 15 · Middle East 1 · Africa 1 ·
Americas 6 · Global 4 = 34.

Stat strip: 70–80 km/h (Akvan winds) · 100,000 (UK–EU youth visas/yr) ·
$87.66 (Anthropic pre-market) · 19,000 (channels removed) · 24.6m (GTA VI
copies) · $2.36bn (day-one sales estimate).

UTC timeline (all times verified from source timestamps): 02:14 Seoul —
Kakao verdict (Reuters 02:14:42 UTC); 02:30 Gopalpur — landfall begins
(08:00 IST); 05:50 Gopalpur — landfall complete (11:20 IST); 08:05 London
— STOXX opens −1% (0805 GMT); 10:30 New York — ANT −4.7% pre-market
(1030 GMT); 13:38 New York — ANT $87.66 pre-market (Finnhub snapshot
13:38:20 UTC).

Date-check box names the excluded other-days' news: Anthropic's $97.17
first-day close and the ICJ Myanmar genocide verdict (both Thursday) ·
the Trump–Xi–Putin summit itself (Thursday) · GTA VI's launch (Thursday) ·
Korea's Suneung exam (Thursday) · the COP31 revised draft (Thursday).

## Date verification

20 November 2026 is a Friday, confirmed with the system date command
(`TZ=Asia/Jakarta date -d 2026-11-20` → Friday 2026-11-20 WIB).

## Weakest-sourced items (flagged honestly)

- Story 12's sales figures are a Sensor Tower *estimate*, not official
  Rockstar/Take-Two numbers — labelled as an estimate on the page.
- Story 5's pre-market figures come from Finnhub quote data ($87.66,
  −9.79% at 08:19 EST) and Sharecast's 10:30 GMT report (−4.7%, $92.60);
  the timeline uses both, at their own timestamps.
- Story 13 (cancer pill) rests on a single BBC headline item; no trial
  name or journal was in the copy read.
- The timeline's 02:30 UTC landfall start converts the IMD's "around
  8 am" IST bulletin; the 05:50 UTC completion converts the 11:20 IST
  bulletin.

## Production and verification (20 Nov 2026)

- `page.html` is the design document (same layout, headlines, summaries
  and briefs as the artwork). `artwork.jpg` was rendered from it with
  headless Chromium (1024×1024 viewport) → PNG → JPEG quality 80.
- Final artwork: JPEG, exactly 1024×1024, 282,675 bytes (limit 1 MiB),
  sha256 9f8816c91179f231f91c9cbdc9f57e97c271a5c378c2e522d90a3a5b0d97de37.
- Verified: `MAKEFUN_OUTPUT_DIR=/tmp/ni1120-out1 python3 main.py` exits 0
  twice; both outputs byte-identical to each other and to `artwork.jpg`
  (`cmp` clean). Story count: 3 lead + 10 medium panels + 21 briefs = 34;
  briefs numbered 14–34 continuously; region counts sum to 34.
- The render was visually inspected twice; fixes made across passes:
  layout overflow (1,478px → 1,024px), clipped SVG banner/text labels
  (Akvan, UK–EU, Prabowo–Xi, GTA VI, cancer pill), panel 7 headline and
  panel 12 summary wrapping to three lines, Union Jack redrawn properly.

## Status

- Package only. NOT bundled, NOT submitted, NO git repo created.
  Bundle + check + submit to be done from a fresh main-chat session
  under the new run-record rules.
