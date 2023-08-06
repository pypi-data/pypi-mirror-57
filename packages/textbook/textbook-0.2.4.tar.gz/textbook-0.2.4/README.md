<h1 align="center">
Textbook
</h1>
<h2 align="center">
Universal NLU/NLI Dataset Processing Framework
</h2>

It is designed with `BERT` in mind and currently support seven commonsense reasoning datsets(`alphanli`, `hellaswag`, `physicaliqa`, `socialiqa`, `codah`, `cosmosqa`, and `commonsenseqa`). It can be also applied to other datasets with few line of codes. It adopts `pandas` and `modin[ray]`'s multiprocessing in loading/processing the datasets.

## Architecture

![Architecture Image](./textbook.svg)

## Dependency

`pip install -r requirements.txt`

## Download raw datasets

```bash
./fetch.sh
```

It downloads `alphanli`, `hellaswag`, `physicaliqa`, `socialiqa`, `codah`, `cosmosqa`, and `commonsenseqa` from AWS in `data_cache`.
In case you want to use something-something, pelase download the dataset from 20bn's website.

## Usage

Following examples show how to load a dataset or create a multitask dataset from multiple datasets.

### Load a dataset in parallel with modin[ray]

```python
from transformers import BertTokenizer
from textbook import *
import modin.pandas as pd

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

d1 = MultiModalDataset(
    df=pd.read_json("data_cache/alphanli/train.jsonl", lines=True),
    template=lambda x: template_anli(x, LABEL2INT['anli']),
    renderers=[lambda x: renderer_text(x[0], tokenizer)],
    parallel=True
)
bt1 = BatchTool(tokenizer, source="anli")
i1 = DataLoader(d1, batch_sampler=TokenBasedSampler(d1, batch_size=64), collate_fn=bt1.collate_fn)
```

### Load a dataset with naive pandas

```python
from transformers import BertTokenizer
from textbook import *
import pandas as pd

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

d1 = MultiModalDataset(
    df=pd.read_json("data_cache/alphanli/train.jsonl", lines=True),
    template=lambda x: template_anli(x, LABEL2INT['anli']),
    renderers=[lambda x: renderer_text(x, tokenizer)],
    parallel=False
)
bt1 = BatchTool(tokenizer, source="anli")
i1 = DataLoader(d1, batch_sampler=TokenBasedSampler(d1, batch_size=64), collate_fn=bt1.collate_fn)
```

### Create a multitask dataset with multiple datasets

```python
from transformers import BertTokenizer
from textbook import *
import pandas as pd

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

# add additional tokens for each task as special `cls_token`
tokenizer.add_special_tokens({"additional_special_tokens": [
        "[ANLI]", "[HELLASWAG]"
]})

d1 = MultiModalDataset(
    df=pd.read_json("data_cache/alphanli/train.jsonl", lines=True),
    template=lambda x: template_anli(x, LABEL2INT['anli']),
    renderers=[lambda x: renderer_text(x, tokenizer, "[ANLI]")],
    parallel=False
)
bt1 = BatchTool(tokenizer, source="anli")
i1 = DataLoader(d1, batch_sampler=TokenBasedSampler(d1, batch_size=64), collate_fn=bt1.collate_fn)

d2 = MultiModalDataset(
        df=pd.read_json("data_cache/hellaswag/train.jsonl", lines=True),
        template=lambda x: template_hellaswag(x, LABEL2INT['hellaswag']),
        renderers=[lambda x: renderer_text(x, tokenizer, "[HELLASWAG]")],
        parallel=False
    )
bt2 = BatchTool(tokenizer, source="hellaswag")
i2 = DataLoader(d2, batch_sampler=TokenBasedSampler(d1, batch_size=64), collate_fn=bt2.collate_fn)

d = MultiTaskDataset([i1, i2], shuffle=False)

#! batch size must be 1 for multitaskdataset, because we already batched in each sub dataset.
for batch in DataLoader(d, batch_size=1, collate_fn=BatchTool.uncollate_fn):

    pass

    # {
    #     "source": "anli" or "hellaswag",
    #     "labels": ...,
    #     "input_ids": ...,
    #     "attentions": ...,
    #     "token_type_ids": ...,
    #     "images": ...,
    # }
```
