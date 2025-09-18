#!/bin/bash

# Test script for phase 2 of HiveBox application
# This script checks if the version function works correctly

OUTPUT=$(docker run --rm hivebox:0.0.1)
echo $OUTPUT
if [[ $OUTPUT == "HiveBox version v0.0.1" ]]; then
    echo "Test passed: Correct version output"
    exit 0
else
    echo "Test failed: Incorrect version output"
    exit 1
fi 