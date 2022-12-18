import asyncio
from ourgroceries import OurGroceries
import argparse
import shopping_utils

#Add arguments to the command line
parser = argparse.ArgumentParser(
                    prog = 'Grocery List organizer',
                    description = 'Pulls a list of items from a grocery '
                                  'list and organizes them by aisle')
parser.add_argument('-u', '--username',
                    help='Username for OurGroceries',
                    required=True)
parser.add_argument('-p', '--password',
                    help='Password for OurGroceries',
                    required=True)
parser.add_argument('-og', '--organize_groceries',
                    help='pass in a grocery store name to '
                    'organize based on store layout',
                    choices=["ALDI", "ACME"],
                    required=False)
args = parser.parse_args()

#Pull in ourgroceries data
og = OurGroceries(args.username, args.password)
loop = asyncio.get_event_loop()
loop.run_until_complete(og.login())
my_lists = loop.run_until_complete(og.get_my_lists())

#Pull in the shopping list of interest
if args.organize_groceries:
    id = shopping_utils.get_shopping_list_id(my_lists['shoppingLists'],
                                             'Groceries')
    raw_grocery_list = loop.run_until_complete(og.get_list_items(list_id=id))

    #Organize the list and remember the API ids as another list
    grocery_list, outids = shopping_utils.get_list_items(raw_grocery_list)
    shop_list = shopping_utils.organize_grocery_list(grocery_list,
                                                     args.organize_groceries)

    #Update the list with the new order after removing the old items
    for item in outids:
        loop.run_until_complete(og.remove_item_from_list(id,item))
    loop.run_until_complete(og.add_items_to_list(id,shop_list))
