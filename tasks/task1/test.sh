
#!/bin/bash
set -e

echo "Running Task 1 automated tests..."

cd /app

python -m unittest -v test_normalize
