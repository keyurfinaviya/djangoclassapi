from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPI(APIView):
	def get(self,request, format = None, id = None):
		if id is not None:
			stu = Student.objects.get(id = id)
			serial = StudentSerializer(stu)
			return Response(serial.data)
		stu = Student.objects.all()
		serial = StudentSerializer(stu,many=True)
		return Response(serial.data)

	def post(self,request, format=None):
		serial = StudentSerializer(data = request.data)
		if serial.is_valid():
			serial.save()
			return Response({'msg':'data Created'},status = status.HTTP_201_CREATED)
		return Response(serial.errors)

	def put(self, request, format=None, id=None):
		stu = Student.objects.get(id = id)
		serial = StudentSerializer(stu,data=request.data)
		if serial.is_valid():
			serial.save()
			return Response({'msg':' Complete data updated'})
		return Response(serial.errors)

	def patch(self,request, format = None, id = None):
		stu = Student.objects.get(id = id)
		serial = StudentSerializer(stu,data=request.data,partial =True)
		if serial.is_valid():
			serial.save()
			return Response({'msg':' Partial data updated'})
		return Response(serial.errors)

	def delete(self,request, format = None, id = None):
		stu  = Student.objects.get(id =id)
		stu.delete()
		return Response({'msg' : 'DATA DELETED'})



		
		
