```python
import numpy
import matplotlib 
import matplotlib.pyplot as plt

data = [
    [  -2, -1,  0,  1,  2],
    [  -1,  0,  0,  1,  1],
    [   0,  0,  0,  0,  0],
    [   1,  1,  0,  0, -1],
    [   2,  1,  0, -1, -2],
]

plt.figure()

plt.imshow(data)

plt.show()
```
[Source](/python/110_imshow.py)