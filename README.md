# Data7
The data given to us is a set of weights (in kilograms) of newborn babies. I loaded this data from a CSV file named 'data7.csv' using NumPy's loadtxt() function and stored it in an array named df_new_born. I then analyzed the distribution of the weights and calculated the mean weight, the 75th percentile weight, and the standard deviation using NumPy.
To describe the distribution of the data, I created a histogram of the newborn weights using Matplotlib's hist() function. The resulting distribution appears to be slightly skewed to the right, indicating that there may be some heavier newborns in the sample.
To calculate the mean weight of the newborns, I used the formula: mean = sum(weights) / n where weights is the array of weights, n is the number of weights in the array, and sum() is a function that adds up all the weights in the array. Using NumPy's mean() function, I obtained an average weight of 3.20 kg.
To calculate the 75th percentile weight of the newborns, I used NumPy's percentile() function with an argument of 75, indicating that we want to find the value that is greater than or equal to 75% of the values in the array. Mathematically, we can express this as: X = P(75) where X is the required value and P(75) is the 75th percentile of the data. Using NumPy's percentile() function, we obtained a value of 3.65 kg for X.
The standard deviation of the newborn weights is 0.53 kg. This value indicates how much the weights of the newborns vary from the mean weight, and provides a measure of the spread or dispersion of the data.
Overall, the distribution of the newborn weights appears to be slightly skewed to the right, with an average weight of 3.20 kg, a 75th percentile weight of 3.65 kg, and a standard deviation of 0.53 kg. These values suggest that there may be some heavier newborns in the sample, but the majority of the babies have weights around 3 kg.
In addition to this report, several color-related parameters are used to customize the appearance of the plot in the code: edgecolor='black', color='lightblue', color='red', color='green', and linestyle='dashed'. These parameters help to visually distinguish the di erent elements of the plot and make it easier to interpret the data. The legend also provides labels for the di erent components of the plot, further enhancing its clarity.
