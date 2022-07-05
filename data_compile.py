#!/usr/bin/env python

import gzip
import re

def unzip_write(data,new_file) -> None:
    gzip.GzipFile(data)

    with gzip.open(data,'rb') as source:
        with open(new_file,'w') as sink:
                for row in source:
                    match = re.match(r'b\'(.*).\\n\'',row.strip())
                    line = match.group(1)
                    print(line.strip(),file=sink)

def main() -> None:
    
    gzip.GzipFile('europarl.es-en.es.gz')
    gzip.GzipFile('europarl.es-en.en.gz')
    gzip.GzipFile('dev2006.es.gz')
    gzip.GzipFile('dev2006.en.gz')

    with open('europarl.es-en.tsv','w') as sink:    
        with gzip.open('europarl.es-en.es.gz','r') as source1, gzip.open('europarl.es-en.en.gz','r') as source2:
                for es,en in zip(source1,source2):
                    print(f'{es.decode("iso-8859-1").strip()}\t{en.decode("iso-8859-1").strip()}',file=sink)

        with gzip.open('dev2006.es.gz','r') as source1, gzip.open('dev2006.en.gz','r') as source2:
                    for es,en in zip(source1,source2):
                        print(f'{es.decode("iso-8859-1").strip()}\t{en.decode("iso-8859-1").strip()}',file=sink)
        

if __name__ == '__main__':
    main()