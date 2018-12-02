from sqlite3 import IntegrityError

from django.db import transaction
from rest_framework import serializers

from .models import Risk, Field, Option, SubmissionSet, SubmissionValue
from time import time

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'display')


class FieldSerializer(serializers.ModelSerializer):
    option_set = OptionSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Field
        fields = ('id', 'field', 'type', 'validation', 'message', 'is_required' 'option_set')


class RiskSerializer(serializers.ModelSerializer):
    field_set = FieldSerializer(many=True)

    class Meta:
        model = Risk
        fields = ('id', 'name', 'description', 'field_set')

    def create(self, validated_data):
        fields = validated_data.pop('field_set')
        try:
            with transaction.atomic():
                risk = Risk.objects.create(**validated_data)
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
        except IntegrityError:
            pass


class ValueSerializer(serializers.ModelSerializer):
    value = serializers.JSONField()

    class Meta:
        model = SubmissionValue
        fields = ('field', 'value')


class SubmissionSerializer(serializers.ModelSerializer):
    submissionvalue_set = ValueSerializer(many=True)

    class Meta:
        model = SubmissionSet
        fields = ('risk', 'submissionvalue_set')

    def create(self, validated_data):
        values = validated_data.pop('submissionvalue_set')
        try:
            with transaction.atomic():
                submission = SubmissionSet.objects.create(**validated_data)
                for value in values:
                    SubmissionValue.objects.create(set=submission, **value)
            return submission
        except IntegrityError:
            pass
