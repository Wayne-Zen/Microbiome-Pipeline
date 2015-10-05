import csv
import sys

def tabulate_blast_result(tax_fp, res_fp, out_fp):
    # build dict
    seqid_to_tax = {}
    with open(tax_fp) as f:
        for line in f:
            content = line.strip().split('\t')
            seqid_to_tax[content[0]] = content[1]

    tax_to_cnt = {}
    SampleID = ''
    with open(res_fp) as csvfile:
        tablereader = csv.reader(csvfile, delimiter='\t')
        prev_query = '-1'
        for row in tablereader:
            header = row[0].split('_')
            SampleID = header[0]
            queryID = header[1]
            if queryID != prev_query:# select best hit
                seqid = row[1]
                tax = seqid_to_tax[seqid]
                if tax not in tax_to_cnt:
                    tax_to_cnt[tax] = 1
                else:
                    tax_to_cnt[tax] += 1
                prev_query = queryID
                

    with open(out_fp, 'w') as fo:
        fo.write('#SampleID\t{}\n'.format('\t'.join(tax_to_cnt.keys())))
        fo.write('{}\t{}\n'.format(SampleID, '\t'.join([str(x) for x in tax_to_cnt.values()])))

if __name__ == '__main__':
    tabulate_blast_result(sys.argv[1], sys.argv[2], sys.argv[3])