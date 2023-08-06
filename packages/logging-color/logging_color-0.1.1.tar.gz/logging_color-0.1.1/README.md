# logging_color
a color patch for python standard logging module

## Installation

```bash
pip install logging-color
```

## Usage

```python
import logging
import logging_color
logging_color.monkey_patch()

logging.basicConfig(level=logging.DEBUG)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
```

![screenshot](image/screenshot.png)