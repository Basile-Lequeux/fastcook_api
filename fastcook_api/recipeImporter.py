from service import models


# parcourir la liste
# selectionner les ingredients qui existent dans notre base
# ajouter la recette dans notre base avec les ingredients selectionnés

allIngredients = models.Ingredient.objects.all()

def recipeImporter(recipe):
    ingredientList = []
    for i in recipe['ingredients']:
        for all in allIngredients:
            if all.name in i:
                ingredientList.append(all)

    r = models.Recipe(name=recipe['name'], url=recipe['url'], imageUrl=recipe['imageUrl'], totalTime=recipe['totalTime'])
    r.save()
    for i in ingredientList:
        r.ingredients.add(i)
        r.save()

