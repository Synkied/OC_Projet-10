from random import randint


results = {"search_results": {}}
search_results = {"count": 2, "products": [{"name": "a", "code": 1}, {"name": "b", "code": 2}]}

search_results_2 = {"count": 2, "products": [{"name": "c", "code": 3}, {"name": "d", "code": 4}]}

for i in range(10):
    rand = randint(0, 5)
    if "products" in results["search_results"]:
        results["search_results"]["products"].append(rand)

    else:
        results["search_results"] = search_results




for product in results["search_results"]["products"]:
    print(product)
