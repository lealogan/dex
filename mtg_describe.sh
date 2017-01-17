#!/bin/bash
#jq --arg card $1 '. [] | .[$card]' temp.json
c=$@
cardname=$(echo $c | tr '[:upper:]' '[:lower:]' | gsed -re "s/\b([a-z])/\U\1/g")
jq --arg card "$cardname" \
    '.[$card]."manaCost",
    .[$card].type,
    .[$card].text,
    .[$card].power,
    .[$card].toughness
    ' allcards.json |\
gsed -e "s/null//" | cat -s
