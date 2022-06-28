from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TalabaSerializer
from .models import Talaba

# Create your views here.
@api_view(['GET', 'POST'])
def test_get(request):
    talaba = Talaba.objects.all()
    serializer = TalabaSerializer(talaba, many=True)
    return Response({'status': 200, 'data': serializer.data})


@api_view(['POST', 'GET'])
def test_post(request):
    serializer = TalabaSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 403, 'message': 'Xatolik yuz berdi'})
    serializer.save()
    return Response({'status': 200, 'data':serializer.data, 'message': "Ma'lumot olindi"})


@api_view(['PUT', 'GET'])
def test_put(request, id):
    talaba = Talaba.objects.get(id=id)
    try:
        serializer = TalabaSerializer(talaba, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status': 403, 'message': 'Xatolik yuz berdi'})
        serializer.save()
        return Response({'status': 200, 'data': serializer.data, 'message': "Ma'lumot olindi"})
    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'Xato id!!!'})

@api_view(['DELETE', 'GET'])
def test_delete(request, id):
    talaba = Talaba.objects.get(id=id)
    talaba.delete()
    return Response({'status': 200, 'message': "Ma'lumot o'chirildi"})

