# Pixi Crispy Doom

This project showcases how to build [Crispy Doom](https://github.com/fabiangreffrath/crispy-doom) via [pixi](https://github.com/prefix-dev/pixi). 
This makes the project completely standalone, and it doesnt require installing any dependencies since that is taken care of by pixi. The repository ships with a lock-file (`pixi.lock`) that contains information about the required depdendencies for different platforms.

To get started simply run:

```shell
pixi run start --iawd <path to wad file>
```

> **Note**
>
> Crispy Doom (or this repository) does not ship with any game files (WAD files), however, you can download a free version of Doom from https://freedoom.github.io/download.html.
