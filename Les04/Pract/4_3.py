def lang_genoeg(x):
    if 120 <= x:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')

lengte = eval(input('Geef je lengte: '))
lang_genoeg(lengte)
