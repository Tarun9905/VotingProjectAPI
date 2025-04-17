from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from .models import VoterEmail, CastVote
from .serializers import VoterEmailSerializer, CastVoteSerializer

@method_decorator(csrf_exempt, name='dispatch')
class VotingView(View):
    def post(self, request):
        data = JSONParser().parse(request)
        email = data.get('email')

        # Check if email already exists
        if VoterEmail.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already voted!'}, status=400)

        # Serialize and save new email
        serializer = VoterEmailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Vote recorded successfully.'}, status=201)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class VotingCast(View):
    def post(self, request):
        data = JSONParser().parse(request)
        email = data.get('email')

        # Prevent duplicate votes
        if CastVote.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already voted!'}, status=400)

        serializer = CastVoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Vote recorded successfully.'}, status=201)
        return JsonResponse(serializer.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class VotingCount(View):
    def get(self, request):
        option_a_votes = CastVote.objects.filter(options="OptionA").count()
        option_b_votes = CastVote.objects.filter(options="OptionB").count()

        data = {
            "OptionA": option_a_votes,
            "OptionB": option_b_votes
        }

        return JsonResponse(data)
