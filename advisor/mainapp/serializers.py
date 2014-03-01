from rest_framework import serializers
from mainapp.models import Trajectory, Program, Major, Minor, GenEd, Concentration, MetaCourse, Course, CourseGroup

class TrajectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajectory

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major

class MinorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minor

class GenEdSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenEd

class ConcentrationSerializer(serializer.ModelSerializer):
    class Meta:
        model = Concentration

class MetaCourseSerializer(serializer.ModelSerializer):
    class Meta:
        model = MetaCourse

class CourseSerializer(serializer.ModelSerializer):
    class Meta:
        model = Course

class CourseGroupSerializer(serializer.ModelSerializer):
    class Meta:
        model = CourseGroup
