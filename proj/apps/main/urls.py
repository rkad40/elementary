from django.urls import path

from . import views as view

urlpatterns = [
  path('', view.Home, name='home'),
  path('home', view.Home, name='home'),
  path('challenges', view.Challenges, name='challenges'),
  path('challenge', view.Challenge, name='challenge'),
  path('challenge/access/<str:key>/<int:code>', view.ChallengeAccess, name='challenge-access'),
  path('jeopardy', view.Jeopardy, name='jeopardy'),
  path('printouts', view.Printouts, name='printouts'),
  path('guide', view.Guide, name='guide'),
  path('results', view.Results, name='results'),
  path('login', view.TeamLogin, name='team-login'),
  path('logout', view.TeamLogout, name='team-logout'),
  path('error', view.Error, name='error'),
]

