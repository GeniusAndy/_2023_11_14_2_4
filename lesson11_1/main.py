import pyinputplus as pyip
import tools

if __name__ == '__main__':
    s_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
    o_nums:int = pyip.inputInt("請輸入科目數(1~7):",min=1,max=7)
    students:list[list] = tools.getStudents(student_nums=s_nums,scores_nums=o_nums)
    fileName = pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名稱):")
    if tools.saveToCSV(fileName=fileName,data=students,subjects_nums=o_nums):
        print("存檔成功")
    else:
        print("存檔失敗")