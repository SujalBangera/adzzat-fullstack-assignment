#!/bin/bash
set -e

echo "Running Task 2 automated tests..."

cd /app

python -m unittest -v test_task2
