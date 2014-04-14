code-combat-downloader
====

The folks at [CodeCombat](http://codecombat.com) have [open-sourced](http://codecombat.com/legal) a lot of CodeCombat, but some of it is hard to pull down for yourself (particularly art and music). This repository exists to store tools for downloading CodeCombat assets for you to use on your own projects (after attributing them correctly and [following the terms of their license](http://creativecommons.org/licenses/by/4.0/)).

usage - downloading thangs
====

I've tested this on Python 2.7.2, and it has no external dependencies.

```shell
  git clone git@github.com:girasquid/code-combat-downloader.git
  cd code-combat-downloader
  python download-thangs.py
```

The downloader will store all of the thangs into a `thangs` directory, categorized by their thang.type on CodeCombat.