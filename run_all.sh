#!/usr/bin/env bash
# Run every task programme and extension, saving console output to outputs/ and plots to figures/.
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"
mkdir -p outputs figures
for f in code/Task_*.py extensions/Task_*.py; do
  name="$(basename "$f" .py)"
  echo "Running $f"
  "$PY" "$f" > "outputs/$name.txt"
done
echo "Done. See outputs/ and figures/."
