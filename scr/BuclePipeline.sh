#!/bin/bash

input=$1
output=$2
ref=$3

mkdir $output/tmp
mkdir $output/tmp/02_fastq_trimmed
mkdir $output/tmp/03_aligned
mkdir $output/tmp/04_deduplicated
mkdir $output/tmp/05_bismark_extractor
mkdir $output/tmp/06_bedGraph

mkdir $output/results
mkdir $output/results/02_fastq_trimmed
mkdir $output/results/03_aligned
mkdir $output/results/04_deduplicated
mkdir $output/results/05_bismark_extractor
mkdir $output/results/06_bedGraph
mkdir $output/results/results_html

array=($(ls $input/*.fastq.gz))
tLen=${#array[@]}

for (( i=0; i<${tLen}; i=i+2));
do

FQ1=${array[$i]}
FQ2=${array[$i+1]}
OUT=$output/tmp/02_fastq_trimmed

trim_galore --quality 30 --gzip --paired --fastqc \
            --illumina --output_dir ${OUT} \
            --cores 4 ${FQ1} ${FQ2}

wait

genome=$ref
PREFIX=one_mismatch

FQ1=$output/tmp/02_fastq_trimmed/*val_1.fq.gz
FQ2=$output/tmp/02_fastq_trimmed/*val_2.fq.gz
OUT=$output/tmp/03_aligned


echo "bismark aligned"; date
bismark --bowtie2 -p 2 --parallel 1 --bam --fastq \
        --output_dir ${OUT} \
        --prefix ${PREFIX} \
        --genome_folder ${genome} \
        -1 ${FQ1} -2 ${FQ2}

wait

BAM_IN=$output/tmp/03_aligned/one_mismatch*pe.bam
OUT=$output/tmp/05_bismark_extractor/

genome=$ref

echo "bismark_methylation_extractor"; date
bismark_methylation_extractor --paired-end \
                              --gzip \
                              --bedGraph \
                              --output ${OUT} \
                              --genome_folder ${genome} \
                              ${BAM_IN}


wait
genome=$ref
IN=$output/tmp/03_aligned/one_mismatch*pe.bam
OUT=$output/tmp/04_deduplicated

bam2nuc --genome_folder ${genome} --dir ${OUT} ${IN} 

wait 
genome=$ref

bismark2report --alignment_report ../data/03_aligned/one_mismatch*report.txt \
               --splitting_report ../data/05_bismark_extractor/one_mismatch*splitting_report.txt \
               --mbias_report ../data/05_bismark_extractor/one_mismatch*.M-bias.txt \
               --nucleotide_report ../data/04_deduplicated/one_mismatch*.nucleotide_stats.txt
wait     

mv $output/tmp/02_fastq_trimmed/* $output/results/02_fastq_trimmed

wait

mv $output/tmp/03_aligned/* $output/results/03_aligned

wait

mv $output/tmp/04_deduplicated/*.bam $output/results/04_deduplicated
mv $output/tmp/04_deduplicated/*.txt $output/results/04_deduplicated

wait 

mv $output/tmp/05_bismark_extractor/*.txt.gz $output/results/05_bismark_extractor
mv $output/tmp/05_bismark_extractor/*.txt $output/results/05_bismark_extractor

wait

mv  $output/tmp/05_bismark_extractor/*.bedGraph.gz $output/results/06_bedGraph
mv  $output/tmp/05_bismark_extractor/*.bismark.cov.gz $output/results/06_bedGraph  

wait 

mv *.html $output/results/results_html
      
done

echo 'DONE'
