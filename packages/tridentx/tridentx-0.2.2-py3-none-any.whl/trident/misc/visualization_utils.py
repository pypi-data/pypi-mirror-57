import datetime
import tkinter
import matplotlib
import platform
if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from IPython import display,get_ipython

from scipy import ndimage
import pylab
import PIL
from PIL import Image
import cv2
import os
import pickle
import codecs
import glob
import math

from ..backend.common import get_time_suffix
from ..backend.image_common import *

__all__ = ['tile_rgb_images','loss_metric_curve']
def tile_rgb_images(*imgs, row=3,save_path=None,imshow=False):
    fig = plt.gcf()
    fig.set_size_inches(len(imgs) * 2, row * 2)
    plt.clf()
    plt.ioff()  # is not None:
    suffix=get_time_suffix()

    for m in range(row * len(imgs)):
        plt.subplot(row, len(imgs), m + 1)
        img = array2image((imgs[int(m % len(imgs))][int(m // len(imgs))]))
        plt.imshow(img, interpolation="nearest", animated=True)
        plt.axis("off")
    filename =save_path.format(suffix)
    plt.savefig(filename, bbox_inches='tight')
    if imshow==True:
        plSize = fig.get_size_inches()
        fig.set_size_inches((int(round(plSize[0]*0.75,0)), int(round(plSize[1]*0.75,0))))
        display.display(plt.gcf())
        #plt.show()



def loss_metric_curve(losses,metrics, legend=None,calculate_base='epoch',max_iteration=None,save_path=None,imshow=False):
    fig = plt.gcf()
    fig.set_size_inches(18, 8)
    plt.clf()
    plt.ioff()  # is not None:

    plt.subplot(2, 2,1)
    if isinstance(losses,dict):
        plt.plot(losses['total_losses'])
        plt.legend(['loss'], loc='upper left')
    elif  isinstance(losses,list):
        for item in losses:
            plt.plot(item['total_losses'])
        if legend is not None:
            plt.legend([ 'loss {0}'.format(lg)for lg in legend], loc='upper left')
        else:
            plt.legend([ 'loss {0}'.format(i)for i in range(len(losses))], loc='upper left')

    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel(calculate_base)

    if max_iteration is not None:
        plt.xlim(0, max_iteration)


    plt.subplot(2, 2, 2)
    if isinstance(metrics,dict):
        for k, v in metrics.items():
            plt.plot(metrics[k])
        plt.legend(list(metrics.keys()), loc='upper left')
    elif  isinstance(metrics,list):
        legend_list=[]
        for i in range(len(metrics)):
            item=metrics[i]
            for k, v in item.items():
                plt.plot(item[k])
                if legend is not None:
                    legend_list.append([ 'loss {0} {1}'.format(k,legend[i])])
                else:
                    legend_list.append([ 'loss {0} {1}'.format(k,i)])
        plt.legend(legend_list, loc='upper left')


    plt.title('model metrics')
    plt.ylabel('metrics')
    plt.xlabel(calculate_base)

    if max_iteration is not None:
        plt.xlim(0, max_iteration)

    if save_path is not None:
        plt.savefig(save_path, bbox_inches='tight')
    if imshow == True:
        display.display(fig)

