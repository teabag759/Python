for i in range(1, 11):
    with open("./Python/Quiz/Quiz07txt/{0}weeks_report.txt".format(i), "w", encoding="utf8") as report_file:
        # report_file.write(" - " + str([i]) + "주차 주간 보고서 - \n부서: \n이름: \n업무 요약: ")
        report_file.write(" - {0} 주차 주간 보고서 - ".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")



