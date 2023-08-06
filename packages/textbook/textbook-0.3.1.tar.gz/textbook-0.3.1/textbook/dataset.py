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

from .templates import *
from .renderers import *

# import pandas as pd
import modin.pandas as pd
from torch.utils.data import Dataset
from tqdm import tqdm
from loguru import logger


def modin_apply_hack(df, func):
    # ! Default pandas return a series, but modin returns a dataframe with one column.
    temp = df.apply(func, axis=1, result_type='expand')
    # ! Have to transform one-column dataframe into a full-blown one.
    d = pd.DataFrame.from_records(temp[0].to_list())
    return d


class MultiModalDataset(Dataset):

    def __init__(self, df: pd.DataFrame, template: Callable, renderers: List[Callable]):
        df = modin_apply_hack(df, template)
        for renderer in renderers:
            df = modin_apply_hack(df, renderer)
        self.data: List[Dict] = df.to_dict('records')

    def __len__(self):

        return len(self.data)

    def __getitem__(self, index):

        return self.data[index]


class MultiTaskDataset(Dataset):

    def __init__(self, dataloaders, shuffle: bool = True):

        self.data: List = []

        for loader in tqdm(dataloaders):
            for batch in tqdm(loader, leave=False):
                self.data.append(batch)

        if shuffle:
            random.shuffle(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]


__all__ = ["MultiTaskDataset", "MultiModalDataset"]
