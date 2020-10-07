# $100 bought 100 (mix of roosters, hens, chicks), a rooster cost $5, a hen cost $3, 3 chicks cost $1. 
# Q: how many roosters, hens and chicks.
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print(f'roosters: {x}, hens: {y}, chicks: {z}')
