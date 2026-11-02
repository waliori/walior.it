#!/usr/bin/env bash
# Renders every thumbnail listed in list.txt (name|frame|path|dim|zoom) into the folder given as $1.
# Needs PUPPETEER_PATH and CHROME_PATH like tools/still.mjs.
set -e; here=$(cd "$(dirname "$0")" && pwd); out=${1:?output folder}; mkdir -p "$out"
while IFS='|' read -r name frame path dim zoom; do [[ -z "$name" || "$name" == \#* ]] && continue
  node "$here/../../tools/still.mjs" "file://$here/thumb.html?frame=frames/$frame&path=$path&dim=$dim&zoom=$zoom" "$out/$name.png" 1280 720; done < "$here/list.txt"
