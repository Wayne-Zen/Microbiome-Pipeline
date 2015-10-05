import csv
import sys

def collect_count_table(meta_fp, output_fp, *tables):
    sampleID_list = []
    with open(meta_fp) as f:
        meta_reader = csv.reader(f, delimiter='\t')
        meta_reader.next()
        for row in meta_reader:
            sampleID_list.append(row[0])
    
    col_dict = {}
    col_list = []
    for table in tables:
        with open(table) as f:
            csv_reader = csv.reader(f, delimiter='\t')
            col_name = csv_reader.next()[1]
            col_list.append(col_name)
            tmp_dict = {}
            for row in csv_reader:
                tmp_dict[row[0]] = row[1]
            col_dict[col_name] = [tmp_dict[x] for x in sampleID_list]
    
    
    with open(output_fp, 'w') as fo:
        fo.write('#SampleID\t{}\n'.format('\t'.join(col_list)))
        for i in range(len(sampleID_list)):
            fo.write('{}\t{}\n'.format(sampleID_list[i], '\t'.join([str(col_dict[x][i]) for x in col_list])))

if __name__ == '__main__':
    collect_count_table(sys.argv[1], sys.argv[2], *sys.argv[3:])