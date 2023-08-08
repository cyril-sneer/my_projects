JOE_HAMBURGERS = {'name':"Joe's hamburgers", 'vegetarian':False, 'vegan':False, 'no_gluten':False, 'acceptable':True}
CENTRAL_PIZZA = {'name':'Central pizza', 'vegetarian':True, 'vegan':False, 'no_gluten':True, 'acceptable':True}
CORNER_CAFE = {'name':'Corner cafe', 'vegetarian':True, 'vegan':True, 'no_gluten':True, 'acceptable':True}
ITALIAN_MUM = {'name':'Italian mum', 'vegetarian':True, 'vegan':False, 'no_gluten':False, 'acceptable':True}
CHIEF_KITCHEN = {'name':"Chief's kitchen", 'vegetarian':True, 'vegan':True, 'no_gluten':True, 'acceptable':True}
CAFES = (JOE_HAMBURGERS, CENTRAL_PIZZA, CORNER_CAFE, ITALIAN_MUM, CHIEF_KITCHEN)

vegetarians = False
vegans = False
gluten_sensitive = False

if input('Будут ли вегетарианцы? yes/no: ') == 'yes': vegetarians = True
if input('Будут ли веганы? yes/no: ') == 'yes': vegans = True
if input('Будут ли безглютенцы? yes/no: ') == 'yes': gluten_sensitive = True

acceptable_cafes = []

for cafe in CAFES:
    if vegetarians:
        if not cafe['vegetarian']: cafe['acceptable'] = False
    if vegans:
        if not cafe['vegan']: cafe['acceptable'] = False
    if gluten_sensitive:
        if not cafe['no_gluten']: cafe['acceptable'] = False
    if cafe['acceptable']: acceptable_cafes.append(cafe)

print('Допустимые кафе:')
for cafe in acceptable_cafes:
    print(cafe['name'], end = ', ')