"""
H0 = There is no difference between the mean Math Scores of Male and Female Students. (P>0.05)
Ha = There is a difference between the mean Math Scores of Male and Female Students.

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
from scipy import stats

# Load the Iris dataset:
students = pd.read_csv("C:/Users/User/OneDrive/Desktop/Data Analytics/T student/data/StudentsPerformance.csv")

studentsGroupBy = students.groupby("gender")

# Filter the dataset for the two gender we want to compare:
female_mathscores = studentsGroupBy.get_group('female')["math score"][:30]
male_mathscores = studentsGroupBy.get_group('male')["math score"][:30]

# Descriptive statistics
print(female_mathscores.describe())
print(male_mathscores.describe())
print("===================================================================")
# The Shapiro–Wilk's test of normality
print("The Shapiro–Wilk's test of normality")
print(stats.shapiro(female_mathscores))
print(stats.shapiro(male_mathscores))
plt.figure(figsize=(10,10))
plt.subplot(121)
sns.histplot(female_mathscores, kde=True)
plt.subplot(122)
sns.histplot(male_mathscores, kde=True)
print("===================================================================")
# Perform the independent sample t-test:
t_stat, p_value = stats.ttest_ind(female_mathscores, male_mathscores)
print("T statistic:", t_stat)
print("P-value:", p_value)

# Interpret the results:
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis; there is a significant difference between the mean Math Scores of Male and Female Students.")
else:
    print("Fail to reject the null hypothesis; there is no significant difference between the mean Math Scores of Male and Female Students.")

plt.show()


