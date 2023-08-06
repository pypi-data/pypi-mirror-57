#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-17 18:09:14
# @Author  : Chenghao Mou (mouchenghao@gmail.com)
# @Link    : link
# @Version : 1.0.0

# pylint: disable=unused-wildcard-import
# pylint: disable=no-member
# pylint: disable=not-callable

import os
import random
import json
from typing import *
from pathlib import Path
from dataclasses import dataclass
from itertools import zip_longest

from .templates import *
from .renderers import *

import torch
import ray
from torch.utils.data import Dataset, Sampler
from torch.nn.utils.rnn import pad_sequence
from transformers import PreTrainedTokenizer
from tqdm import tqdm
from dask.dataframe.utils import make_meta
import pandas as pd
from loguru import logger


class MultiModalDataset(Dataset):

    def __init__(self, df: pd.DataFrame, template: Callable, renderers: List[Callable], parallel=False):

        df = df.apply(template, axis=1, result_type='expand')
        for renderer in renderers:
            df = df.apply(renderer, axis=1, result_type='expand')
        if parallel:
            self.data: List[Dict] = df[0].to_dict('records')
        else:
            self.data: List[Dict] = df.to_dict('records')

    def __len__(self):

        return len(self.data)

    def __getitem__(self, index):

        return self.data[index]


class MultiTaskDataset(Dataset):

    def __init__(self, dataloaders, shuffle: bool = True):

        self.data: List = []

        for loader in tqdm(dataloaders):
            for batch in tqdm(loader, leave=True):
                self.data.append(batch)
        if shuffle:
            random.shuffle(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]


__all__ = ["MultiTaskDataset", "MultiModalDataset"]
