from cf.util import *
from cf.classes import *
from prettytable import PrettyTable as PT
import pydoc

def userstatus(res):
    res = res['result']
    s = [Submission(r) for r in res]
    
    # Define the table and its headers
    pt = PT()
    headers = ["Problem ID", "Problem Name", "Points", "Language", "Verdict", "TestSet", "Passed Tests", "Time(ms)", "Memory(bytes)"]
    
    # Apply colors to the headers
    headers = [get_colored(header, 'magenta') for header in headers]
    pt.field_names = headers
    
    # Add rows to the table
    for i in s:
        pid = str(i.problem.contestId) + str(i.problem.index)
        pname = str(i.problem.name)
        points = str(i.problem.points)
        lang = str(i.programmingLanguage)
        verd = str(i.verdict)
        ts = str(i.testset)
        ptest = str(i.passedTestCount)
        time = str(i.timeConsumedMillis)
        mem = str(i.memoryConsumedBytes)
        
        # Colorize row data
        row = [pid, pname, points, lang, verd, ts, ptest, time, mem]
        row_colors = ['cyan'] * len(row)
        
        # Apply specific colors based on conditions
        if 'OK' in verd:
            row_colors[0] = 'green'
            row_colors[1] = 'green'
            row_colors[2] = 'green'
            row_colors[3] = 'green'
            row_colors[4] = 'green'
            row_colors[5] = 'green'
            row_colors[6] = 'green'
            row_colors[7] = 'green'
            row_colors[8] = 'green'

        elif 'WRONG_ANSWER' in verd:
            row_colors[0] = 'red'
            row_colors[1] = 'red'
            row_colors[2] = 'red'
            row_colors[3] = 'red'
            row_colors[4] = 'red'
            row_colors[5] = 'red'
            row_colors[6] = 'red'
            row_colors[7] = 'red'
            row_colors[8] = 'red'
        elif 'COMPILATION_ERROR' in verd:
            row_colors[0] = 'blue'
            row_colors[1] = 'blue'
            row_colors[2] = 'blue'
            row_colors[3] = 'blue'
            row_colors[4] = 'blue'
            row_colors[5] = 'blue'
            row_colors[6] = 'blue'
            row_colors[7] = 'blue'
            row_colors[8] = 'blue'
        else:
            row_colors[4] = 'orange'
        
        # Add row to table with colors
        colored_row = [get_colored(item, color) for item, color in zip(row, row_colors)]
        pt.add_row(colored_row)
    
    # Display the table
    pydoc.pager(pt.get_string())
