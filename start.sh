#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage ./start.sh name_of_dir"
    exit
fi

new_dir=$1

if [ -d $new_dir ];then 
    echo "$new_dir exists"
    exit
fi
cp -r zero $new_dir
mv $new_dir/src/zero.py $new_dir/src/"$new_dir".py
