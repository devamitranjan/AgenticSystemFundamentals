import pandas as pd

df = pd.read_csv("employees.csv")

x = df[df["Salary"] > 100000] #filter dataframe df[], df["Salary"] > 100000

#print(x)



#EmployeeID,Name,Department,Age,Experience,Salary,PerformanceScore,Remote,JoinYear
#101,Alice,AI,28,3,70000,88,True,2021. #false
#102,Bob,Backend,35,8,120000,92,False,2016 #true
#103,Charlie,AI,30,5,95000,85,True,2019 # false
#104,David,Frontend,25,2,60000,78,False,2022 # false
#105,Eva,AI,40,12,150000,95,True,2013 #true
#106,Frank,Backend,29,4,80000,82,False,2020 # false
#107,Grace,Frontend,31,6,90000,89,True,2018 #false
#108,Hannah,AI,27,3,72000,91,True,2021 #false


# give me all employees whose departmant is AI


y = df[df["Department"] == "AI"]
#print(y)


# Employees in AI and Salary > 80000. , &


z = df[(df["Department"]== "AI") & (df["Salary"] > 80000)]
#print(z)



# Give me all employees whose department is AI or backend  | 
# df --> complete data

#a= df[ # filter out department which is AI or Backend]
# a = df[(condition 1) | (condition2)]
# condiont df["Department"] == "AI"
# condtion  df["Department"] == "Backend"


a = df[(df["Department"] == "AI") | (df["Department"] == "Backend")]
#print(a)


# a = df[#not department = "frontend"]. ~


b = df[(df["Department"] != "Frontend")]
print(b)