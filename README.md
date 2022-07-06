[![test](https://github.com/zschumacher/setlist-fm-client/actions/workflows/test.yml/badge.svg)](https://github.com/zschumacher/setlist-fm-client/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/setlist-fm-client/badge/?version=latest)](https://setlist-fm-client.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/zschumacher/setlist-fm-client/branch/main/graph/badge.svg?token=ZNUE1K18VD)](https://codecov.io/gh/zschumacher/setlist-fm-client)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# setlist-fm-client
`setlist-fm-client` is a python client for the  [setlist.fm REST API](https://api.setlist.fm/docs/1.0/index.html).

## Installation

### pip
```console
pip install setlist-fm-client
```

### poetry

```console
poetry add setlist-fm-client
```

## Help
See the [documentation](https://setlist-fm-client.readthedocs.io/en/latest/) for more details.


## Authentication
In order to authenticate to the setlist.fm REST API, you must [apply for an API key](https://www.setlist.fm/settings/api) 
(link for logged-in users only) - if you're not registered user yet, then 
[register first](https://www.setlist.fm/signup) (it's free).

Once you have your key, you can use it in the *setlist-fm-client* by setting the `SETLIST_FM_API_KEY` environment 
variable or by passing `api_key="xxx"` as a kwarg to any function (see [docs]()).


## Simple Example
*setlist-fm-client* is extremely easy to use.  By setting `serialize=True`, you get a pydantic model returned to you instead of
a `httpx.Response` object.

Below are examples of what the code looks like for both the sync and async apis.

### sync
```python
import setlist_fm_client

setlists = setlist_fm_client.get_artist_setlists(
    "0bfba3d3-6a04-4779-bb0a-df07df5b0558", api_key="xxx", serialize=True
)
print(setlists)
```

### async
```python
import asyncio 

import setlist_fm_client

async def main():
    setlists = await setlist_fm_client.get_artist_setlists(
        "0bfba3d3-6a04-4779-bb0a-df07df5b0558", api_key="xxx", serialize=True
    )
    print(setlists)

asyncio.run(main())
```

This will give you an `ArtistSetListResponse` object.


