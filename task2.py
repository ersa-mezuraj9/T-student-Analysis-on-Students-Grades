"""
Identifying the statistical significance of the difference between the groups of two samples containing Reading Scores and Writing Scores.

H0 = There is no difference between the two groups of scores. (P>0.05)
Ha = There is a difference There is no difference between the two groups of scores.

"""
 
# Import the necessary libraries:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

students = pd.read_csv("C:/Users/User/OneDrive/Desktop/Data Analytics/T student/data/StudentsPerformance.csv")

students_readingscores = students['reading score'].head(30).to_numpy()
students_writingscores = students['writing score'].head(30).to_numpy()

difference_list = students_readingscores - students_writingscores

# Perform the paired sample t-test:
t_stat, p_value = stats.ttest_rel(students_readingscores, students_writingscores)
print("T statistic:", t_stat)
print("P-value:", p_value)

# Interpret the results:
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis; there is a significant difference between the two groups.")
else:
    print("Fail to reject the null hypothesis; there is no significant difference between the two groups.")

plt.show()

