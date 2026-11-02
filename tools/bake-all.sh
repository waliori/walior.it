#!/usr/bin/env bash
# Bakes every frame the page uses: the resting white-phosphor frames and their colour variants for hover.
# Three at a time with four ImageMagick threads each; more than that and the jobs thrash.
set -e; cd "$(dirname "$0")/.."
export MAGICK_THREAD_LIMIT=4
jobs=()
# the eight thumbnails: mono at rest, full colour with aberration on hover
i=0; for id in $(python3 -c "import json;print(' '.join(v['id'] for v in json.load(open('videos.json'))))"); do i=$((i+1))
  jobs+=("material/thumbs/$id.jpg site/images/v-$id.webp --seed $((i*11+3)) --size 1600x900")
  jobs+=("material/thumbs/$id.jpg site/images/v-$id-c.webp --seed $((i*11+3)) --size 1600x900 --colour 115 --shift 5")
done
# the reels: mono at rest, muted colour on hover (light interfaces inverted in mono only)
for f in "sail-1:" "sail-2:" "sail-3:" "sail-4:" "sail-5:" "toucan-1:--invert" "toucan-2:--invert" "toucan-3:--invert" "toucan-5:--invert" "ayat-1:--invert" "ayat-2:--invert" "ayat-4:--invert"; do
  IFS=: read n inv <<<"$f"; i=$((i+1))
  jobs+=("material/screens/$n.png site/images/$n.webp $inv --seed $((i*7))")
  jobs+=("material/screens/$n.png site/images/$n-c.webp --seed $((i*7)) --colour 55 --shift 3")
done
only="${1:-}"   # a substring to bake only some jobs, e.g. -c.webp
printf '%s\n' "${jobs[@]}" | { if [ -n "$only" ]; then grep -- "$only"; else cat; fi; } | xargs -P 3 -I{} sh -c 'python3 tools/crt.py {} >/dev/null && echo done {}' | cut -d' ' -f1-3
