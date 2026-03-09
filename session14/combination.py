import pandas as pd

df = pd.read_csv("employees.csv")

#give me all employess whose deplartment is AI  and salary > 80000 
# show only name and salary
# descending order of salary

# Give me name and salary of all employess in descending order of salary whose departmet is AI
# and saalry is 8000


result = df[(df["Department"] == "AI") & (df["Salary"] > 80000)]
#result_2 = result[["Name", "Salary"]]
result_3 = (df[(df["Department"] == "AI") & (df["Salary"] > 80000)]
            [["Name", "Salary"]]
            .sort_values("Salary", ascending=False))
print(result_3)