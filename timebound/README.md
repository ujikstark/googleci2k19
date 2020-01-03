# Why Numpy is Faster ?

<h3> Numpy is made by C(almost all)</h3>

<h4>we can try this code for comparing :</h4>

`import numpy as np
import timeit

a = list(range(1000))
b = np.array(range(1000))

print("Time only python : ", timeit.timeit("[i + 1 for i in a]", setup="from __main__ import a", number=100000))
print("Time with numpy : ", timeit.timeit("np.add(1,b)", setup="from __main__ import np, b", number=100000))`

<h4>and the result looks like this :</h4>

![Screenshot from 2020-01-03 04 28 15](https://user-images.githubusercontent.com/57621743/71716315-4c0cfd80-2de2-11ea-89b6-273719eb2064.png)

**you must be know C language is faster rather than north, wait that is GOT XD.
 C is faster rather than any language i think, so the numpy is made by C which is make the numpy faster.
 C is not check array index bounds and the numpy should be like that **
