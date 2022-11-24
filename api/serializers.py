from rest_framework import serializers


class SoftwareSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    Discipline = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    OpSys = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    Name = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    Practicum_Num = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
