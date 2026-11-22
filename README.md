# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/tamarsmaile/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/tamarsmaile/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A 1024×1024 newspaper front page summing up 22 November 2026 world news, drawn by a Python program (Pillow + DejaVu fonts on the build workstation; the entry program itself is standard library only, no network).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=jad7ba0e&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>

---

Entry for the make.fun bounty **“Sum up 22 November's world news in one image”**
($100, shared by the 50 best-ranked entries): https://make.fun/bounty/news-image-20261122

## The image

`entry.png` is a 1024×1024 PNG newspaper front page — **“THE WORLD IN ONE
DAY — SUNDAY 22 NOVEMBER 2026”** — drawn with Pillow. It sums up the day's
world news, all events first reported on 22 November 2026:

1. **The Gulf (lead)** — Iran strikes a US air base in Kuwait and targets
   Bahrain as attacks widen across the Gulf; tankers hit off the Oman coast,
   blasts on Qeshm Island.
2. **The Baltic** — Drones hit a Russian cargo ship in the Gulf of Finland;
   Finland tightens security.
3. **Peru** — A magnitude 6.9 earthquake shakes the Andes; no damage or
   casualties reported at first.
4. **Climate / COP31** — Talks run into overtime with no final deal as
   nearly 200 countries split over fossil fuels.
5. **Mexico** — 'El Chapo Isidro', a fugitive on the FBI's Ten Most Wanted
   list, is captured in Sinaloa.
6. **Also today** — BepiColombo reaches Mercury after an 8-year voyage;
   Australia ends England's T20 winning streak; Leeds stun Chelsea 4–1.

## The program

`main.py` (Python 3, standard library only, no network) copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`),
as the kit's own starter does. The image is rendered by `render.py`, kept
outside this entry folder; it is not part of the submitted program.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verify

```sh
python3 -c "from PIL import Image; im=Image.open('out/entry.png'); print(im.format, im.size)"
ls -l out/entry.png   # 1024x1024, well under 1 MiB
```

## License

MIT — see [LICENSE](LICENSE).
