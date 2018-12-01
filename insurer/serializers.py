from rest_framework import serializers

from .models import Risk, Field, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'display')


class FieldSerializer(serializers.ModelSerializer):
    option_set = OptionSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Field
        fields = ('id', 'field', 'type', 'validation', 'message', 'option_set')


class RiskSerializer(serializers.ModelSerializer):
    field_set = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Risk
        fields = ('id', 'name', 'description', 'field_set')

    def create(self, validated_data):
        risk = Risk.objects.create(**validated_data)
        fields = self.initial_data.get('field_set')
        for field in fields:
            options = []
            try:
                options = field.pop('option_set')
            except KeyError:
                pass

            field = Field.objects.create(risk=risk, **field)
            for option in options:
                Option.objects.create(field=field, **option)
        return risk
