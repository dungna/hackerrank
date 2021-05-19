"""
URL: https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
Here are the test scores of 10 students in physics and history:
Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.
Output Format
In the text box, using the language of your choice, print the floating point/decimal value required. Do not leave any leading or trailing spaces.
For example, if your answer is 0.255. In python you can print using
"""

# CACH 1
from scipy.stats import pearsonr
physics_scores =[15,12,8,8,7,7,7,6,5,3]
history_scores = [10,25,17,11,13,17,20,13,9,15]
corr,_ = pearsonr(physics_scores, history_scores)
print('Pearsons correlation:%.3f' % corr)


# CACH 2
import math
import numpy as np
physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
p_mean = np.mean(physics)
h_mean = np.mean(history)

tu_so_physics = [p - p_mean for p in physics]
tu_so_history = [h - h_mean for h in history]
tu_so = 0
for p, h in zip(tu_so_physics, tu_so_history):
    tu_so += p*h

mau_physics = sum([p**2 for p in tu_so_physics])
mau_history = sum([h**2 for h in tu_so_history])
mau_so = math.sqrt(mau_physics*mau_history)

r = tu_so/mau_so
print(round(r, 3))

# CACH 3
import math

hs_score = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
ps_score = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
n = len(hs_score)
total_1, total_2a, total_2b = 0, 0, 0

avgHsScore = sum(hs_score)/n
avgPsScore = sum(ps_score)/n

for i in range(n):
    total_1 += (hs_score[i] - avgHsScore) * (ps_score[i] - avgPsScore)
    total_2a += (ps_score[i] - avgPsScore) * (ps_score[i] - avgPsScore)
    total_2b += (hs_score[i] - avgHsScore) * (hs_score[i] - avgHsScore)

r = round(total_1/(math.sqrt(total_2a*total_2b)), 3)

print(r)
