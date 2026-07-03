<div align="center">
  
  <img src="data/icons/io.github.tanaybhomia.Whisp.svg" alt="Whisp Icon" width="128" height="128" style="vertical-align: middle;"> 
  <h1>Whisp</h1>
  <p><b>The Anti-Note for GNOME. A fluid, gesture-driven scratchpad designed for speed.</b></p>

  <a href="https://flathub.org/apps/io.github.tanaybhomia.Whisp">
    <img src="https://flathub.org/api/badge?svg&locale=en" alt="Download on Flathub" height="50">
  </a>
  <a href="https://ko-fi.com/tanaybhomia">
    <img src="docs/assets/support_me_on_kofi_badge_red.png" alt="Support me on Ko-fi" height="50">
  </a>
  <br><br>
  
  <a href="#"><img src="https://img.shields.io/badge/Platform-GNOME-4A86CF?style=flat-square" alt="Platform: GNOME"></a>
  <a href="#"><img src="https://img.shields.io/badge/GTK-4.0-white?style=flat-square&logo=gtk" alt="GTK4"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-GPLv3-blue?style=flat-square" alt="License: GPLv3"></a>
  <a href="https://github.com/tanaybhomia/Whisp/stargazers"><img src="https://img.shields.io/github/stars/tanaybhomia/Whisp?style=flat-square&logo=github&color=gold" alt="GitHub Stars"></a>
  <a href="https://flathub.org/apps/io.github.tanaybhomia.Whisp"><img src="https://img.shields.io/flathub/downloads/io.github.tanaybhomia.Whisp?style=flat-square&logo=flathub&color=blue" alt="Flathub Downloads"></a>
  <br><br>
</div>

<div align="center">
  <img alt="Whisp Main Interface" src="docs/assets/1-hero.png" style="max-width: 100%; height: auto;" />
</div>


Whisp is a fast note-taking application built for the GNOME desktop environment. It replaces traditional file hierarchies with a spatial, swipeable canvas. Inspired by the "anti-note" philosophy, it acts as a quick desktop scratchpad with Markdown editing, built natively with GTK4 and Libadwaita.

## Why Whisp?

Most note-taking apps force you into a heavy workflow of creating files, managing folders, and hitting "Save". **Whisp is different.**
- **Zero Friction**: There are no titles to type, no files to name, and no folders to manage. Just open the app and start typing. 
- **Swipeable Canvas**: Instead of a sidebar of files, your notes exist in a spatial, horizontal carousel. A quick trackpad swipe instantly glides you to your next thought.
- **The "Anti-Note"**: Use it as a scratchpad. Jot down quick thoughts, paste temporary links, and when you're done, hit `Ctrl+D` to delete it forever and keep your desk clean.

## Core Features

- **Spatial Navigation**: Fluidly swipe between your recent notes using 1:1 touchpad gestures via Adwaita Carousel.
- **WYSIWYG Markdown**: Real-time rendering of Markdown. Toggle WYSIWYG mode to instantly hide Markdown syntax symbols and view clean rich text.
- **Paper Themes**: Native dynamic styling. Choose between Dotted, Grid, or Blank backgrounds to mimic physical engineering paper or scratchpads.
- **Smart Paste**: Copy a URL and press `Ctrl+V` to automatically shrink it via TinyURL in the background, or use `Ctrl+Shift+V` to extract and paste pure plain text, actively stripping all source Markdown formatting.
- **Keyboard-Centric Workflow**: 
  - `Ctrl+N` to instantly create a new note.
  - `Ctrl+B`, `Ctrl+I`, `Ctrl+U` for quick text formatting.
- **Performance Focused**: Renders only the most recently active notes to keep startup times fast.
- **File Management**: Search, filter by tags, and recover deleted files from a hidden `.trash` directory.


## Installation

Whisp is officially distributed through Flathub, making it easy to install on any Linux distribution.

```bash
flatpak install flathub io.github.tanaybhomia.Whisp
```

## Contribution & Development

If you'd like to contribute to Whisp or build your own version, we have set up scripts to make local development frictionless.

### Local Testing
You do not need to install the app or compile it with Meson just to test Python code changes. Run the following command in the project root to instantly launch the app from the source code:
```bash
./run.sh
```

### Development Environment Setup
If you want to use the official Flathub release for your daily notes, but also want a separate development version of Whisp in your app launcher for testing, run:
```bash
./install-dev.sh
```
This script creates a separate "Whisp (Development)" entry in your GNOME app grid. It uses a custom development icon and saves your test notes to a completely isolated folder (`~/.local/share/Whisp/`), keeping your official Flatpak notes safe. Any code changes you make in your IDE will instantly be reflected the next time you click the Development app icon.

## Architecture

Whisp follows the GNOME Human Interface Guidelines (HIG). It uses `Adw.Carousel` for its swipeable interface and uses a custom `Gtk.TextView` wrapper to parse and format Markdown text.


## License

Whisp is free and open-source software licensed under the **GNU General Public License v3.0** (GPL-3.0). See the [LICENSE](LICENSE) file for more details.

## Inspiration

Whisp was heavily inspired by the core workflow and design philosophy of **[Anti Note on macos](https://antinote.io/)**. I loved the concept of a distraction-free, "anti-folder" scratchpad, but since it wasn't available on Linux, I built Whisp to bring that exact experience natively to the GNOME ecosystem!

## Stargazers

Thank you to everyone who has starred the repository and supported the project!
<a href="https://www.star-history.com/?repos=tanaybhomia%2FWhisp&type=timeline&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=tanaybhomia/Whisp&type=timeline&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=tanaybhomia/Whisp&type=timeline&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=tanaybhomia/Whisp&type=timeline&legend=top-left" />
 </picture>
</a>


