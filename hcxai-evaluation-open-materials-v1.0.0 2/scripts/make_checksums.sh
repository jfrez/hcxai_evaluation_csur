#!/bin/sh
set -eu

cd "$(dirname "$0")/.."
find . -type f \
  ! -path './.git/*' \
  ! -name 'CHECKSUMS_SHA256.txt' \
  ! -name '.DS_Store' \
  | sort \
  | xargs shasum -a 256 > CHECKSUMS_SHA256.txt
