from cf.classes import *
from cf.util import *
from prettytable import PrettyTable as PT
from cf.classes import *
from cf.util import *

def contest_list(contests, num):
    contests = contests['result']
    n = len(contests)
    p = []
    for i in range(n):
        p.append(Contest(contests[i]))

    found = False
    for i in range(n):
        if p[i].id == num:
            disp_contest(p[i])
            found = True
            break
    if not found:
        print_head("No Contest with the provided id", 'red')
    
    
def disp_contest(contest):
    # Create a PrettyTable object
    pt = PT()
    
    # Define the table headers
    pt.field_names = [
        get_colored("Field", 'magenta'), 
        get_colored("Value", 'magenta')
    ]
    
    # Define the contest details to display
    details = [
        ("ID", str(contest.id)),
        ("Name", str(contest.name)),
        ("Type", str(contest.type)),
        ("Phase", str(contest.phase)),
        ("Duration", str(seconds_to_hrs(-contest.durationSeconds))),
        ("Start Time", format_date(contest.startTimeSeconds) if contest.startTimeSeconds else "N/A"),
        ("Time Left", seconds_to_hrs(contest.relativeTimeSeconds) if contest.relativeTimeSeconds else "N/A"),
        ("Prepared By", str(contest.preparedBy) if contest.preparedBy else "N/A"),
        ("Website Url", str(contest.websiteUrl) if contest.websiteUrl else "N/A"),
        ("Difficulty", str(contest.difficulty) if contest.difficulty else "N/A"),
        ("Kind", str(contest.kind) if contest.kind else "N/A"),
        ("Description", str(contest.description) if contest.description else "N/A"),
        ("IcpcRegion", str(contest.icpcRegion) if contest.icpcRegion else "N/A"),
        ("Country", str(contest.country) if contest.country else "N/A"),
        ("City", str(contest.city) if contest.city else "N/A"),
        ("Season", str(contest.season) if contest.season else "N/A")
    ]
    
    # Add rows to the table
    for field, value in details:
        pt.add_row([get_colored(field, 'cyan'), get_colored(value, 'cyan')])
    
    # Print the table
    print("\n")
    print_head("Contest Details", 'red')
    print(pt)