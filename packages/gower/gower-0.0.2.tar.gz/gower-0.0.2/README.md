## Examples

```python
import numpy as np
import pandas as pd
import gower

Xd=pd.DataFrame({'age':[21,21,19, 30,21,21,19,30,None],
'gender':['M','M','N','M','F','F','F','F',None],
'civil_status':['MARRIED','SINGLE','SINGLE','SINGLE','MARRIED','SINGLE','WIDOW','DIVORCED',None],
'salary':[3000.0,1200.0 ,32000.0,1800.0 ,2900.0 ,1100.0 ,10000.0,1500.0,None],
'has_children':[1,0,1,1,1,0,0,1,None],
'available_credit':[2200,100,22000,1100,2000,100,6000,2200,None]})
Yd = Xd.iloc[1:3,:]
X = np.asarray(Xd)
Y = np.asarray(Yd)

```


```python
gower.gower_topn(Xd.iloc[0:2,:], Xd.iloc[:,], n = 5)
```




    {'index': array([4, 3, 1, 7, 5]),
     'values': array([0.16872811, 0.31787416, 0.3590238 , 0.47778758, 0.52622986],
           dtype=float32)}




```python
gower.gower_matrix(X)
```




    array([[0.        , 0.3590238 , 0.6707398 , 0.31787416, 0.16872811,
            0.52622986, 0.59697855, 0.47778758,        nan],
           [0.3590238 , 0.        , 0.6964303 , 0.3138769 , 0.523629  ,
            0.16720603, 0.45600235, 0.6539635 ,        nan],
           [0.6707398 , 0.6964303 , 0.        , 0.6552807 , 0.6728013 ,
            0.6969697 , 0.740428  , 0.8151941 ,        nan],
           [0.31787416, 0.3138769 , 0.6552807 , 0.        , 0.4824794 ,
            0.48108295, 0.74818605, 0.34332284,        nan],
           [0.16872811, 0.523629  , 0.6728013 , 0.4824794 , 0.        ,
            0.35750175, 0.43237334, 0.3121036 ,        nan],
           [0.52622986, 0.16720603, 0.6969697 , 0.48108295, 0.35750175,
            0.        , 0.2898751 , 0.4878362 ,        nan],
           [0.59697855, 0.45600235, 0.740428  , 0.74818605, 0.43237334,
            0.2898751 , 0.        , 0.57476616,        nan],
           [0.47778758, 0.6539635 , 0.8151941 , 0.34332284, 0.3121036 ,
            0.4878362 , 0.57476616, 0.        ,        nan],
           [       nan,        nan,        nan,        nan,        nan,
                   nan,        nan,        nan,        nan]], dtype=float32)




```python
def smallest_indices(ary, n):
    """Returns the n largest indices from a numpy array."""
    n += 1
    flat = np.nan_to_num(ary.flatten(), nan=999)
    indices = np.argpartition(-flat, -n)[-n:]
    indices = indices[np.argsort(flat[indices])]
    indices = np.delete(indices,0,0)
    values = flat[indices]
    return {'index': indices, 'values': values}
```


```python
out = smallest_indices(np.nan_to_num(aaa[1], nan=1),3)
```


```python
out
```




    {'index': array([5, 3, 0]),
     'values': array([0.16720603, 0.3138769 , 0.3590238 ], dtype=float32)}




```python
X[out['index'],:]
```




    array([[21.0, 'M', 'SINGLE', 1200.0, 0.0, 100.0],
           [21.0, 'F', 'SINGLE', 1100.0, 0.0, 100.0],
           [30.0, 'M', 'SINGLE', 1800.0, 1.0, 1100.0]], dtype=object)




```python
X
```




    array([[21.0, 'M', 'MARRIED', 3000.0, 1.0, 2200.0],
           [21.0, 'M', 'SINGLE', 1200.0, 0.0, 100.0],
           [19.0, 'N', 'SINGLE', 32000.0, 1.0, 22000.0],
           [30.0, 'M', 'SINGLE', 1800.0, 1.0, 1100.0],
           [21.0, 'F', 'MARRIED', 2900.0, 1.0, 2000.0],
           [21.0, 'F', 'SINGLE', 1100.0, 0.0, 100.0],
           [19.0, 'F', 'WIDOW', 10000.0, 0.0, 6000.0],
           [30.0, 'F', 'DIVORCED', 1500.0, 1.0, 2200.0],
           [nan, None, None, nan, nan, nan]], dtype=object)




```python
numpy.delete
```




    array([0.        , 0.3590238 , 0.6707398 , 0.31787416, 0.16872811,
           0.52622986, 0.59697855, 0.47778758,        nan], dtype=float32)




```python

```
