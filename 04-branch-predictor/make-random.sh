#!/bin/bash

N=10000000
RANDOM_FILE="random.bin"
PREDICTABLE_FILE="predictable.bin"

# Step 1: Generate random 0s and 1s
head -c $N /dev/urandom | tr -dc '\0\1' | head -c $N > "$RANDOM_FILE"

# Step 2: Count 0s and 1s
zeros=$(tr -cd '\0' < "$RANDOM_FILE" | wc -c)
ones=$(tr -cd '\1' < "$RANDOM_FILE" | wc -c)

# Step 3: Generate predictable file with same counts
{ head -c $zeros < /dev/zero; head -c $ones < /dev/zero | tr '\0' '\1'; } > "$PREDICTABLE_FILE"

# Print confirmation
echo "Generated $RANDOM_FILE with $zeros zeros and $ones ones"
echo "Generated $PREDICTABLE_FILE with identical counts in order"
