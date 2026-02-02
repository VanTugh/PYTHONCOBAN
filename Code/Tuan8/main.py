import pandas as pd
from pandas import DataFrame
def luu_data():
    data ={
        'EmployeeID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie','David', 'Eva'],
        'Age': [28, 34, 29, 42, 30],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing'],
        'Salary': [50000, 60000, 55000, 70000, 90000]
    }
    df = pd.DataFrame(data, columns=['EmployeeID', 'Name', 'Age', 'Department', 'Salary'])
    return df
def tim_kiem(df , employee_name):
    result  = df[df['Name'] == employee_name]
    if not result.empty:
        return True
    else:
        df.loc[len(df)] = [
            '6', 'Frank', 28, 'Marketing', 65000
        ]
        return False
def sua_TT(df, employee_id, new_salary, new_department):
    result = df[df['EmployeeID'] == employee_id]
    if not result.empty:
        df.loc[df['EmployeeID'] == employee_id, 'Salary'] = new_salary
        df.loc[df['EmployeeID'] == employee_id, 'Department'] = new_department
        return True
    else:
        return False
def xoa_TT(df : DataFrame, employee_id):
    result = df[df['EmployeeID'] == employee_id]
    if not result.empty:
        df.drop(df[df['EmployeeID'] == employee_id].index,inplace=True)
        return True
    else :
        return False
def main():
    df = luu_data()
    print("DataFrame:")
    print(df)

    check = tim_kiem(df, 'Frank')
    if check:
        print("Employee found in the DataFrame.")
    else:
        print("Employee not found. New employee added.")
        print("Updated DataFrame:")
        print(df)
    
    update = sua_TT(df, 3, 75000, 'HR')
    if update:
        print("Employee information updated.")
        print("Updated DataFrame:")
        print(df)
    else:
        print("Employee ID not found. No updates made.")

    remove = xoa_TT(df,4)
    if remove:
        print("Employee information removed.")
        print("Updated DataFrame:")
        print(df)
    else:
        print("Employee ID not found. No updates made.")
if __name__ == "__main__":
    main()