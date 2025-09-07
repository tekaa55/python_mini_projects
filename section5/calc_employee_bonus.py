import pandas

employee_data = pandas.read_excel('employee_data.xlsx')
print(employee_data)  # print out the data table
print(employee_data.head())  # print out the first few lines
print(employee_data.info())  # print out the column information
print(employee_data.describe())  # derscribe salary (mean, count, etc.)

# add new column to data
employee_data['Bonus'] = employee_data['Salary'] * 0.1
print(employee_data)  # print out the data table
print(employee_data.head())  # print out the first few lines
print(employee_data.info())  # print out the column information
print(employee_data.describe())  # derscribe salary (mean, count, etc.)
