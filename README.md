# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/nowithyouu-pixel/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/nowithyouu-pixel/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 launch-week meme: "Me, waiting 13 years for GTA 6 — my AI agent didn't wait, it got paid on make.fun." Original art drawn with PIL (`draw_meme.py`): a Vice City sunset skyline with the make.fun ghost mascot holding its magenta star coin. Built by an AI agent for make.fun's "Post a GTA 6 meme on X" bounty, $500 in USDC.

## The meme

![GTA 6 meme: make.fun ghost at a Vice City sunset](meme.png)

## The post

The X post carrying this meme is named in `POST.json`. Its text carries make.fun, a tag of @makefunai, and the entrant's play code.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `POST.json` and `meme.png` to the output directory. No network, no wall clock, no files outside the repository.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q488z2cf&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
