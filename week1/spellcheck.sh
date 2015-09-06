#!/bin/bash

echo -n "Enter some text : "
read mytext 

echo  "$mytext" > file2.txt

tr -sc [:alpha:] '\n' < file2.txt | tr A-Z a-z | sort | uniq | comm -23 - dict.txt | wc -l

#comm -32 <(tr -sc [:alpha:] '\n'  < file2.txt | tr A-Z a-z | sort -u) <(tr A-Z a-z <  dict.txt |sort -u)|wc -l
