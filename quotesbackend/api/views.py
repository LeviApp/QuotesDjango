from rest_framework.response import Response
from rest_framework.decorators import api_view
from quotesbackend.models import Quotes
from quotesbackend.api.serializers import QuotesSerializer
from django.http import HttpResponse
from rest_framework import status

@api_view(['GET'])
def working_api(request):

        return Response({ "message": "api is working"})

@api_view(['GET', 'POST'])
def quotes_api(request):
    try:
        quotes = Quotes.objects.all()
    except Quotes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuotesSerializer(quotes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuotesSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer, 'is valid')
            serializer.save()
        else:
            print('it isnt valid!', serializer.errors)
        return Response(serializer.data)



@api_view(['GET', "PATCH", "DELETE"])
def quote_api(request, pk):
    try:
        quote = Quotes.objects.get(id=pk)
    except Quotes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuotesSerializer(quote, many=False)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = QuotesSerializer(quote, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        quote.delete()    
        return Response({ "message": "Quote Deleted"})
