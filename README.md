# Pixi Crispy Doom

This project showcases how to build [Crispy Doom](https://github.com/fabiangreffrath/crispy-doom) via [pixi](https://github.com/prefix-dev/pixi).
This makes the project completely standalone, and it doesnt require installing any dependencies since that is taken care of by pixi. The repository ships with a lock-file (`pixi.lock`) that contains information about the required depdendencies for different platforms.

To get started simply run:

```shell
pixi run start
```

> [!NOTE]
>
> Crispy Doom (or this repository) does not ship with any game files (WAD files), however, you can download a free version of Doom from https://freedoom.github.io/download.html.
> The `pixi run get-iwad` command is used to download the IWAD file automatically.

# What will pixi do for you?

Pixi is a package manager and workflow tool, this combiniation allows the users to only run a single command and pixi will take over the rest of the work.
On running `pixi run start`, pixi will
1. Install preperation environment
2. Initialize git submodles
3. Download IWAD files
4. Build the crispy doom cmake project
5. Run crispy doom with the IWAD file

You only need `pixi` and `git` on your machine to get started.
