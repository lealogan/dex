#!/bin/bash
while read c; do
    cleanedcard=$(echo -n $c | tr '[:upper:]' '[:lower:]' | gsed -re "s/^[0-9 \t]+//"); # -e "s/\b([a-z])/\U\1/g");
    #cleanedcard=$(echo -n $c | tr '[:upper:]' '[:lower:]' | gsed -re "s/^[0-9 \t]+//" -e "s/\b([a-z])/\U\1/g");
    echo $cleanedcard;
    jq --arg cardname "$cleanedcard" \
        '.[] | select(.imageName == $cardname) as $card |
        $card.manaCost,
        $card.type,
        $card.text,
        $card.power,
        $card.toughness' ~/code/dex/allcards.json |\
    gsed -e "s/null//" | cat -s;
done < $1
