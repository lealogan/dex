"""Basic utility to cmc curve and color/manasource distributions"""
import json

j = json.load(file('../../allcards.json'))
dcmc = {}
for card in file('./UR-Madness.txt').readlines():
    if card[0:3] != "SB:":
        card = ' '.join(card.split(' ')[1:])
        card = card.replace('\n', '')
        name = j[card]['name']
        try:
            print j[card]['name'], j[card]['cmc'], j[card]['manaCost']#, j[card]['text']
            dcmc[int(j[card]['cmc'])].append(j[card]['name'])
        except KeyError:
            print ''
print dcmc

#j = json.load(file('../../allcards.json'))
#print j['Moonmist']


#stop = 0
#for i in json.load(file('../../allcards.json')).iteritems():
#    if stop > 10: break
#    print i[1]['name'], i[1]['cmc'], i[1]['manaCost'], i[1]['text']
#    stop+=1

#Moonmist {u'layout': u'normal'
# u'name': u'Moonmist'
# u'text': u'Transform all Humans. Prevent all combat damage that would be dealt this turn by creatures other than Werewolves and Wolves. (Only double-faced cards can be transformed.)'
# u'cmc': 2
# u'colors': [u'Green']
# u'imageName': u'moonmist'
# u'types': [u'Instant']
# u'manaCost': u'{1}{G}'
# u'type': u'Instant'
# u'colorIdentity': [u'G']}
