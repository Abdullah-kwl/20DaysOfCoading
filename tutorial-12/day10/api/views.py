from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'message': 'This is GET request'}, headers={'Content-Type': 'application/json'})
    elif request.method == 'POST':
        return Response({'message': 'This is POST request'}, headers={'Content-Type': 'application/json'})
