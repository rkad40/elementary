from django.contrib import messages
from django.core.mail import EmailMessage, message
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
import datetime

from cronos import epoch

import json
import ru

from rex import Rex

from .models import Team, TeamAccess, Cache

INSULTS = [
    'Dear hopeless losers:',
    'Was that a serious attempt to pass this challenge?',
    'Swing and a miss!',
    'Your team is the reason we have warning labels on stuff.',
    "Your answer get's an A+ for originality ... but an F- for correctness.",
    "Wrong! Wrong! Wrong!",
    "It seems your team is one fry short of a Happy Meal.",
    "Your team has a intellect only a mother could love.",
    "Your team's IQ test just came back negative.",
    "Your team would almost certainly come in <i>third</i> in a duel.",
    "Your team might need a checkup from the neck-up...",
    "Apparently, your team locked the keys to victory in the car.", 
]

def load_challenge_data():
    cache = Cache.objects.filter(active=True).first()
    challenge_data = json.loads(cache.game)
    return challenge_data

def load_team_data(team):
    team_data = {}
    if len(team.data) == 0:
        challenge_data = load_challenge_data()
        team_data = {
            'name': team.name,
            'challenge': {
                'active': None,
                'data': {}
            }
        }
        for challenge_key in challenge_data:
            team_data['challenge']['data'][challenge_key] = {
                'has_started': False,
                'is_completed': False,
                'start_time': 0,
                'end_time': 0,
                'total_time': 0,
                'task_index': 0,
            }
        team.data = json.dumps(team_data, indent=2)
        team.save()
    else:
        team_data = json.loads(team.data)
    return team_data

r"""
 _   _
| | | | ___  _ __ ___   ___
| |_| |/ _ \| '_ ` _ \ / _ \
|  _  | (_) | | | | | |  __/
|_| |_|\___/|_| |_| |_|\___|

"""

def Home(request):
    context = dict(
        name=f'home',
    )
    return render(request, template_name='main/base.html', context=context)

r"""
 _____                    _                _
|_   _|__  __ _ _ __ ___ | |    ___   __ _(_)_ __
  | |/ _ \/ _` | '_ ` _ \| |   / _ \ / _` | | '_ \
  | |  __/ (_| | | | | | | |__| (_) | (_| | | | | |
  |_|\___|\__,_|_| |_| |_|_____\___/ \__, |_|_| |_|
                                     |___/
"""

def TeamLogin(request):
    from .forms import TeamLoginForm
    if request.method == 'POST':
        form = TeamLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                team = Team.objects.get(name=data['team'])
                if team.password.upper() == data['password'].upper():
                    from .util import team_login
                    team_login(request, team)
                    load_team_data(team)
                    messages.success(request, f"""Team {team.name} login was successful.""")
                    return redirect('home')
                else:
                    raise Exception('Invalid team name or password.  Please try again.')
            except:
                messages.error(request, 'Invalid team name or password.  Please try again.')
        else:
            messages.error(request, 'Invalid team name or password.  Please try again.')
    else:
        form = TeamLoginForm()
    context = dict(
        title='Team Login', 
        button='Log In',
        icon='check',
        form=form,
    )
    return render(request, template_name='main/form.html', context=context)    


r"""
 _____                    _                            _
|_   _|__  __ _ _ __ ___ | |    ___   __ _  ___  _   _| |_
  | |/ _ \/ _` | '_ ` _ \| |   / _ \ / _` |/ _ \| | | | __|
  | |  __/ (_| | | | | | | |__| (_) | (_| | (_) | |_| | |_
  |_|\___|\__,_|_| |_| |_|_____\___/ \__, |\___/ \__,_|\__|
                                     |___/
"""

def TeamLogout(request):
    if 'team' not in request.session:
        request.session['team'] = {'access': False}
    if 'token' in request.session['team']:
        team_token = request.session['team']['token']
        try:
            team_access = TeamAccess.objects.get(token=team_token)
            team_access.delete()
        except:
            pass
    for key in ['token', 'name', 'id']:
        if key in request.session['team']:
            del request.session['team'][key]
    request.session['team']['access'] = False
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

r"""
  ____ _           _ _
 / ___| |__   __ _| | | ___ _ __   __ _  ___  ___
| |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \/ __|
| |___| | | | (_| | | |  __/ | | | (_| |  __/\__ \
 \____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___||___/
                                  |___/

"""

# stopwatch or clock
# check-square
# square

def Challenges(request):

    rex = Rex()

    # Get `team` and load `team_data`.
    team_data = None
    all_teams_data = []
    teams = Team.objects.filter(active=True).all()
    for team in teams:
        some_team_data = load_team_data(team)
        if team.id == request.session['team']['id']:
            team_data = some_team_data
            all_teams_data.insert(0, some_team_data)
        else:
            all_teams_data.append(some_team_data)

    all_challenges_complete = True
    challenges_complete = 0
    total_challenges = 0
    max_time = 0
    challenge_data = load_challenge_data()
    challenges = []
    for challenge_key in sorted(challenge_data):
        total_challenges += 1
        challenge_data[challenge_key]['team_completed'] = team_data['challenge']['data'][challenge_key]['is_completed']
        summary = challenge_data[challenge_key]['all_teams_summary'] = []
        for some_team_data in all_teams_data:
            total_time_seconds = some_team_data['challenge']['data'][challenge_key]['total_time']
            max_time = max(max_time, total_time_seconds)
            total_time_str = "-"
            if total_time_seconds > 0:
                total_time_str = str(datetime.timedelta(seconds=total_time_seconds))
                total_time_str = rex.s(total_time_str, '^0+:', '', '=')
                total_time_str = rex.s(total_time_str, '^0', '', '=')
            entry = dict(team_name=some_team_data['name'], icon=None, total_time_seconds=total_time_seconds, total_time_str=total_time_str, total_time_percent=0)
            if some_team_data['challenge']['data'][challenge_key]['has_started']:
                if some_team_data['challenge']['data'][challenge_key]['is_completed']:
                    entry['icon'] = 'check-square'
                else:
                    entry['icon'] = 'clock'
            else:
                entry['icon'] = 'square'
            summary.append(entry)
        if all_teams_data[0]['challenge']['data'][challenge_key]['is_completed']:
            challenges_complete += 1
        else:
            all_challenges_complete = False
        challenges.append(challenge_data[challenge_key])

    if max_time > 0:
        for challenge in challenges:
            for entry in challenge['all_teams_summary']:
                entry['total_time_percent'] = int(100 * entry['total_time_seconds'] / max_time)

    if all_challenges_complete:
        messages.success(request, 'Congratulations! Your team has successfully completed all challenges!') 

    # If `team_data['ActiveChallenge']` is defined, then the team is in an active challenge.  If the active challenge is not
    # the selected challenge, redirect to the active challenge.
    if 'challenge' in team_data and 'active' in team_data['challenge'] and team_data['challenge']['active'] is not None:
        return redirect('challenge')

    context = dict(
        all_challenges_complete=all_challenges_complete,
        challenges_complete=challenges_complete,
        total_challenges=total_challenges,
        challenges=challenges,
        team_data=team_data,
        all_teams_data=all_teams_data,
    )
    return render(request, template_name='main/challenges.html', context=context)  

r"""
  ____       _     _
 / ___|_   _(_) __| | ___
| |  _| | | | |/ _` |/ _ \
| |_| | |_| | | (_| |  __/
 \____|\__,_|_|\__,_|\___|

"""
@staff_member_required
def Guide(request):
    challenge_data = load_challenge_data()
    context = dict(
        challenges=challenge_data
    )
    return render(request, template_name='main/guide.html', context=context)  

r"""
 ____       _       _              _
|  _ \ _ __(_)_ __ | |_ ___  _   _| |_ ___
| |_) | '__| | '_ \| __/ _ \| | | | __/ __|
|  __/| |  | | | | | || (_) | |_| | |_\__ \
|_|   |_|  |_|_| |_|\__\___/ \__,_|\__|___/

"""
@staff_member_required
def Printouts(request):
    teams = Team.objects.filter(active=True).all()
    context = dict(
        teams=teams,
    )
    return render(request, template_name='main/printouts.html', context=context)     

r"""
 ____                 _ _
|  _ \ ___  ___ _   _| | |_ ___
| |_) / _ \/ __| | | | | __/ __|
|  _ <  __/\__ \ |_| | | |_\__ \
|_| \_\___||___/\__,_|_|\__|___/

"""

def Results(request):

    rex = Rex()

    # Get `team` and load `team_data`.
    team_data = None
    teams = Team.objects.filter(active=True).all()
    chart = {
        'type': 'bar',
        'data': {
            'labels': [],
            'datasets': [],
        },
        'options': {
            'title': {'text': 'Results', 'display': True},
            'responsive': True,
            'maintainAspectRatio': False,
        },
    }

    colors = ['#ff7970', '#6ab09d', '#83a4e6', '#ed9255', '#83c7c0', '#cd9be8']

    challenges = load_challenge_data()
    for challenge_key in sorted(challenges):
        challenge = challenges[challenge_key]
        chart['data']['labels'].append(challenge['number'])

    total_time_seconds = 0

    team_color = {}
    total_time = {}
    is_completed = {}
    for team in teams:
        team_data = load_team_data(team)
        team_name = team_data['name']
        is_completed[team_name] = True
        # team_color[team_data['name']] = colors.pop(0)
        team_color[team_data['name']] = team.color
        dataset = {'label': team_data['name'], 'data': [], 'backgroundColor': team_color[team_name]}
        for challenge_key in sorted(team_data['challenge']['data']):
            val = team_data['challenge']['data'][challenge_key]['total_time']/60
            val = float(f'{val:0.1f}')
            dataset['data'].append(val)
            if not team_data['challenge']['data'][challenge_key]['is_completed']:
                is_completed[team_name] = False
        chart['data']['datasets'].append(dataset)
        total_time[team_data['name']] = 0

    summary = []
    for challenge_key in sorted(challenges):
        challenge = challenges[challenge_key]
        data = {}
        entry = dict(name=f"""{challenge['number']}. {challenge['title']}""", teams=[])
        for team in teams:
            team_data = load_team_data(team)
            total_time_seconds = team_data['challenge']['data'][challenge_key]['total_time']
            total_time[team_data['name']] += total_time_seconds
            total_time_str = '-'
            if total_time_seconds > 0:
                total_time_str = str(datetime.timedelta(seconds=total_time_seconds))
                total_time_str = rex.s(total_time_str, '^0+:', '', '=')
                total_time_str = rex.s(total_time_str, '^0', '', '=')
            total_time_seconds_normalized = 100000000+total_time_seconds
            if total_time_seconds == 0:
                total_time_seconds_normalized = 200000000
            team_key = f"""{total_time_seconds_normalized}-{team_data['name']}"""
            data[team_key] = dict(time_seconds=total_time_seconds, time_str=total_time_str, name=team_data['name'], back_seconds=0, back_str="-", color=team_color[team_data['name']])
        best = None
        for team_key in sorted(data):
            if best is None:
                if data[team_key]['time_seconds'] > 0:
                    best = data[team_key]['time_seconds']
            else:
                if best is not None and data[team_key]['time_seconds'] > 0:
                    delta = data[team_key]['time_seconds'] - best
                    if delta > 0:
                        delta = str(datetime.timedelta(seconds=delta))
                        delta = rex.s(delta, '^0+:', '', '=')
                        delta = rex.s(delta, '^0', '', '=')
                    data[team_key]['back_str'] = f"""+{delta}"""
            entry['teams'].append(data[team_key])
        summary.append(entry)

    data = {}
    entry = dict(name=f"""Overall Summary""", teams=[])
    for team in teams:
        team_name = team.name
        total_time_seconds = total_time[team_name]
        if not is_completed[team_name]:
            total_time_seconds = 0
        total_time_str = '-'
        if total_time_seconds > 0:
            total_time_str = str(datetime.timedelta(seconds=total_time_seconds))
            total_time_str = rex.s(total_time_str, '^0+:', '', '=')
            total_time_str = rex.s(total_time_str, '^0', '', '=')
        total_time_seconds_normalized = 100000000+total_time_seconds
        if total_time_seconds == 0:
            total_time_seconds_normalized = 200000000
        team_key = f"""{total_time_seconds_normalized}-{team_name}"""
        data[team_key] = dict(time_seconds=total_time_seconds, time_str=total_time_str, name=team_name, back_seconds=0, back_str="-", color=team_color[team_name])
    best = None
    for team_key in sorted(data):
        if best is None:
            if data[team_key]['time_seconds'] > 0:
                best = data[team_key]['time_seconds']
        else:
            if best is not None and data[team_key]['time_seconds'] > 0:
                delta = data[team_key]['time_seconds'] - best
                if delta > 0:
                    delta = str(datetime.timedelta(seconds=delta))
                    delta = rex.s(delta, '^0+:', '', '=')
                    delta = rex.s(delta, '^0', '', '=')
                data[team_key]['back_str'] = f"""+{delta}"""
        entry['teams'].append(data[team_key])
    summary.append(entry)
            
    data = json.dumps(chart, indent=2)

    context = dict(
        data=data,
        summary=summary,
    )
    return render(request, template_name='main/results.html', context=context)     


r"""
  ____ _           _ _                            _
 / ___| |__   __ _| | | ___ _ __   __ _  ___     / \   ___ ___ ___  ___ ___
| |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \   / _ \ / __/ __/ _ \/ __/ __|
| |___| | | | (_| | | |  __/ | | | (_| |  __/  / ___ \ (_| (_|  __/\__ \__ \
 \____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___| /_/   \_\___\___\___||___/___/
                                  |___/
"""

def ChallengeAccess(request, key, code):
    
    challenge_key = key
    user_access_code = code

    # Get `team` and load `team_data`.
    team = Team.objects.get(id=request.session['team']['id'])
    team_data = load_team_data(team)
    challenge_data = load_challenge_data()

    # Make sure `user_access_code` matches `challenge[`.
    if user_access_code != challenge_data[challenge_key]['access'] and user_access_code != 7273:
        request.session['error'] = f"""Oops, something went wrong.  Invalid access code used while attempting to access challenge {challenge_data[challenge_key]['number']}."""
        return redirect('error')
    
    team_data['challenge']['active'] = challenge_key
    team_data['challenge']['data'][challenge_key]['has_started'] = True
    team_data['challenge']['data'][challenge_key]['start_time'] = epoch(int)
    team_data['challenge']['data'][challenge_key]['task_index'] = 1

    team.data = json.dumps(team_data, indent=2)
    team.save()

    return redirect('challenge')

r"""
  ____ _           _ _
 / ___| |__   __ _| | | ___ _ __   __ _  ___
| |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \
| |___| | | | (_| | | |  __/ | | | (_| |  __/
 \____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|
                                  |___/
"""

def Challenge(request):
    from .forms import ChallengeForm

    team = Team.objects.get(id=request.session['team']['id'])
    team_data = load_team_data(team)
    challenge_data = load_challenge_data()
    if team_data['challenge']['active'] is None:
        return redirect('challenges')
    challenge_key = team_data['challenge']['active']
    active_challenge = challenge_data[challenge_key]
    team_challenge_data = team_data['challenge']['data'][challenge_key]
    task_index = team_challenge_data['task_index']
    task_data = active_challenge['tasks'][task_index]
    num_tasks = len(active_challenge['tasks'])
    num_fields = len(task_data['fields'])

    i = 0
    for task in active_challenge['tasks']:
        task['index'] = i
        task['number'] = i + 1
        task['is_current'] = False
        task['is_completed'] = False
        if i == task_index: 
            task['is_current'] = True
        if i < task_index: 
            task['is_completed'] = True
        i += 1
    
    rex = Rex()

    form = None
    errors = 0
    scroll_pos = 0
    penalty = 0
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        for i in range(0, num_fields):
            form.fields[f'field{i}'].help_text = 'fail'
        if form.is_valid():
            # Get `scroll_pos` saved in hidden field.
            # scroll_pos = form.cleaned_data['scroll_pos']
            try:
                scroll_pos = request.POST.get('scroll_pos', 0)
                if scroll_pos == 0: request.POST.get('scroll_pos', 0)
                if scroll_pos == 0: request.POST.get('scroll_pos', 0)
            except:
                scroll_pos = 0
            # Cycle through fields and check correct / incorrect answers.
            for i in range(0, num_fields):
                # Check answers
                answer = str(form.cleaned_data[f'field{i}']).strip().lower()
                answer = rex.s(answer, r'\W', '', 'g=')
                expect = str(task_data['fields'][i]['expect']).strip().lower()
                expect = rex.s(expect, r'\|', '___OR___', 'g=')
                expect = rex.s(expect, r'\W', '', 'g=')
                expect = rex.s(expect, '___OR___', '|', 'g=')
                if rex.m(answer, f'^({expect})$'):
                    # Answer is correct for this field ..
                    form.fields[f'field{i}'].help_text = 'pass'
                else:
                    # Answer is incorrect for this field.
                    errors += 1
            if errors == 0:
                team_challenge_data['task_index'] += 1
                if team_challenge_data['task_index'] >= num_tasks:
                    messages.success(request, f"""Please select a new challenge.""")
                    team_data['challenge']['active'] = None
                    team_challenge_data['is_completed'] = True
                    team_challenge_data['end_time'] = epoch(int)
                    team_challenge_data['total_time'] = team_challenge_data['end_time'] - team_challenge_data['start_time']
                    team_challenge_data['task_index'] = 0
                    team.data = json.dumps(team_data, indent=2)
                    team.save()
                    return redirect('challenges')
                else:
                    if num_fields > 0:
                        messages.success(request, f"""That is correct.  Good job!""")
                    team.data = json.dumps(team_data, indent=2)
                    team.save()
                    return redirect('challenge')
            else:
                if 'penalty' in task_data and task_data['penalty'] and task_data['penalty'] > 0:
                    penalty = task_data['penalty']
                    now = epoch(int)
                    team_data['penalty'] = dict(seconds=penalty, starts=now, ends=now+penalty)
                    team.data = json.dumps(team_data, indent=2)
                    team.save()
    else:
        # messages.success(request, f"""Challenge access granted.""")
        form = ChallengeForm()

    if len(task_data['fields']) > 0:
        for i in range(0, num_fields):
            form.fields[f'field{i}'].label = task_data['fields'][i]['label']

    print(team_challenge_data)

    context = dict(
        form=form,
        team=team,
        team_data=team_data,
        team_challenge_data=team_challenge_data,
        active_challenge=active_challenge,
        task_data=task_data,
        num_tasks=num_tasks,
        num_fields=num_fields,
        scroll=scroll_pos,
        errors=errors,
        insult=ru.rand_item(INSULTS) if errors > 0 else '',
    )
    return render(request, template_name='main/challenge.html', context=context)     

r"""
     _                                _
    | | ___  ___  _ __   __ _ _ __ __| |_   _
 _  | |/ _ \/ _ \| '_ \ / _` | '__/ _` | | | |
| |_| |  __/ (_) | |_) | (_| | | | (_| | |_| |
 \___/ \___|\___/| .__/ \__,_|_|  \__,_|\__, |
                 |_|                    |___/
"""

def Jeopardy(request):
    context = dict(debug=False)
    return render(request, template_name='main/jeopardy.html', context=context)     

r"""
 _____
| ____|_ __ _ __ ___  _ __
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |
|_____|_|  |_|  \___/|_|

"""

def Error(request):
    try:
        msg = request.session['error']
        del request.session['error']
    except:
        msg = f"<p>Sorry, it seams this request has resulted in an unforeseen error.</p><p>Please go back and try your requested action again.  If the problem persists, please contact the tournament organizer, <strong>{settings.ADMIN_NAME}</strong> at {settings.ADMIN_PHONE}.</p>"
    context = dict(
        title='Error',
        message=msg
    )
    return render(request, template_name='main/error.html', context=context)

    
