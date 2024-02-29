import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Here our CSV file is in the Data folder
df = pd.read_csv('Data/Banking_Data.csv')

# Display the first few rows of the DataFrame to understand its structure and contents
print("First few rows of the DataFrame:")
print(df.head())

# added to Check for missing values and handle them if necessary
print("Number of missing values in each column:")
print(df.isnull().sum())

# Perform basic data analysis
#  Get the average duration of the calls
average_duration = df['duration'].mean()
print("Average duration of calls:", average_duration)

# to Count the number of calls made in each month
calls_per_month = df['month'].value_counts()
print("Number of calls made in each month:")
print(calls_per_month)

# to Calculate the total number of campaigns conducted
total_campaigns = df['campaign'].sum()
print("Total number of campaigns conducted:", total_campaigns)

# the Group data by 'job' and calculate the average 'duration' for each job
average_duration_per_job = df.groupby('job')['duration'].mean()
print("Average duration of calls per job:")
print(average_duration_per_job)

# to Calculate the total number of calls made on each day of the week
calls_per_day_of_week = df['day_of_week'].value_counts()
print("Number of calls made on each day of the week:")
print(calls_per_day_of_week)

# Data Visualization
# Here i visualize the distribution of call duration using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['duration'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Call Duration')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.show()

# Here i visualize the number of calls made in each month using a bar plot
plt.figure(figsize=(10, 6))
sns.countplot(x='month', data=df, palette='viridis')
plt.title('Number of Calls Made in Each Month')
plt.xlabel('Month')
plt.ylabel('Number of Calls')
plt.xticks(rotation=45)
plt.show()

# Here i visualize the distribution of calls by job title using a box plot
plt.figure(figsize=(10, 8))
sns.boxplot(x='job', y='duration', data=df, palette='pastel')
plt.title('Distribution of Call Duration by Job')
plt.xlabel('Job')
plt.ylabel('Duration (seconds)')
plt.xticks(rotation=45)
plt.show()
