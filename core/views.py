from rest_framework.response import Response
from rest_framework import status,generics
from .models import Device
from .serializers import DeviceSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import  get_object_or_404


# @api_view(['GET'])
# def device_list(request):
#     devices=Device.objects.all()
#     serializer= DeviceSerializer(devices,many=True)
#     return JsonResponse({ 'devices':serializer.data})


class DeviceList(generics.ListCreateAPIView):
    queryset =Device.objects.all()
    serializer_class = DeviceSerializer


@api_view(['POST'])
def create(request):
    serializer=DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    

def get_by_id(request, pk):
    device = get_object_or_404(Device, pk=pk)
    serializer= DeviceSerializer(device)
    return JsonResponse({"device": serializer.data})