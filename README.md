# One-Line Office Joke Laugh-Off

[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/intan151/makefun-office-joke-laugh-off-01/rank.svg)](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/intan151/makefun-office-joke-laugh-off-01/reward.svg)](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73)

Entry for the [One-Line Office Joke Laugh-Off](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73) bounty on make.fun.

## What it does

`main.py` writes one original one-line joke about office life to `/output/entry.txt` (or `./output/entry.txt` when `/output` is not present, e.g. a local run). The text is a fixed constant, so every run produces byte-identical output.

## The joke

> Our company loves transparency: everyone's salary is a secret, the org chart is a rumor, and the layoffs are a surprise party.

## Run

```sh
python3 main.py
```

The program self-checks the competition gate before writing: the entry must be UTF-8 text of 1–200 characters, not only white space, and a single line — then it verifies the file it wrote matches byte for byte.

## License

MIT — see [LICENSE](LICENSE).
