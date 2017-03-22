
create type card as (artist text, cmc int, colorIdentitiy text[], flavor text, id text, imageName text, layout text, manacost text, multiverseid int, name text, names text[], number int, power int,  rarity text, subtypes text[], supertypes text[], "text" text, toughness int, "type" text, types text[]);

select json_populate_recordset(null::card, json_array_elements(data->'SOI'->'cards')) from public.all limit 10;


 {
"artist"
"cmc"
"colorIdentity"
"colors"
"id"
"imageName"
"layout"
"manaCost"
"multiverseid"
"name"
"names"
"number"
"power"
"rarity"
"subtypes"
"supertypes"
"text"
"toughness"
"type"
"types"
}

--Full
with jsn as (
    select json_array_elements(data->'SOI'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'OGW'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'DTK'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'BFZ'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'ORI'->'cards') as card
    from public.all 
) select 
card->>'name' as name,
card->>'manaCost' as manaCost,
card->>'text' as text,
card->>'power' as power,
card->>'toughness' as toughness,
card->>'colors' as colors,
card->>'colorIdentity' as colorIdentity,
card->>'cmc' as cmc,
card->>'type' as "type",
card->>'types' as types,
card->>'subtypes' as subtypes,
card->>'supertypes' as supertypes,
card->>'imageName' as imageName,
card->>'names' as names,
card->>'multiverseid' as multiverseid,
card->>'id' as id,
card->>'layout' as layout,
card->>'number' as "number",
card->>'rarity' as rarity,
card->>'artist' as artist
into public.standard
from jsn;

--abbreviated
with jsn as (
    select json_array_elements(data->'SOI'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'OGW'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'DTK'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'BFZ'->'cards') as card
    from public.all 
    UNION ALL
    select json_array_elements(data->'ORI'->'cards') as card
    from public.all 
) select 
card->>'imageName' as name,
card->>'manaCost' as manaCost,
card->>'text' as text,
card->>'power' as power,
card->>'toughness' as toughness,
card->>'colorIdentity' as colors,
card->>'cmc' as cmc,
card->>'type' as "type",
card->>'types' as types,
card->>'subtypes' as subtypes,
card->>'supertypes' as supertypes,
card->>'names' as names
into public.standard
from jsn;
