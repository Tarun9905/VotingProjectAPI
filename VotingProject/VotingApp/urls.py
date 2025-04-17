from django.urls import path
from .views import VotingView, VotingCast, VotingCount

urlpatterns = [
    path('emailverify/', VotingView.as_view()),
    path('castvote/', VotingCast.as_view()),
    path('count/',VotingCount.as_view())
]