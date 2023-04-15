from django.shortcuts import redirect
from .models import Profile, Hobby
from .serializer import ProfileSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.db.models import Prefetch
# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.prefetch_related(Prefetch('user_hobby', queryset=Hobby.objects.all()))
    serializer = ProfileSerializer(queryset, many=True)