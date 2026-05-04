import pandas as pd

# Pull input file from GitHub
url = "https://raw.githubusercontent.com/Ymallikarjuna27/miniporject/main/data/input_data.csv"
df = pd.read_csv(url)

# Transform the data
df["result"] = df["marks"].apply(lambda x: "Pass" if x >= 70 else "Fail")

average_marks = df["marks"].mean()

# Save output files
df.to_csv("output\\processed_data.csv", index=False)

with open("output\\summary.txt", "w") as f:
    f.write(f"Average Marks: {average_marks}")

print("Data transformed and output generated successfully")