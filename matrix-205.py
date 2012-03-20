score_hash = {}
score_hash_2 = {}
total_rolls = 4**9
total_rolls_2 = 6**6

import itertools

def score(x, scores):
    sum_x = sum(x)
    if not scores.has_key(sum_x):
        scores[sum_x] = 0
    scores[sum_x] += 1 

r = lambda: range(1,5)
map(lambda x: score(x, score_hash),itertools.product(r(),r(),r(),r(),r(),r(),r(),r(),r())) 
r = lambda: range(1, 7)
map(lambda x: score(x, score_hash_2), itertools.product(r(),r(),r(),r(),r(),r()))

scores_matrix = []
probabilities_matrix = []

for x in itertools.product(score_hash, score_hash_2):
    key1 = x[0]
    key2 = x[1]
    if key1 > key2:
        scores_matrix.append(1)
    else:
        scores_matrix.append(0)

for key1 in score_hash:
    for key2 in score_hash_2:
        probability = score_hash[key1]/float(total_rolls) * score_hash_2[key2]/float(total_rolls_2)
        probabilities_matrix.append(probability)
            
print sum(map((lambda x: x[0]*x[1]), zip(scores_matrix, probabilities_matrix)))
