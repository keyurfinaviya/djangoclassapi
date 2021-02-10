from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
	
	def start(value):
		if value[0] == value[0].lower():
			raise serializers.ValidationError('first letter should be capital')
 

	class Meta:

		model = Student
		fields = ['name','roll','city']
		