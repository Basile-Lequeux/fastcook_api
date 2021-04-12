import json
from django.http import HttpResponse
import requests



def search_recipes(request):



    ingr = request.GET['ingr']
    url = "https://api.edamam.com/search?q={}%20meat&app_id=9b103c7a&app_key=d23af99b892e026f695ff215031e3ac7".format(ingr)

    response = requests.get(url).json()


    
    recipe_list = []
    for i in response['hits']:

        recipe = {}
        recipe["name"] = i['recipe']['label']
        recipe["url"] = i['recipe']['url']
        recipe["imageUrl"] = i['recipe']['image']
        j = i['recipe']['ingredientLines']
        recipe["ingredients"] = []
        for ingredient in j:
            recipe["ingredients"].append(ingredient)

        recipe_list.append(recipe)

    #print(json.dumps(recipe_list, indent=4))

    return HttpResponse(json.dumps(recipe_list, indent=4), content_type= 'application/json')
