import shelve
with shelve.open('TestShelve') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = 'Good for making cider'
    print(fruit['apple'])
