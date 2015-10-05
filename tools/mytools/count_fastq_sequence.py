import sys
from itertools import islice


fastq_files = sys.argv[3:]
cnt_dict = {}
for fq in fastq_files:
    with open(fq) as f:
        while True:
            next_n = list(islice(f, 4))
            if not next_n:
                break
            sample_id = next_n[0].strip()[1:].split('_')[0]
            if sample_id in cnt_dict:
                cnt_dict[sample_id] += 1
            else:
                cnt_dict[sample_id] = 1

with open(sys.argv[1], 'w') as fo:
    fo.write('#SampleID\t%s\n' % sys.argv[2])
    for key in cnt_dict:
        fo.write('{}\t{}\n'.format(key, cnt_dict[key]))
