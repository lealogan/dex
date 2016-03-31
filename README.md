#Download allcards command
wget http://mtgjson.com/json/AllCards.json.zip -O temp.zip; unzip -p temp.zip | python -m json.tool > allcards.json; rm temp.zip

#Search through allcards.json (using sed)
sed -n /Black\ Lotus/,/},/p allcards.json

#Pretty print a cockatrice .cod file
python xml_parser.py mydeck.cod

#TODO add cube generation command and details
