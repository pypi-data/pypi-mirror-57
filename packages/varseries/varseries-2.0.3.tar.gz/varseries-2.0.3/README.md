# VarSeries
An utility to build and display variation series


## Some examples
```python3
from varseries import DiscreteVS, ContinuousVS

v = DiscreteVS([1, 1, 1.11, 1.23, 2, 2.3, 4, 5.1, 5.1, 5 ... 8])
v.draw_polygon()
print(v.vs)  # Variation series representation
print(v.acc_frequencies)  # Accumulated frequencies list
# etc.

v1 = ContinuousVS(
    [1, 1, 1.11, 1.23, 2, 2.3, 4, 5.1, 5.1, 5 ... 8],
    precision=4
    )
v1.draw_hist()
v.draw_cumulate()
print(v.mode)  # Mode of the variation series
# etc
```
