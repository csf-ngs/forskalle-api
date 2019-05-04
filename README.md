# FSK API + cli

Python library for Fsk3 API. Will add functionality as needed.

## Installation

Install from the VBCF.NGS repository:

```
pip install git+https://ngs.vbcf.ac.at/repo/ngs-software/fsk-api.git
```

## Usage

### CLI

```
fsk-cli [command] [options] etc
```

Point it at your favorite Forskalle instance either by

- setting environment variables: `FSK_API_BASE` and `FSK_API_KEY`
- using a config file in `~/.fsk_api.yml`, please see [doc/](doc/) for an example

Try `fsk-cli --help` for some hints!

### Library

```
from forskalle_api import FskApi

fsk_api = FskApi()
sample_json = fsk_api.get_sample(54321)
```

There is no API-doc or similar, but we all love reading python source code!
