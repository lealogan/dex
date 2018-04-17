'''
creates dataset for cmc bayesian analysis
'''
import xml.etree.ElementTree as ET
import pandas as pd
DECKSIZE = 60


def parse_deck(filepath, verbose):
    # Split cards stored as "Commit // Memory" in cod files, but "Commit" in
    # allcards.json
    tree = ET.parse(filepath)
    root = tree.getroot()
    deck = {}
    for c in root[2]:
        if verbose:
            print(c.get('number') + ' ' + c.get('name'))
        card_number = c.get('number')
        card_name = c.get('name')
        if card_name.__contains__('/'):
            card_name = card_name.split('/')[0].strip()
        deck[card_name] = card_number
    return deck


def parse_sideboard(filepath, verbose):
    tree = ET.parse(filepath)
    root = tree.getroot()
    for c in root[3]:
        print('SB: '+c.get('number') + ' ' + c.get('name'))


def extract_mana_from_deck(deckname, deck, dall):
    '''
    Params:
        deck: dictionary {cardname : card_count}
        dall: pandas dataframe of allcards.json
    Returns:
        Dataframe of cmc distribution and average, along with the number of
        lands for a single deck. The idea being to predict number of lands
        cmc   0  1  2  3  4  5  6  numlands deckname   cmc_avg
        num  24  4  7  9  8  5  3        24  ug-draw  3.333333

    '''
    ddeck = pd.DataFrame(deck, index=['num'], dtype=int).transpose()

    # card_columns = ['cmc', 'type', 'text']
    card_columns = ['cmc', 'type']
    djoin = pd.merge(
            ddeck, dall[card_columns], left_index=True, right_index=True)
    decksize = djoin.num.sum()
    if decksize < DECKSIZE or decksize > DECKSIZE + 10:
        print('Skipping {}, has {} cards'.format(deckname, decksize))
        return (1, '')

    if ddeck.shape[0] != djoin.shape[0]:
        print("Warning: card not joined. Skipping: "+deckname)
        print(set(ddeck.index) - set(djoin.index))
        return (1, '')

    # count the lands
    numlands = djoin[djoin.type.str.contains('Land')].num.sum()
    nonlands = djoin[~djoin.type.str.contains('Land')].num.sum()

    cmc_avg = sum(djoin.num * djoin.cmc) / nonlands
    cmc_dist = djoin.groupby(djoin.cmc).sum().transpose()
    cmc_dist[0] = cmc_dist[0] - numlands
    # Calc cmc_avg from the histogram
    # del cmc_dist[0]
    # cmc_dist = cmc_dist.transpose()
    # avg_cmc = sum(cmc_dist.index * cmc_dist['num'])/cmc_dist.num.sum()

    cmc_dist['cmc_avg'] = cmc_avg
    cmc_dist['numlands'] = numlands
    cmc_dist['deckname'] = deckname
    return (0, cmc_dist)


'''
decks_to_parse = [
    # 'Rivals_of_Ixalan/rug-prowess.cod',
    'Rivals_of_Ixalan/metalwork.cod',
    # 'Rivals_of_Ixalan/ug-draw.cod'
    # 'Rivals_of_Ixalan/rg-monsters.cod'
] '''
decks_to_parse = open('deckpaths.txt')
decks_to_parse = decks_to_parse.readlines()
dall = pd.read_json('allcards.json').transpose()
firstdeck = True

for deckpath in decks_to_parse:
    deckpath = deckpath.strip()
    print('Processing: '+deckpath)
    deckname = deckpath.split('/')[-1].split('.')[0]
    deck = parse_deck(deckpath, False)
    (exitcode, dmana_extracted) = extract_mana_from_deck(deckname, deck, dall)
    if exitcode != 0:
        continue
    if firstdeck:
        firstdeck = False
        dmana = dmana_extracted
    else:
        dmana = pd.concat([dmana, dmana_extracted])

dmana.fillna(0, inplace=True)
dmana.set_index('deckname', inplace=True)
cols = ['numlands', 'cmc_avg'] + \
       [i for i in set(dmana.columns) - set(['cmc_avg', 'numlands'])]
dmana = dmana[cols]
# print(dmana)
dmana.to_csv('manacosts.csv')
