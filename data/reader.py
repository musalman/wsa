import gzip
with gzip.open('sentibayes.gz','r') as fin:        
    for line in fin:        
        print(line)