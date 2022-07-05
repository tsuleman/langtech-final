#!/usr/bin/env python


def data_prep(data,es_path,en_path) -> None:

    with open(data,'r') as source:
        with open(es_path,'w') as es_sink, open(en_path,'w') as en_sink:
                for line in source:
                    line.strip()
                    es,en = line.split('\t')
                    print(es.casefold().strip(),file=es_sink)
                    print(en.casefold().strip(),file=en_sink)


def main() -> None:
    
    data_prep('europarl_train.tsv','train.es','train.en')
    data_prep('europarl_dev.tsv','dev.es','dev.en')
    data_prep('europarl_test.tsv','test.es','test.en')
    
        

if __name__ == '__main__':
    main()