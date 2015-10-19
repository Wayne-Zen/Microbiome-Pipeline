# Microbiome Pipeline Based on Galaxy

## Download and run
```
mkdir Galaxy
cd Galaxy
git clone https://github.com/Wayne-Zen/Microbiome-Pipeline.git
cd Microbiome-Pipeline
sudo ./run.sh
```

## Setup
* sign up admin account
wzheng4@buffalo.edu

* data library
  1. Admin -> Data libraries -> Add datasets -> Upload files from filesystem paths
  2. Link to files without copying into Galaxy
    * my-data/projects/demo/sequence_data_galaxy/ [fastq]
    * my-data/projects/demo/meta_data/  [tabular]
    * my-data/database/HOMD

* install shed tools:
  1. Admin -> Search Tool Shed
    * pear: PEAR evaluates all possible paired-end read overlaps; [Pair-end Joining]
    * fastqc: Read QC reports using FastQC; [Quality Control]
    * fastq_groomer: Convert between various FASTQ quality formats; [Convert Formats]
    * fastq_quality_filter: Filter by quality; [Quality Control]
    * fastq_to_fasta: FASTQ to FASTA converter; [Convert Formats]
    * ncbi_blast_plus: NCBI BLAST+; [BLAST Search]

## Demo
1. import sequence data
2. Build List of Dataset Pairs, pair
3. Pear, Paired-end Dataset Collection
4. fq_counter, Joined
5. FastQC, Before
6. FASTQ Groomer
7. Filter by quality
8. fq_counter, Filtered
9. FastQC, After
10. FASTQ to FASTA, Discard no, Rename no
11. import meta_data
12. collect count table, meta_data, original_count, Joined, Filtered
13. !!NCBI BLAST+ makeblastdb, nucleotide, homd.fa, homd
14. NCBI BLAST+ blastn, FASTQ to FASTA result, homd.fa, megablast, 12 columns, Maximum hits to show(5), 97, 95
15. tabulate blast result
16. collect blast table

## Development from zero
```
mkdir Galaxy
cd Galaxy
git clone git@github.com:Wayne-Zen/Microbiome-Pipeline.git
cd Microbiome-Pipeline
git checkout -b dev origin/dev
```

## Sync with original Galaxy
Original Galaxy -> dev -> master 
```
cd Galaxy/Microbiome-Pipeline
git checkout dev
git remote add upstream https://github.com/galaxyproject/galaxy
git fetch upstream master
git merge upstream/master
git merge dev
git push -u origin dev
git checkout master
git merge dev
git push -u origin master
```
