import pandas as pd

# Load sample dataset
data = pd.read_csv("muscle_data.csv")

print("Physiotherapy Muscle Data Overview:\n")
print(data)

# Example 1: filter muscles linked to back pain
back_pain_related = data[data["Common Issues"].str.contains("back pain", case=False)]
print("\nMuscles linked to back pain:")
print(back_pain_related)

# Example 2: show muscles important for posture
posture_related = data[data["Clinical Relevance"].str.contains("posture", case=False)]
print("\nMuscles important for posture:")
print(posture_related)

# Example 3: list notes mentioning 'athletes'
athlete_related = data[data["Notes"].str.contains("athlete", case=False)]
print("\nMuscles commonly injured in athletes:")
print(athlete_related)
