# Last updated: 8/23/2026, 9:43:00 PM
1import pandas as pd
2
3def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
4    employees["salary"] = employees["salary"] * 2
5    return employees