import pandas as pd

# Load sample dataset
data = pd.read_csv("muscle_data.csv")

# Print summary
print("Physiotherapy Muscle Data Overview:")
print(data)

# Example: filter muscles linked to back pain
back_pain_related = data[data["Common Issues"].str.contains("back pain", case=False)]
print("\nMuscles linked to back pain:")
print(back_pain_related)
