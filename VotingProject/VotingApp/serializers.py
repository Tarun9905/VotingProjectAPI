from rest_framework import serializers
from .models import VoterEmail, CastVote

class VoterEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoterEmail
        fields = ['email']

class CastVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastVote
        fields = "__all__"
