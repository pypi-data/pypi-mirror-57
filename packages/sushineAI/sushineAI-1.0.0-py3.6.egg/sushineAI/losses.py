"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: losses.py
@time: 2019/12/16 16:31
@desc:
"""

import keras.backend as k


def rmse(y_true, y_pred):
    return k.sqrt(k.mean(k.square(y_pred - y_true), axis=-1))


def mse(y_true, y_pred):
    return k.mean(k.square(y_pred - y_true), axis=-1)


loss = {'rmse': rmse, 'mse': mse}
