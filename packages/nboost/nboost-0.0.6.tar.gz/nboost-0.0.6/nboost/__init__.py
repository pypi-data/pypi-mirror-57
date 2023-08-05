"""General nboost package parameters"""
from pathlib import Path

PKG_PATH = Path(__file__).parent

# component => class => module
CLASS_MAP = {
    'codex': {
        'ESCodex': 'es'
    },
    'model': {
        'ShuffleModel': 'shuffle',
        'TransformersModel': 'transformers',
        'BertModel': 'bert_model',
        'AlbertModel': 'albert_model'
    },
    'indexer': {
        'ESIndexer': 'es'
    }
}

# model_dir => url
MODEL_MAP = {
    "bert-base-uncased-msmarco": "https://storage.googleapis.com/koursaros/bert-base-uncased-msmarco.tar.gz",
    "albert-tiny-uncased-msmarco": "https://storage.googleapis.com/koursaros/albert-tiny-uncased-msmarco.tar.gz",
    "biobert-base-uncased-msmarco": "https://storage.googleapis.com/koursaros/biobert-base-uncased-msmarco.tar.gz"
}

# image => directory
IMAGE_MAP = {
    'alpine': '../Dockerfiles/alpine',
    'tf': '../Dockerfiles/tf',
    'torch': '../Dockerfiles/torch'
}

