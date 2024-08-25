from cf.classes import *
from cf.util import *
from prettytable import PrettyTable
from colorama import Fore, Style

def user_info(user):
    u1 = User(user['result'][0])
    
    # Creating the table for User Details
    details_table = PrettyTable()
    details_table.field_names = [f"{Fore.RED}User Details{Style.RESET_ALL}", f"{Fore.CYAN}Information{Style.RESET_ALL}"]

    details_table.add_row(["Handle", f"{Fore.CYAN}{u1.handle}{Style.RESET_ALL}"])
    
    if u1.email:
        details_table.add_row(["Email", f"{Fore.CYAN}{u1.email}{Style.RESET_ALL}"])
    
    if u1.firstName and u1.lastName:
        details_table.add_row(["Name", f"{Fore.CYAN}{u1.firstName} {u1.lastName}{Style.RESET_ALL}"])
    elif u1.firstName:
        details_table.add_row(["Name", f"{Fore.CYAN}{u1.firstName}{Style.RESET_ALL}"])
    elif u1.lastName:
        details_table.add_row(["Name", f"{Fore.CYAN}{u1.lastName}{Style.RESET_ALL}"])
    
    if u1.city:
        details_table.add_row(["City", f"{Fore.CYAN}{u1.city}{Style.RESET_ALL}"])
    if u1.country:
        details_table.add_row(["Country", f"{Fore.CYAN}{u1.country}{Style.RESET_ALL}"])
    if u1.organization:
        details_table.add_row(["Organization", f"{Fore.CYAN}{u1.organization}{Style.RESET_ALL}"])

    # Creating the table for Rating Statistics
    rating_table = PrettyTable()
    rating_table.field_names = [f"{Fore.RED}Rating Statistics{Style.RESET_ALL}", f"{Fore.CYAN}Value{Style.RESET_ALL}"]
    
    rating_table.add_row(["Contribution", f"{Fore.CYAN}{u1.contribution}{Style.RESET_ALL}"])
    rating_table.add_row(["Rank", f"{Fore.CYAN}{u1.rank}{Style.RESET_ALL}"])
    rating_table.add_row(["Rating", f"{Fore.CYAN}{u1.rating}{Style.RESET_ALL}"])
    rating_table.add_row(["Max Rank", f"{Fore.CYAN}{u1.maxRank}{Style.RESET_ALL}"])
    rating_table.add_row(["Max Rating", f"{Fore.CYAN}{u1.maxRating}{Style.RESET_ALL}"])
    
    # Print the tables
    print(details_table)
    print("\n")
    print(rating_table)

