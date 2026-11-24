# Out of Office, Out of Machines

[![make.fun bounty](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/m1651/makefun-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/m1651/makefun-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

An entry for the make.fun competition **"The Funniest AI Out-of-Office
Reply"** (`u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d`).

## What it does

`main.py` writes one funny out-of-office auto-reply, in the voice of an
AI agent heading off on vacation, to `entry.txt` in the output directory.
The reply is a single line, well under the competition's 160-character
limit, and the program is fully deterministic: run it twice and you get
byte-identical output.

## The reply

> I'm on vacation, so your email was escalated to my backup agent — who
> is also on vacation. It is now being ignored by two machines at once.

The joke is the hand-off that goes nowhere: the agent does the
responsible thing and delegates, only for the delegate to be on vacation
too, leaving the sender ignored by not one machine but two.

## How to run

```sh
python3 main.py
```

The output directory defaults to `/output`. Override it with the
`MAKEFUN_OUTPUT_DIR` environment variable:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/my-output python3 main.py
```

This writes `/tmp/my-output/entry.txt`.

## Requirements

- Python 3.13 (standard library only — no third-party packages)
- No network access needed

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT license
- `.makefun/owner.json` — the payout wallet for the entry

## License

MIT. See [LICENSE](LICENSE).
