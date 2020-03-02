#!/bin/bash

h=$(cat words.csv)
m=$(echo $h | tr ',' '\n')

c=0
for i in $m; 
    do
        echo "5 % $c" | bc -l
        #if 1 % $c == 0 ; then
            #echo $i
        #fi
        c=$(($c+1))
        echo "count: $c"
    done
