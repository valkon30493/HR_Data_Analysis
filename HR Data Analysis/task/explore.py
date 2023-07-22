import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
# Objective 1
A_office_data = pd.read_xml("../Data/A_office_data.xml")
B_office_data = pd.read_xml("../Data/B_office_data.xml")
HR_data = pd.read_xml("../Data/hr_data.xml")

# Objective 3
A_office_data.set_index('employee_office_id', inplace=True)
A_office_data.set_index("A" + A_office_data.index.astype(str), inplace=True)
B_office_data.set_index('employee_office_id', inplace=True)
B_office_data.set_index("B" + B_office_data.index.astype(str), inplace=True)
HR_data.set_index('employee_id', inplace=True)

# Objective 4
office_data = pd.concat([A_office_data, B_office_data])

# Objective 5
unified_dataset = office_data.merge(HR_data, how='inner', left_index=True, right_index=True, indicator=True)

# Objective 6
unified_dataset.drop(columns=['_merge'], axis=1, inplace=True)

# Objective 7
unified_dataset.sort_index(inplace=True)


# Objective 8
def count_bigger_5(column_data, threshold):
    bigger_5 = column_data[column_data > threshold].count()
    return bigger_5

# Objective 9
result_table = unified_dataset.groupby('left').agg\
    ({'number_project': ['median', lambda x: count_bigger_5(x, 5)],
        'time_spend_company': ['mean', 'median'],
        'Work_accident': ['mean'],
        'last_evaluation': ['mean', 'std']})

result_table.rename(columns={'<lambda_0>': 'count_bigger_5'}, inplace=True)

# Objective 10
result_dict = result_table.round(2).to_dict()
print(result_dict)