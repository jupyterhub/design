# JupyterHub Design

This repository contains branding guide and assets for the [JupyterHub] and [Binder] projects.

[JupyterHub] and [Binder] are subprojects of [Jupyter] supported by the [Jupyter Foundation], a project of [The Linux Foundation]. The branding guide and assets of [Jupyter] are available at [`jupyter/design` on GitHub](https://github.com/jupyter/design/).

## Assets

The `*.png` and `.*svg` files to used. They are generated using [`build-assets.py`](./build-assets.py).

### Binder

Assets of the [Binder] project are located in the [`assets/binder`](./assets/binder) directory.

### JupyterHub

Assets of the [JupyterHub] project are located in the [`src/jupyterhub`](./src/jupyterhub) directory.

## Source

The `.svg` files are provided for reproducibility. This files **must** only be consumed by [`build-assets.py`](./build-assets.py).

### Usage Requirements

- [Python](https://www.python.org/)
- [Inkscape](https://inkscape.org/)
- Myriad Pro from [`fontfen/myriad-pro` on GitHub](https://github.com/fontfen/myriad-pro)

  On GNU/Linux,

  ```bash
  mkdir -p ~/.local/share/fonts/myriad-pro
  git clone git@github.com:fontfen/myriad-pro.git
  cd myriad-pro
  cp *.ttf ~/.local/share/fonts/myriad-pro
  ```

### Usage

```bash
python build-assets.py --all
```

### Binder

Assets of the [Binder] project are located in the [`src/binder`](./src/binder) directory.

### JupyterHub

Assets of the [JupyterHub] project are located in the [`assets/jupyterhub`](./assets/jupyterhub) directory.

## Branding Guide

### Binder

#### Color Palette

| Color name    | Hexadecimal color codes |
| ------------- | ----------------------- |
| Binder Orange | `#f5a252`               |
| Binder Pink   | `#e66581`               |
| Binder Blue   | `#579aca`               |
| Grey          | `545454`                |

#### Typography

[Myriad](<https://en.wikipedia.org/wiki/Myriad_(typeface)>) Pro is used.

### JupyterHub

The JupyterHub brand follows the Jupyter branding guide.

#### Color Palette

| Color name       | Hexadecimal color codes |
| ---------------- | ----------------------- |
| Jupyter Orange   | `#F37626`               |
| Dark Grey        | `#4D4D4D`               |
| Medium Dark Grey | `#616161`               |
| Medium Grey      | `#757575`               |
| Grey             | `#9E9E9E`               |

#### Typography

[Myriad](<https://en.wikipedia.org/wiki/Myriad_(typeface)>) Pro is used.

[Binder]: https://jupyter.org/binder
[Jupyter]: https://jupyter.org/
[JupyterHub]: https://jupyter.org/hub
[Jupyter Foundation]: https://jupyterfoundation.org/
[The Linux Foundation]: https://www.linuxfoundation.org/
