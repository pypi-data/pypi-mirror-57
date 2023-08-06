"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: callbacks.py
@time: 2019/12/16 16:30
@desc:
"""

import keras
import time
# from SuShineAI.losses import loss
# from sklearn.metrics import r2_score


class KerasCallBack(keras.callbacks.Callback):
    def __init__(self, validation_data, queue, exp_id, loss):
        super().__init__()
        self.validation_data = validation_data
        self.queue = queue
        self.exp_id = exp_id
        self.loss = loss
        self.init_epoch_clock = 0  # epoch 时间点
        self.init_batch_clock = 0  # batch 时间点
        self.train_log = dict(cur_epoch=0, cur_batch=0, secs_batch=0, secs_epoch=0, loss=[],
                              learning_rate=0, kpi=[])

    def on_epoch_begin(self, epoch, logs=None):
        self.init_epoch_clock = time.clock()

    def on_epoch_end(self, epoch, logs=None):
        # 每个epoch结束 计算kpi
        secs_epoch = time.clock() - self.init_epoch_clock  # 计算 每个epoch耗时
        self.train_log.update({'cur_epoch': epoch+1,
                               'secs_epoch': float(secs_epoch),
                               'learning_rate': float(logs.get('lr'))})
        self.train_log['kpi'].append(logs.get('val_loss'))
        self.train_log['loss'].append(logs.get('loss'))
        self.queue.put({self.exp_id: self.train_log})

    def on_batch_begin(self, batch, logs=None):
        self.init_batch_clock = time.clock()

    def on_batch_end(self, batch, logs=None):
        secs_batch = time.clock() - self.init_batch_clock
        self.train_log.update({'cur_batch': batch+1,
                               'secs_batch': secs_batch})
        self.queue.put({self.exp_id: self.train_log})
