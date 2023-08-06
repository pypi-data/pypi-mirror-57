#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-20 21:18:27
# @Author  : Chenghao Mou (chengham@isi.edu)

# pylint: disable=unused-wildcard-import
# pylint: disable=no-member

import os
import json

from dataclasses import dataclass
from typing import *

# Third party libraries
import regex
import ray
from loguru import logger


class Configuration:

    def transform(self, datum: Union[str, Dict]) -> Dict[str, Any]:

        raise NotImplementedError("not implemented")


@ray.remote
@dataclass
class ANLIConfiguration(Configuration):

    int2label: Dict[int, str] = None
    label2int: Dict[str, int] = None

    def __post_init__(self):

        self.int2label = {
            "0": "1",
            "1": "2",
        }
        self.label2int = {
            "1": 0,
            "2": 1,
        }

    def transform(self, datum: Union[str, Dict]) -> Dict[str, Any]:

        assert isinstance(datum, str)

        datum = json.loads(datum)

        template = {
            "text": [
                [datum["obs1"], datum["hyp1"], datum["obs2"]],
                [datum["obs1"], datum["hyp2"], datum["obs2"]],
            ],
            "label": None if "label" not in datum else self.label2int[datum["label"]],
            "image": None,
            "token_type_id": [0, 1, 0],
            "attention": [1, 1, 1]
        }

        return template


@ray.remote
@dataclass
class HellaSwagConfiguration(Configuration):

    int2label: Dict[int, str] = None
    label2int: Dict[str, int] = None

    def __post_init__(self):

        self.int2label = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
        }

        self.label2int = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
        }

    def transform(self, datum: Union[str, Dict]) -> Dict[str, Any]:

        assert isinstance(datum, str)

        datum = json.loads(datum)

        template = {
            "text": [
                [datum["ctx"], x] for x in datum["ending_options"]
            ],
            "label": None if "label" not in datum else self.label2int[datum["label"]],
            "image": None,
            "token_type_id": [0, 1],
            "attention": [1, 1]
        }

        return template


@ray.remote
@dataclass
class PIQAConfiguration(Configuration):

    int2label: Dict[int, str] = None
    label2int: Dict[str, int] = None

    def __post_init__(self):

        self.label2int = {
            "0": 0,
            "1": 1,
        }
        self.int2label = {
            "0": "0",
            "1": "1",
        }

    def transform(self, datum: Union[str, Dict]) -> Dict[str, Any]:

        assert isinstance(datum, str)

        datum = json.loads(datum)

        template = {
            "text": [
                [datum["goal"], datum["sol1"]],
                [datum["goal"], datum["sol2"]],
            ],
            "label": None if "label" not in datum else self.label2int[datum["label"]],
            "image": None,
            "token_type_id": [0, 1],
            "attention": [1, 1]
        }

        return template


@ray.remote
@dataclass
class SIQAConfiguration(Configuration):

    int2label: Dict[int, str] = None
    label2int: Dict[str, int] = None

    def __post_init__(self):

        self.int2label = {
            "0": "1",
            "1": "2",
            "2": "3"
        }
        self.label2int = {
            "1": 0,
            "2": 1,
            "3": 2
        }

    def transform(self, datum: Union[str, Dict]) -> Dict[str, Any]:

        assert isinstance(datum, str)

        datum = json.loads(datum)

        template = {
            "text": [
                [datum["context"], datum["question"], datum["answerA"]],
                [datum["context"], datum["question"], datum["answerB"]],
                [datum["context"], datum["question"], datum["answerC"]],
            ],
            "label": None if "label" not in datum else self.label2int[datum["label"]],
            "image": None,
            "token_type_id": [0, 0, 1],
            "attention": [1, 1, 1]
        }

        return template


@ray.remote
@dataclass
class SMTHSMTHConfiguration(Configuration):

    def transform(self, datum: Dict) -> Dict[str, Any]:

        assert isinstance(datum, Dict)

        template = {
            "text": [
                [datum["label"]]
            ],
            "label": None,
            "image": datum["id"],
            "token_type_id": [0],
            "attention": [1]
        }

        return template


@ray.remote
@dataclass
class CODAHConfiguration(Configuration):

    def transform(self, datum: Union[str, Dict]) -> Dict[str, Any]:
        category, prompt, answer0, answer1, answer2, answer3, label = regex.split(r' {2,}', datum)
        result = {
            "category": category,
            "text": [
                [prompt, answer0],
                [prompt, answer1],
                [prompt, answer2],
                [prompt, answer3]
            ],
            "image": None,
            "label": int(label),
            "token_type_id": [0, 1],
            "attention": [1, 1],
        }

        return result


@ray.remote
@dataclass
class CommonsenseQAConfiguration(Configuration):

    int2label: Dict[int, str] = None
    label2int: Dict[str, int] = None

    def __post_init__(self):

        self.int2label = {
            "0": "A",
            "1": "B",
            "2": "C",
            "3": "D",
            "4": "E",
        }
        self.label2int = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4
        }

    def transform(self, datum: Union[str, Dict]) -> Dict[str, Any]:

        assert isinstance(datum, str)

        datum = json.loads(datum)

        template = {
            "text": [
                [datum["question"]["stem"], x['text']] for x in datum["question"]["choices"]
            ],
            "label": None if "answerKey" not in datum else self.label2int[datum["answerKey"]],
            "image": None,
            "token_type_id": [0,  1],
            "attention": [1, 1]
        }

        return template
