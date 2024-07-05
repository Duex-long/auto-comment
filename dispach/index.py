#  任务分发
from openpyxl import load_workbook,Workbook

class Dispach:
    missions = []
    def __init__(self,file_path):
        # df = pd.read_excel(file_path)
        # print(df)
        workbook = load_workbook(file_path)
        print(workbook.sheetnames,'表名')
        sheet = workbook.active
        print(sheet)
        for row in sheet.iter_rows(values_only=True):
            self.missions.append(row)
        print('加载完成')
    

# path = './test.xlsx'
# Dispach(path)