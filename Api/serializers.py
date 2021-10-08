from rest_framework import serializers
from .models import Course, Difficulty, MathQ, Info, Withdraw

#'id', 'course','difficulty', 
class CourseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id','name')

class DifficultySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Difficulty
        fields = ('id','name')

class MathQSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MathQ
        fields = ('question' ,'option1' ,'option2' ,'option3' ,'answer')

class InfoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class WithdrawSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('account' ,'amount' ,'method')

