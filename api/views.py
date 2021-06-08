from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('user-list', request=request, format=format),
        'recipe': reverse('recipe-list', request=request, format=format),
        'ingredient': reverse('ingredient-list', request=request, format=format)
    })

