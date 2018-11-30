from rest_framework import serializers

from .models import Risk, Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class RiskSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Risk
        fields = ('name', 'description', 'fields')

    def create(self, validated_data):
        risk = Risk.objects.create(**validated_data)
        fields = self.initial_data.get('fields')
        for field in fields:
            Field.objects.create(risk=risk, **field)
        return risk
