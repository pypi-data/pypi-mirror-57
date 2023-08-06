# log

> pip install xlog


```python
from logext666 import xlog

xlog.file = 'logs/%Y-%m-%d.log'
xlog.level = 'info'
xlog.format = '%(levelname)s %(name)s %(user)s %(message)s'
xlog.file = '%Y-%m-%d.html'
xlog.debug({'foo': 'bar'}, indent=2)
xlog.info("hello", extra={'user': 'hanzhichao'})

```

output:
```
2019-12-09 19:30:16,419 DEBUG log None ->
{
  "foo": "bar"
}
2019-12-09 19:30:16,419 INFO log hanzhichao hello
```
