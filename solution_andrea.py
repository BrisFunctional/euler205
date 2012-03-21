import itertools

PYRAMID = [range(1, 5)] * 9
CUBIC = [range(1, 7)] * 6

pyramid_combs = itertools.product(*PYRAMID)
cubic_combs = itertools.product(*CUBIC)

d_pyr = dict((i, 0) for i in range(9, 37))
d_cub = dict((i, 0) for i in range(6, 37))

for p in pyramid_combs:
    d_pyr[sum(p)] += 1

for p in cubic_combs:
    d_cub[sum(p)] += 1

tot_cube = 4**9
tot_pyr = 6**6

prob_cube_winning = 0

for k, v in d_pyr.iteritems():
    event_prob = float(sum([y for x, y in d_cub.iteritems() if x < k])) / tot_pyr
    tot_prob = (event_prob * v) / tot_cube
    prob_cube_winning += tot_prob

print prob_cube_winning
