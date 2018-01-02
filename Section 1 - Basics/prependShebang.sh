#!/bin/sh
for file in *.py; do
    cat shebang.txt $file >> $file.$$
    mv $file.$$ $file
done
