from cf.util import *
from cf.classes import *
from prettytable import PrettyTable as PT

def ratingchange(res):
    res = res['result']
    rc = [RatingChange(r) for r in res]
    
    # Create a PrettyTable object
    pt = PT()
    
    # Define the table headers
    pt.field_names = [
        get_colored("Rank", 'blue'),
        get_colored("Handle", 'blue'),
        get_colored("Old Rating", 'blue'),
        get_colored("New Rating", 'blue'),
        get_colored("Delta", 'blue')
    ]
    
    # Add rows to the table
    for r in rc:
        rank = str(r.rank)
        handle = r.handle
        old_rating = format_rating(r.oldRating)
        new_rating = format_rating(r.newRating)
        delta = calculate_delta(r.oldRating, r.newRating)
        pt.add_row([rank, handle, old_rating, new_rating, delta])
    
    # Header for the table
    header = get_colored('Rating Changes for contest: ' + str(rc[0].contestId) + " " + rc[0].contestName, 'magenta') + "\n\n"
    
    # Print the header and the table
    print(header)
    print(pt)

def format_rating(rating):
    """Formats the rating value with color."""
    return get_colored(f'{rating}', 'cyan')

def calculate_delta(old_rating, new_rating):
    delta = new_rating - old_rating
    if delta > 0:
        return get_colored(f'+{delta}', 'green')
    elif delta < 0:
        return get_colored(f'{delta}', 'red')
    else:
        return get_colored('0', 'white')

def ratc(res):
    ratingchange(res)

def rath(res, han):
    found = False
    for r in res['result']:
        if r['handle'] == han:
            r = RatingChange(r)
            # Create a PrettyTable object
            pt = PT()
            
            # Define the table headers
            pt.field_names = [
                get_colored("Rank", 'blue'),
                get_colored("Handle", 'blue'),
                get_colored("Old Rating", 'blue'),
                get_colored("New Rating", 'blue'),
                get_colored("Delta", 'blue')
            ]
            
            # Add the row to the table
            rank = str(r.rank)
            handle = r.handle
            old_rating = format_rating(r.oldRating)
            new_rating = format_rating(r.newRating)
            delta = calculate_delta(r.oldRating, r.newRating)
            pt.add_row([rank, handle, old_rating, new_rating, delta])
            
            # Print the table
            print(pt)
            found = True
            break
    if not found:
        print(get_colored('\nUser did not participate in contest', 'red'))
