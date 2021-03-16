# FSK API + cli

Python library for Fsk3 API. Will add functionality as needed.

## Installation

Install from the VBCF.NGS repository:

```
pip install git+https://ngs.vbcf.ac.at/repo/software/forskalle-api.git
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

#### Examples

Set all sequenced samples of a multiplex to Ok:

```bash
fsk-cli get-multi M4711 | jq '.multiplex_samples[].sample_id' | \
  while read sample_id; do 
    fsk-cli set-sequencing-status $sample_id --status Ok
  done
```

In place editing with jq and updating:

```bash
# update all request lanes to status Ready
fsk-cli request R4711 get | \
  jq '.request_lanes[].status="Ready"' | \
  fsk-cli request R4711 update
```

### Library

```
from forskalle_api import FskApi

fsk_api = FskApi()
sample_json = fsk_api.get_sample(54321)
```

```
from forskalle_api import FskApi
from forskalle_api.auto.queryparams import IlluminaRunFilters
from forskalle_api.fsk_query import FskQuery

fsk_api = FskApi()
irf = IlluminaRunFilters(sequenced_after="2020-05-01")
q = FskQuery(filters=irf)
runs = fsk_api.get_runs_illumina(q)
```


There is no API-doc or similar, but we all love reading python source code!
