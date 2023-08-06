# bvr
BVR: Log like a Beaver

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version](https://badge.fury.io/py/bvr.svg)](https://badge.fury.io/py/bvr)
![GitHub](https://img.shields.io/github/license/doedotdev/bvr)

## Install
```
pip install bvr
```

### bvr decorators
- [bvr_start: log when a method starts](#bvr_start)
- [bvr_end: log when a method ends](#bvr_end)
- [bvr_start_end: log when a method starts and ends](#bvr_start_end)
- [bvr_rest_before: log and sleep before a method starts](#bvr_rest_before)
- [bvr_rest_after: log and sleep after a method ends](#bvr_rest_after)
- [bvr_time: log the amount of time a method takes](#bvr_time)
- [bvr_try: log and catch an exception](#bvr_try)
- [bvr_repeat: log and repeat a method](#bvr_repeat)
- [bvr_compose: compose multiple other bvr decorators on a single method](#bvr-compose)


### bvr_start 
log when a method starts

example:
```
from bvr import bvr_start

@bvr_start
def example_one():
    print("hello")
    return 3

example_one()
```

output:
```
STARTED | FUNCTION: example_one | ARGS: () | KWARGS: {}

hello
```


### bvr_end
log when a method ends

example:
```
from bvr import bvr_end

@bvr_end
def example_one():
    print("hello")
    return 3

example_one()
```

output:
```
hello

ENDED | FUNCTION: example_one | ARGS: () | KWARGS: {}
```

### bvr_start_end
log when a method starts and ends

example:
```
from bvr import bvr_start_end

@bvr_start_end
def example_one():
    print("hello")
    return 3

example_one()
```

output:
```
STARTED | FUNCTION: example_one | ARGS: () | KWARGS: {}

hello

ENDED | FUNCTION: example_one | ARGS: () | KWARGS: {} 
```

### @bvr_rest_before
log and sleep before a method starts

Coming Soon!

### @bvr_rest_after
log and sleep after a method ends

Coming Soon!

### @bvr_time
log the amount of time a method takes

Coming Soon!

### @bvr_try
log and catch an exception

Coming Soon!

### @bvr_repeat
log and repeat a method n times

Coming Soon!

### @bvr_compose
compose multiple other bvr decorators on a single method

Coming Soon!


## Tech Notes
- Langauges
    - Python
    - Bash
    - Markdown
- Quality
    - PyTest
    - Coverage
    - Pylint
- Automation
    - Github Actions
    - Travis CI
- Hosting
    - Test PyPi
    - Prod Pypi

