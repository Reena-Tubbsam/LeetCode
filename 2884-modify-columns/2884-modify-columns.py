import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    return employees.assign(salary=employees.salary*2)