from django.conf import settings
from main.models import TeamAccess
import ru
import json

class TeamAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        team_access_granted = False

        team = request.session['team'] if 'team' in request.session else {'access': False}

        if 'token' in team:
            session_team_token = team['token']
            try:
                team_access = TeamAccess.objects.get(token=session_team_token)
                if settings.DEBUG: print(f'Team {team_access.team.name} access is granted.')
                team['name'] = team_access.team.name
                team['id'] = team_access.team.id
                team['access'] = True
                team_access_granted = True
            except:
                pass
        if not team_access_granted:
            team = {'access': False}
        request.session['team'] = team

        # Required statement.  Do not remove!!!
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response