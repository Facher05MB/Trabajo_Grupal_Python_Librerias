import wikipedia as wiki


if 'Busca' in rec:
    busca = rec.replace('busca','')
    wiki.summary(busca, 1)
    print('buscando' +rec)