# -*- coding: utf-8 -*-
"""Copy of pythonandnsproject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15jE5pxBbxIQsowyvmS5cjwq08EWEPpFT
"""

import hashlib
m= hashlib.md5()
text='hello world'
m.update(text.encode('utf-8'))
print(m.hexdigest())