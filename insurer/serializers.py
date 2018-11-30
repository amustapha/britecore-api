from rest_framework import serializers

from .models import Risk, Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('id', 'field', 'key')


class RiskSerializer(serializers.ModelSerializer):
    field_set = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Risk
        fields = ('id', 'name', 'description', 'field_set')

    def create(self, validated_data):
        risk = Risk.objects.create(**validated_data)
        fields = self.initial_data.get('field_set')
        for field in fields:
            Field.objects.create(risk=risk, **field)
        return risk
