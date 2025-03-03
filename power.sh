#!/bin/sh
a=3
b=4
result=$(echo "$a^$b" | bc)
echo "power($a, $b) -> $result"
