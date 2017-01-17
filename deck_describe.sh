#!/bin/bash
while read c; do
    cardname=$(echo -n $c | tr '[:upper:]' '[:lower:]' | gsed -re "s/^[0-9 \t]+//" -e "s/\b([a-z])/\U\1/g");
    echo $cardname;
    jq --arg card "$cardname" \
        '.[$card]."manaCost",
        .[$card].type,
        .[$card].text,
        .[$card].power,
        .[$card].toughness
        ' allcards.json |\
    gsed -e "s/null//" | cat -s;
done < $1
