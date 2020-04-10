from config import ConfigArgs as args
import os
import data
import numpy as np

fpaths, texts, _ = data.read_meta(os.path.join(args.data_path, args.meta))

max_mel = max(np.load(os.path.join(args.data_path, args.mel_dir, fpath)).shape[0] for fpath in fpaths)
max_char = max(len(text) for text in texts)
print(f'max_Tx is {max_char}')
print(f'max_Ty is {max_mel}')
