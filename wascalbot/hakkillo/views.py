import json
from django.db.models.query import QuerySet
from django.http import HttpResponse, response
from django.shortcuts import render
from backend.main import chat
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from hakkillo.models import intent
from hakkillo.serializers import intentSerializer






class chatbotViews(APIView):
	def get(self, request, *arg, **kwargs):
		# // recuperatuin d la question de lutilisateur
		queryset = request.GET.get('msg')
		# exectuion de l'IA pour recuperer la reponse
		reponse = chat(queryset)
		# retour de la reponse
		
		# return Response(request.GET.get('msg'))
		
		return Response(reponse)


class mainpage(TemplateView):
	Template_view="hakkillo/index.html"

	def get(self,request):
		return render(request,self.Template_view)

	def post(self,request):
		if request.method == 'POST':
			command = request.POST.get('input',False)
			context={"bot":chat(command)}
			print(context)
		return render(request,self.Template_view,context)

class intentAPIView(APIView):
	def get(self, *args, **kwargs):
		intents=intent.objects.all() 
		serializer = intentSerializer(intents, many=True)
		return Response(serializer.data)