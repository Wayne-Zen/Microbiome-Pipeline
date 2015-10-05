import csv
import sys

def collect_blast_table(meta_fp, output_fp, *tables):
    sampleID_list = []
    with open(meta_fp) as f:
        meta_reader = csv.reader(f, delimiter='\t')
        meta_reader.next()
        for row in meta_reader:
            sampleID_list.append(row[0])
    
    tax_set = set()
    for table in tables:
        with open(table) as f:
            csv_reader = csv.reader(f, delimiter='\t')
            header_row = csv_reader.next()
            for tax in header_row[1:]:
                tax_set.add(tax)
    tax_list = sorted(list(tax_set))
    
    tax_dict = {} #sampleID: []  #ordered by tax_list
    for table in tables:
        with open(table) as f:
            csv_reader = csv.reader(f, delimiter='\t')
            header = csv_reader.next()
            content = csv_reader.next()
            tax = header[1:]
            cnt = content[1:]
            tmp_dict = dict(zip(tax, cnt))
            sampleID = content[0]
            tax_dict[sampleID] = [tmp_dict[x] if x in tmp_dict else 0 for x in tax_list]

                                  
    with open(output_fp, 'w') as fo:
        fo.write('#SampleID\t{}\n'.format('\t'.join(tax_list)))
        for sampleID in sampleID_list:
            fo.write('{}\t{}\n'.format(sampleID, '\t'.join([str(x) for x in tax_dict[sampleID]])))

if __name__ == '__main__':
    collect_blast_table(sys.argv[1], sys.argv[2], *sys.argv[3:])