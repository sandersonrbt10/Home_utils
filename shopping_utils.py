


acme_org_dict = {}
aldi_org_dict = {"broccoli":1.0,"cilantro":1.0,"fresh cilantro":1.0,"brussels sprouts":1.0,"brussel sprouts":1.0,"bag salad (greek or garden)":1.0,"bagged salad":1.0,"bag salad":1.0,"carrots":1.0,"celery":2.5,"cucumber":2.5,"mini cucumber":2.5,"red refresh":99,
                 "green beans":1.0,"lettuce":1.0,"onions":2.5,"peppers":2.5,"balsamic vinaigrette":2.5,
                 "potatoes":2.5,"spinach":1.0,"tomatoes":2.5,"tomato":2.5,"zucchini":2.5,"berries":1.0,
                 "apples":1.0,"bananas":1.0,"grapes":1.0,"oranges":1.0,"clementines":1.0,"asparagus":1.0,
                 "peaches":1.0,"pineapple":1.0,"strawberries":1.0,"pomegranate plum juice":2.0,
                 "blueberries":1.0,"cherries":1.0,"grapefruit":1.0,
                 "kiwi":1.0,"lemons":1.0,"limes":1.0,"mango":1.0,
                 "nectarines":1.0,"pears":1.0,"plums":1.0,"raspberries":1.0,
                 "bread":1.5,"wheat bread":1.5,"bagels":1.5,"pita bread":1.5,"buns":1.5,"hot dog buns":1.5,
                 "hamburger buns":1.5,"burger buns":1.5,"rolls":1.5,"chips":1.5,"crackers":1.5,
                 "goldfish":1.5,"graham crackers":1.5,"pretzels":1.5,
                 "tortilla chips":1.5,"chicken":1.9,"ground beef":1.9,"rotisserie chicken":1.9,
                 "pork chops":1.9,"steak":1.9,"chicken breast":1.9,"pork tenderloin":1.9,"salmon":1.9,"whole chicken":1.9,
                 "coffee":2.0,"tea":2.0,"cereal":2.0,"granola":2.0,"decaf":2.0,
                 "decaf coffee":2.0,"cereal bars":2.0,"cheerios":2.0,"corn flakes":2.0,
                 "frosted flakes":2.0,"frosted mini wheats":2.0,"froot loops":2.0,
                 "wheat chex":99,"garlic":2.5,"ginger":2.5,"mustard":2.5,"salad dressing":2.5,
                 "soy sauce":2.5,"ketchup":2.5,"mayonnaise":2.5,"olive oil":2.5,"jalapenos":2.5,
                 "jalepeno peppers":2.5,"bell peppers":2.5,"salad":1.0,"green peppers":2.5,
                 "red peppers":2.5,"yellow peppers":2.5,"avocado":1.0,"peanuts":2.5,"almonds":2.5,
                 "cashews":2.5,"pecans":2.5,"walnuts":2.5,"peanut butter":2.5,"jam":2.5,
                 "preserves":2.5,"peach preserves":2.5,"strawberry preserves":2.5,"jelly":2.5,
                 "sausage":1.9,"kielbasa":1.9,"hot italian sausage":1.9,"turkey":3.9,"turkey breast":3.9,
                 "salami":3.9,"ham":3.9,"sliced cheese":3.9,"string cheese":3.9,"cheddar cheese":3.9,"swiss cheese":3.9,
                 "cheese sticks":3.9,"cheese slices":3.9,"american cheese":3.9,"mozzarella cheese":3.9,
                 "toilet paper":3.5,"paper towels":3.5,"tissues":3.5,"toilet bowl cleaner":3.5,
                 "laundry detergent":3.5,"dish soap":3.5,"dishwasher detergent":3.5,
                 "dishwasher pods":3.5,"tin foil":3.5,"aluminum foil":3.5,"foil":3.5,"dog food":3.5,
                 "flour":4.0,"sugar":4.0,"brown sugar":4.0,"powdered sugar":4.0,"salt":4.0,
                 "beans":4.0,"black beans":4.0,"kidney beans":4.0,"pinto beans":4.0,
                 "refried beans":4.0,"canelini beans":4.0,"rice":4.0,"brown rice":4.0,
                 "canned corn":4.0,"canned green beans":4.0,"canned peas":4.0,"canned tomatoes":4.0,
                 "tomato sauce":5.5,"pasta":5.5,"tortillas":5.5,"big tortillas":5.5,"taco seasoning":5.5,"orzo":5.5,"macaroni":5.5,"spaghetti":5.5,"noodles":5.5,
                 "rigatoni":5.5,"lasagna noodles":5.5,"angel hair pasta":5.5,"egg noodles":5.5,
                 "pesto":5.5,"parmesan cheese":4.9,"parmesan":4.9,"guacamole":4.9,"prosciutto":4.9,
                 "cream cheese":6.0,"buttermilk":6.0,"milk":6.0,"eggs":6.0,"yogurt":6.0,"butter":6.0,
                 "cream":6.0,"sour cream":6.0,"heavy cream":6.0,"whipping cream":6.0,
                 "half and half":6.0,"creamer":6.0,"gogurt":6.0,"go-gurt":6.0,"yoplait":6.0,"yogurt tubes":6.0,
                 "orange juice":6.0,"almond milk":6.0,"soy milk":6.0,"chicken nuggets":6.5,
                 "chicken tenders":6.5,"chicken fingers":6.5,"frozen chicken":6.5,
                 "frozen chicken breasts":6.5,"perogies":6.5,"pierogies":6.5,"hot dogs":6.5,"frozen pizza":6.5,"hamburgers":6.5,"burgers":6.5,"hash browns":6.5,
                 "ice cream":6.5,"frozen vegetables":6.5,"frozen corn":6.5,"frozen peas":6.5,
                 "cod fillets":6.5,"cod":6.5,"tilapia fillets":6.5,"tilapia":6.5,"hamburger":6.5,
                 "meatballs":6.5,"frozen meatballs":6.5,"swedish meatballs":6.5,"frozen waffles":6.5,
                 "baby puree":1.5,"good bagels":99,"greek yogurt":6.0,"probiotic yogurt":6.0,
                 "cooking spray":4.0,"lobster":6.5,"spaghetti sauce":5.5,"pasta sauce":5.5,}

org_cmd_dict = {"ALDI":aldi_org_dict,
                "ACME":acme_org_dict}


def get_shopping_list_id(ourgroc_lists,
                         list_type):
    """takes an ourgroc json item and pulls out a list with the
    name matched by the list type input"""
    for item in ourgroc_lists:
        if item['name'] == list_type:
            return item['id']
    return None


def organize_grocery_list(grocery_list, dictval):
    """iterates through grocery list makes all items lowercase
    and returns a list of items sorted by their dictionary value"""
    grocery_dict\
        = org_cmd_dict[dictval]
    grocery_list = [item.lower().replace(" -- ","~").split("~")[-1] for item in grocery_list]
    grocery_list = [item.lower().replace("?","") for item in grocery_list]
    print(grocery_list)

    #iterate through grocery list and try to sort by dictionary value unless missing then add to end
    sorted_grocery_list = []
    for item in grocery_list:
        try:
            sorted_grocery_list.append((grocery_dict[item.split("(")[0].strip()],
                                        str(grocery_dict[item.split("(")[0].strip()]) + " -- " + item))
        except KeyError:
            sorted_grocery_list.append((-1, '?'+item))
    return [x[1] for x in sorted(sorted_grocery_list)]


def get_list_items(ourgroc_lists, crossstatus=False):
    """takes an ourgroc json item and pulls out a list with the
    list items that match the crossed status"""
    outlist = [x['name'] for x in ourgroc_lists['list']['items'] \
               if x['crossedOff'] == crossstatus]
    outids = [x['id'] for x in ourgroc_lists['list']['items'] \
               if x['crossedOff'] == crossstatus]
    return outlist,outids
