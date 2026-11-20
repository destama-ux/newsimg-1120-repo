# The World in One Day — Friday 20 November 2026: 34 verified stories

![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)
![rank](https://make.fun/badge/news-image-20261120/destama-ux/newsimg-1120-repo/rank.svg)
![reward](https://make.fun/badge/news-image-20261120/destama-ux/newsimg-1120-repo/reward.svg)

A make.fun entry for the **news-image-20261120** competition ("Sum up
20 November's world news in one image"). The judged artifact is a single
one-page newspaper image: `artwork.jpg`, a 1024×1024 JPEG presenting 34
verified stories from Friday 20 November 2026 — 13 illustrated panels, each
with a headline, a short summary and a source tag, plus 21 one-line briefs.
The page also carries a world map with numbered pins tied to the stories, a
big-number stat strip with the day's key figures, and a date-check box
confirming every story belongs to Friday 20 November 2026.

`page.html` is the page source the artwork was rendered from, and
`BUILD-NOTES.md` documents how the entry was researched and built.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is a small standard-library-only Python script. It checks that
`artwork.jpg` sits next to it and is a well-formed 1024×1024 JPEG, then
copies it byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (the output name
the competition kit expects) and re-reads the copy to confirm it is
byte-identical before reporting success.

## Sources

Every story was verified against real reporting of Friday 20 November 2026
from major wire services and international outlets (Reuters, AP, BBC,
Al Jazeera and similar); the illustrated stories carry their source tag on
the page itself.

## License

MIT — see `LICENSE`.
