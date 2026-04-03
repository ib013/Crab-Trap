"""
File: anova_calc.py
Author: Mohammad Ibrahim Riaz
Date: 2026-03-31
Description: This script runs a one-way ANOVA test for my concentration and contact time tests and prints the f-statistic, p-value, and η².

"""

import numpy as np
from scipy import stats

group1 = [60.00, 50.00, 50.00]    # 100 mg/L
group2 = [76.00, 72.30, 55.00]    # 200 mg/L
group3 = [86.00, 81.50, 80.00]    # 400 mg/L

# ANOVA
f_stat, p_val = stats.f_oneway(group1, group2, group3)

# η² (eta-squared)
all_data = group1 + group2 + group3
grand_mean = np.mean(all_data)
ss_between = sum(len(g) * (np.mean(g) - grand_mean)**2 for g in [group1, group2, group3])
ss_total = sum((x - grand_mean)**2 for x in all_data)
eta_sq = ss_between / ss_total

print(f"Concentration: F = {f_stat:.2f}, p = {p_val:.4f}, η² = {eta_sq:.2f}")

# Contact time groups (at 400 mg/L)
time_5  = [40.00, 55.38, 60.00]
time_10 = [41.67, 55.56, 58.33]
time_15 = [76.00, 84.62, 83.33]
time_25 = [86.00, 81.54, 80.00]

f_stat, p_val = stats.f_oneway(time_5, time_10, time_15, time_25)

all_data = time_5 + time_10 + time_15 + time_25
grand_mean = np.mean(all_data)
ss_between = sum(len(g) * (np.mean(g) - grand_mean)**2 for g in [time_5, time_10, time_15, time_25])
ss_total = sum((x - grand_mean)**2 for x in all_data)
eta_sq = ss_between / ss_total

print(f"Contact Time: F = {f_stat:.2f}, p = {p_val:.4f}, η² = {eta_sq:.2f}")
