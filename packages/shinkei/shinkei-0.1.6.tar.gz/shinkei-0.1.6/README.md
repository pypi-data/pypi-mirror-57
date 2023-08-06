# shinkei

[![Pipeline Status](https://img.shields.io/gitlab/pipeline/PendragonLore/shinkei.svg)](https://gitlab.com/PendragonLore/shinkei/pipelines)
[![ReadTheDocs Status](https://img.shields.io/readthedocs/shinkei.svg)](https://readthedocs.org/projects/shinkei/)


A client library for [singyeong](https://github.com/queer/singyeong), a fully-dynamic, metadata-oriented service mesh.

For more info on how to configure and run a singyeong server visit the official repository previously linked.

The binaries for it are available on [docker](https://hub.docker.com/r/queer/singyeong).

### Credits

Special thanks to [amy (queer)](https://github.com/queer/) for creating and helping me understand singyeong and to
[Rapptz (Danny)](https://github.com/Rapptz) for the amazing docs addon and overall heavily inspiring this lib's design 
through [discord.py](https://github.com/Rapptz/discord.py).

## Installation

The library is available on PyPi so it can be installed through pip:

```bash
pip install shinkei -U
```

### Requirements

* Python 3.5.3+
* [websockets](https://github.com/aaugustin/websockets) 6.0
* [aiohttp](https://github.com/aio-libs/aiohttp) 3.3.0+

These should already be handled by ``pip``.

#### Optional

* [ujson](https://github.com/esnme/ultrajson) (For faster json encoding/decoding)
    - ``pip install shinkei[ujson] -U``

## Documentation

The documentation is available at [read the docs](https://shinkei.rtfd.io).
