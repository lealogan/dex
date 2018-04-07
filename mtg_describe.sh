#!/bin/bash
#jq --arg card $1 '. [] | .[$card]' temp.json
c=$@
cardname=$(echo $c | tr '[:upper:]' '[:lower:]' | sed -re "s/\b([a-z])/\U\1/g")
jq --arg card "$cardname" \
    '.[$card]."manaCost",
    .[$card].type,
    .[$card].text,
    .[$card].power,
    .[$card].toughness
    ' allcards.json |\
sed -e "s/null//" | cat -s
