SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1
FLOUR_RECIPE = 2.75
COOKIES_RECIPE = 48

cookies = int(input('How many cookies do you want to bake?... '))

sugar = SUGAR_RECIPE / COOKIES_RECIPE * cookies
butter = BUTTER_RECIPE / COOKIES_RECIPE * cookies
flour = FLOUR_RECIPE / COOKIES_RECIPE * cookies

print(f'Ok, you need: \n'
      f'\t{sugar:.2f} glasses of sugar \n'
      f'\t{butter:.2f} glasses of butter \n'
      f'\t{flour:.2f} glasses of mill'
      )
