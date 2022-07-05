#!/usr/bin/env python
"""script for calculating BLEU scores using NLTK module."""

import nltk
from nltk.translate.bleu_score import corpus_bleu
import re
import logging
from typing import Iterable, List, Tuple



targets = [] # initialize list of target translations
hypotheses = [] # initialize list of generated translations

def main() -> None:
    logging.basicConfig(filename='bleu_scoring.log', level=logging.INFO)
    
    # this dictionary stores the values for the models' 1gram, 2gram, 3gram, 4gram,bleu4 scores in a list
    # predictions_4000updates.txt -- file of translations by LSTM @ 4000 updates
    # predictions_8000updates.txt -- file of translations by LSTM @ 8000 updates
    # predictions_transformer1.txt -- file of translations by Transformer @ 4000 updates
    # predictions_transformer8000.txt -- file of translations by Transformer @ 8000 updates
    predictions = {'predictions_4000updates.txt': [0,0,0,0,0],'predictions_8000updates.txt':[0,0,0,0,0],'predictions_transformer1.txt':[0,0,0,0,0],'predictions_transformer8000.txt':[0,0,0,0,0]} 
    
    for prediction in predictions:
        logging.info(f'started {prediction}')
        with open(prediction,'r') as source:
            for line in source: 
                if re.match(r'T-\d*\s(.*)',line):
                    targ = nltk.tokenize.word_tokenize(re.match(r'T-\d*\s(.*)',line).group(1))       
                    targets.append([targ])
                    logging.info('gold found!')
                elif re.match(r'H-\d*\s(.*)',line):
                    hyp = nltk.tokenize.word_tokenize(re.match(r'H-\d*\s(.*)',line).group(1))
                    hypotheses.append(hyp)
                    logging.info('translation found!')
                    
            logging.info(f'starting {prediction} 1-gram bleu scoring...')
            predictions[prediction][0] = corpus_bleu(targets, hypotheses,smoothing_function=nltk.translate.bleu_score.SmoothingFunction().method0,weights=(1,0,0,0))
            
            logging.info(f'starting {prediction} 2-gram bleu scoring...')
            predictions[prediction][1] = corpus_bleu(targets, hypotheses,smoothing_function=nltk.translate.bleu_score.SmoothingFunction().method0,weights=(0,1,0,0))
            
            logging.info(f'starting {prediction} 3-gram bleu scoring...')
            predictions[prediction][2] = corpus_bleu(targets, hypotheses,smoothing_function=nltk.translate.bleu_score.SmoothingFunction().method0,weights=(0,0,1,0))
            
            logging.info(f'starting {prediction} 4-gram bleu scoring...')
            predictions[prediction][3] = corpus_bleu(targets, hypotheses,smoothing_function=nltk.translate.bleu_score.SmoothingFunction().method0,weights=(0,0,0,1))
            
            logging.info(f'starting {prediction} even-weight bleu scoring...')
            predictions[prediction][4] = corpus_bleu(targets, hypotheses,smoothing_function=nltk.translate.bleu_score.SmoothingFunction().method0,weights=(0.25,0.25,0.25,0.25))
            
            print(f'{prediction}: {predictions[prediction]}')
            
            logging.info(f'finished {prediction}')

if __name__== "__main__": 
    
    main()