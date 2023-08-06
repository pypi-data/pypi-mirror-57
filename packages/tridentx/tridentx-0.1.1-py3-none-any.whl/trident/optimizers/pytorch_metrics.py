import os
import sys
import math
import torch
import torch.nn as nn

import torch.nn.functional as F
from torch.autograd import Variable
from functools import partial
import numpy as np
from ..backend.common import get_session,addindent,get_time_suffix,get_class
from ..backend.pytorch_ops import argmax

__all__ = ['accuracy','psnr','rmse']

# def accuracy(input, target,axis=1):
#     input_tensor=input.clone().detach()
#     target_tensor=target.clone().detach()
#     if input_tensor.dtype!=torch.int64:
#         input_tensor=argmax(input_tensor,axis).squeeze()
#     if target_tensor.dtype!=torch.int64:
#         target_tensor=argmax(target_tensor,axis).squeeze()
#     if input_tensor.shape!=target_tensor.shape:
#         raise  ValueError('input shape {0} is not competable with target shape {1}'.format(input_tensor.shape,target_tensor.shape))
#     else:
#         return input_tensor.eq(target_tensor).float().mean()


# 计算准确度



def accuracy(output, target, topk=1,axis=1):
    """Computes the precision@k for the specified values of k
    prec1, prec5 = accuracy(output.data, target, topk=(1, 5))
    """
    input_tensor=output.clone().detach()
    target_tensor=target.clone().detach()
    if input_tensor.dtype!=torch.int64 and topk==1:
        input_tensor=argmax(input_tensor,axis).squeeze()
    if target_tensor.dtype!=torch.int64:
        target_tensor=argmax(target_tensor,axis).squeeze()
    if input_tensor.shape!=target_tensor.shape and topk==1:
        raise  ValueError('input shape {0} is not competable with target shape {1}'.format(input_tensor.shape,target_tensor.shape))

    batch_size = target_tensor.size(0)
    if len(target_tensor.size())>=3 or topk==1:
        return input_tensor.eq(target_tensor).float().mean()
    else:
        _, pred = input_tensor.topk(topk, -1, True, True)
        pred = pred.t()
        correct = pred.eq(target_tensor.view(1, -1).expand_as(pred))
        res = []

        correct_k = correct[:topk].view(-1).float().sum(0, keepdim=True)
        return correct_k.mul_(1 / batch_size)



def rmse(output, target):
    """Computes the precision@k for the specified values of k
    prec1, prec5 = accuracy(output.data, target, topk=(1, 5))
    """
    input_tensor=output.clone().detach()
    target_tensor=target.clone().detach()


    if input_tensor.shape!=target_tensor.shape :
        raise  ValueError('input shape {0} is not competable with target shape {1}'.format(input_tensor.shape,target_tensor.shape))

    batch_size = target_tensor.size(0)
    error_sq = torch.sqrt_((input_tensor - target_tensor).pow(2).mean())
    return error_sq








def psnr(output, target):
    input_tensor = output.clone().detach()
    target_tensor = target.clone().detach()
    if input_tensor.shape != target_tensor.shape :
        raise ValueError(
            'input shape {0} is not competable with target shape {1}'.format(input_tensor.shape, target_tensor.shape))
    diff = input_tensor - target_tensor
    diff=diff ** 2.
    diff = diff.view(diff.size(0),-1).mean()
    return  10 * torch.log(255**2 / diff)/math.log(10)

