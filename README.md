# Info

non-cohesive collection of python code. It's packaged and published together for my personal use.  

## La_edu

### matrix_to_ascii
```python-repl
>>> from la_edu.matrix_to_ascii import *
>>> import numpy as np
>>> array = np.arange(8)
>>> array = array.reshape((2,4))
>>> decorate(array)
'┌         ┐\n| 0 1 2 3 |\n| 4 5 6 7 |\n└         ┘'
>>> print(decorate(array))
┌         ┐
| 0 1 2 3 |
| 4 5 6 7 |
└         ┘
>>> array = array.reshape((4,2))
>>> print(decorate(array))
┌     ┐
| 0 1 |
| 2 3 |
| 4 5 |
| 6 7 |
└     ┘
>>> array = array.reshape((1,8))
>>> print(decorate(array))
┌                 ┐
| 0 1 2 3 4 5 6 7 |
└                 ┘
>>>

```