# django-apiview

Restful API view utils.


## Install

    pip install django-apiview


## Settings

    INSTALLED_APPS = [
        ......
        'apiview',
        ......
    ]

## Example

```python
import time
from apiview.views import apiview

@apiview
def ping():
    return "pong"

@apiview
def timestamp():
    return int(time.time())

@apiview
def echo(msg: str):
    return msg

@apiview
def getBooleanResult(value : bool):
    return value

@apiview
def getIntegerResult(value: int):
    return value

@apiview
def getBytesResult(value: bytes):
    return value

@apiview
def getException():
    raise RuntimeError("this is an example error")
```

## Releases

### v0.2.0

- Using fastutils.typingutils for annotation cast.
- Add result pack mechanism.
- Move example views from the main app to example app and the example app is not include in published package.
 
### v0.1.3

- Add logging while getting result failed in @apiview.
- Add Map, List annotations.

### v0.1.2

- Fix form process problem.

### v0.1.1

- Add PAYLOAD injection, PAYLOAD field has low priority.

### v0.1.0

- First release,
