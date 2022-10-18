src = not False and True or False and not True

# result = True and True or False and False - избавляемся от логического "не"
# result = True or False - избавляемся от логического "и"
# result = True - избавляемся от логического "или"

result = True

print(src == result)
