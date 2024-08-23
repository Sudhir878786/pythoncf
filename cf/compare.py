from cf.util import *
from cf.classes import *
from prettytable import PrettyTable as PT
import os

def compare(res):
    res = res['result']
    u1 = User(res[0])
    u2 = User(res[1])
    
    # Create and write data for comparison
    with open('compare_prof.dat', mode='w') as f:
        f.write("@ {},{}\n".format(u1.handle, u2.handle))
        f.write("Rating,{},{}\n".format(u1.rating, u2.rating))
        f.write("Max Rating,{},{}\n".format(u1.maxRating, u2.maxRating))
    
    # Generate termgraph comparison
    os.system('termgraph compare_prof.dat --title "User Comparison" --width 50 --format "{:<.2f}" --suffix " pts" --color "blue red"')

    # Clean up the temporary data file
    if os.name == 'posix':  # Unix-like OS
        os.system('rm compare_prof.dat')
    elif os.name == 'nt':  # Windows
        os.system('del compare_prof.dat')

    # Create PrettyTable objects for user information
    pt = PT()
    pt.field_names = ["Attribute", u1.handle, u2.handle]
    
    # Add rows for each attribute with None handling
    pt.add_row(["Rating", get_colored(str(u1.rating) if u1.rating is not None else 'N/A', 'blue'), get_colored(str(u2.rating) if u2.rating is not None else 'N/A', 'red')])
    pt.add_row(["Max Rating", get_colored(str(u1.maxRating) if u1.maxRating is not None else 'N/A', 'blue'), get_colored(str(u2.maxRating) if u2.maxRating is not None else 'N/A', 'red')])
    pt.add_row(["City", get_colored(u1.city if u1.city is not None else 'N/A', 'blue'), get_colored(u2.city if u2.city is not None else 'N/A', 'red')])
    pt.add_row(["Country", get_colored(u1.country if u1.country is not None else 'N/A', 'blue'), get_colored(u2.country if u2.country is not None else 'N/A', 'red')])
    pt.add_row(["Organization", get_colored(u1.organization if u1.organization is not None else 'N/A', 'blue'), get_colored(u2.organization if u2.organization is not None else 'N/A', 'red')])
    
    # Print user details in tabular format
    print("\n" + get_colored("Comparison Summary:", 'magenta'))
    print(pt)
    
    # Additional textual summary
    print("\n" + get_colored("User 1 ({}):".format(u1.handle), 'cyan'))
    print(" - Rating: " + get_colored(str(u1.rating), 'blue'))
    print(" - Max Rating: " + get_colored(str(u1.maxRating), 'blue'))
    print("\n" + get_colored("User 2 ({}):".format(u2.handle), 'cyan'))
    print(" - Rating: " + get_colored(str(u2.rating), 'red'))
    print(" - Max Rating: " + get_colored(str(u2.maxRating), 'red'))

    print("\n" + get_colored("Graphical comparison generated using termgraph.", 'green'))
