domy = [4, 2, 0, 5, 0, 1, 5, 4]

print('pocet obyvatelov je', sum(domy))
print('neobyvanych domov je', len([x for x in domy if x == 0]))
print('maximalny pocet obyvatelov v dome je', max(domy))
print('pocet maximalnych domov', len([x for x in domy if x == max(domy)]))
