#!/usr/bin/env bash

python preprocess.py -f ../dataset/log_preprocess/20181128/all_ph.txt --columns uirt --sep '\t' --val_size 1000 --test_size 5000
python train.py -d ../dataset/log_preprocess/20181128/all_ph/
