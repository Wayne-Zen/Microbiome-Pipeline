import os
import sys
import pandas as pd
from itertools import islice

#trim primer
#change header
#count sequence number
def preprocess_for_galaxy(meta_data_dir, input_dir, output_dir):
    meta_data = pd.read_csv(os.path.join(meta_data_dir, 'meta_data.txt') , sep='\t')
    
    cnt_list = []
    for i in meta_data.index:
        # forward
        cnt1 = 0
        with open(os.path.join(input_dir, meta_data.ix[i, 'OriginalForwardFileName'])) as fi, \
                 open(os.path.join(output_dir, meta_data.ix[i, 'GalaxyForwardFileName']), 'w') as fo:
            while True:
                next_n = list(islice(fi, 4))
                if not next_n:
                    break
                cnt1 += 1
                fo.write('@{}_{}\n'.format(meta_data.ix[i, '#SampleID'], cnt1))
                fo.write(next_n[1][len(meta_data.ix[i, 'LinkerPrimerSequence']):])
                fo.write(next_n[2])
                fo.write(next_n[3][len(meta_data.ix[i, 'LinkerPrimerSequence']):])
        # reverse
        cnt2 = 0
        with open(input_dir + '/' + meta_data.ix[i, 'OriginalReverseFileName']) as fi, \
                 open(output_dir + '/' + meta_data.ix[i, 'GalaxyReverseFileName'], 'w') as fo:
            while True:
                next_n = list(islice(fi, 4))
                if not next_n:
                    break
                cnt2 += 1
                fo.write('@{}_{}\n'.format(meta_data.ix[i, '#SampleID'], cnt2))
                fo.write(next_n[1][len(meta_data.ix[i, 'ReversePrimer']):])
                fo.write(next_n[2])
                fo.write(next_n[3][len(meta_data.ix[i, 'ReversePrimer']):])
        
        if cnt1 != cnt2:
            raise Exception("ERROR: forward sequence number is not equal to reverse sequence number")
        cnt_list.append(cnt1)
    
    # build sequence_count.txt
    cnt_df = pd.concat([meta_data[['#SampleID']], pd.DataFrame({'Original': cnt_list})], axis=1)
    cnt_df.to_csv(os.path.join(meta_data_dir, 'original_sequence_count.txt'), sep='\t', index=False)
    
if __name__ == "__main__":
    meta_data_dir = os.path.join('projects', sys.argv[1], 'meta_data')
    input_dir = os.path.join('projects', sys.argv[1], 'sequence_data_original')
    output_dir = os.path.join('projects', sys.argv[1], 'sequence_data_galaxy')
    preprocess_for_galaxy(meta_data_dir, input_dir, output_dir)
    
