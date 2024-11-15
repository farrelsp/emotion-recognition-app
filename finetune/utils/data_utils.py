import numpy as np
import pandas as pd
import string
import torch
import re
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer

#####
# Emotion Twitter
#####
class EmotionDetectionDataset(Dataset):
    # Static constant variable
    LABEL2INDEX = {'sadness': 0, 'anger': 1, 'surprise': 2, 'fear': 3, 'joy': 4, 'disgust': 5, 'trust': 6, 'anticipation': 7}
    INDEX2LABEL = {0: 'sadness', 1: 'anger', 2: 'surprise', 3: 'fear', 4: 'joy', 5: 'disgust', 6: 'trust', 7: 'anticipation'}
    NUM_LABELS = 8
    
    def load_dataset(self, path):
        # Load dataset
        dataset = pd.read_csv(path)
        dataset['label'] = dataset['label'].apply(lambda sen: self.LABEL2INDEX[sen])
        return dataset

    def __init__(self, dataset_path, tokenizer, no_special_token=False, *args, **kwargs):
        self.data = self.load_dataset(dataset_path)
        self.tokenizer = tokenizer
        self.no_special_token = no_special_token
        
    def __getitem__(self, index):
        tweet, label = self.data.loc[index,'tweet'], self.data.loc[index,'label']        
        subwords = self.tokenizer.encode(tweet, add_special_tokens=not self.no_special_token)
        return np.array(subwords), np.array(label), tweet
    
    def __len__(self):
        return len(self.data)
        
class EmotionDetectionDataLoader(DataLoader):
    def __init__(self, max_seq_len=512, *args, **kwargs):
        super(EmotionDetectionDataLoader, self).__init__(*args, **kwargs)
        self.collate_fn = self._collate_fn
        self.max_seq_len = max_seq_len
        
    def _collate_fn(self, batch):
        batch_size = len(batch)
        max_seq_len = max(map(lambda x: len(x[0]), batch))
        max_seq_len = min(self.max_seq_len, max_seq_len)
        
        subword_batch = np.zeros((batch_size, max_seq_len), dtype=np.int64)
        mask_batch = np.zeros((batch_size, max_seq_len), dtype=np.float32)
        label_batch = np.full((batch_size, 1), -100, dtype=np.int64)

        seq_list = []
        for i, (subwords, label, raw_seq) in enumerate(batch):
            subwords = subwords[:max_seq_len]
            subword_batch[i,:len(subwords)] = subwords
            mask_batch[i,:len(subwords)] = 1
            label_batch[i] = label

            seq_list.append(raw_seq)
            
        return subword_batch, mask_batch, label_batch, seq_list