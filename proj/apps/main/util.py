import json, csv
import ru
from rex import Rex
from django.apps import apps
from .models import Team
from django.db.models import Q
from django.contrib import messages
from cronos import epoch
import unchained

XMAS_WORDS = ['elf', 'snow', 'santa', 'deer', 'xmas', 'holly', 'sled', 'gift', 'family', 'winter', 
'jingle', 'bells', 'silver', 'gold', 'white', 'card', 'tree', 'star', 'candy', 'season', 'great', 
'good', 'peace', 'bow', 'box', 'candle', 'cheer', 'carol', 'believe', 'angel', 'eggnog', 'faith', 
'frosty', 'festive', 'grinch', 'jolly', 'joy', 'noel', 'wrap', 'wish']

r"""
                     _                             _
  ___ _ __ ___  __ _| |_ ___   _ __ __ _ _ __   __| | ___  _ __ ___
 / __| '__/ _ \/ _` | __/ _ \ | '__/ _` | '_ \ / _` |/ _ \| '_ ` _ \
| (__| | |  __/ (_| | ||  __/ | | | (_| | | | | (_| | (_) | | | | | |
 \___|_|  \___|\__,_|\__\___| |_|  \__,_|_| |_|\__,_|\___/|_| |_| |_|

                                           _
 _ __   __ _ ___ _____      _____  _ __ __| |
| '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |
| |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |
| .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
|_|

"""

def create_random_password():
    password = ru.ritem(XMAS_WORDS) + str(ru.rint(100, 999))
    return password

r"""
                     _                             _
  ___ _ __ ___  __ _| |_ ___   _ __ __ _ _ __   __| | ___  _ __ ___
 / __| '__/ _ \/ _` | __/ _ \ | '__/ _` | '_ \ / _` |/ _ \| '_ ` _ \
| (__| | |  __/ (_| | ||  __/ | | | (_| | | | | (_| | (_) | | | | | |
 \___|_|  \___|\__,_|\__\___| |_|  \__,_|_| |_|\__,_|\___/|_| |_| |_|

                                           _
 _ __   __ _ ___ _____      _____  _ __ __| |___
| '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` / __|
| |_) | (_| \__ \__ \\ V  V / (_) | | | (_| \__ \
| .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|___/
|_|
"""

def create_random_passwords(request):
    teams = Team.objects.filter(active=True).filter(Q(password='') | Q(password__isnull=True)).all()
    cnt = len(teams)
    if cnt > 0:
        for team in teams:
            password = create_random_password()
            team.password = password
            team.save()
        messages.success(request, f'Random passwords added for {cnt} {ru.pluralize("team", cnt)}.')
    else:
        messages.success(request, f'All valid teams already have passwords defined. No passwords added.')

r"""
     _ _      _        _
  __| (_) ___| |_ __ _| |_ ___
 / _` | |/ __| __/ _` | __/ _ \
| (_| | | (__| || (_| | ||  __/
 \__,_|_|\___|\__\__,_|\__\___|

"""

def dictate(data):
    d = {}
    for key in data:
        if key.startswith('_'): continue
        val = data[key]
        stype = ru.stype(data[key])
        if stype not in ['int', 'str', 'bool', 'float']:
            val = str(val)
        d[key] = val
    return d

r"""
 _                         _             _
| |_ ___  __ _ _ __ ___   | | ___   __ _(_)_ __
| __/ _ \/ _` | '_ ` _ \  | |/ _ \ / _` | | '_ \
| ||  __/ (_| | | | | | | | | (_) | (_| | | | | |
 \__\___|\__,_|_| |_| |_| |_|\___/ \__, |_|_| |_|
                                   |___/
"""

def team_login(request, team):
    from .models import TeamAccess
    token = f'{team.name}.{team.id:08d}.{epoch()}.{ru.rint(10000, 99999)}'
    TeamAccess.objects.create(token=token, team=team)
    if 'team' not in request.session:
        request.session['team'] = {}
    request.session['team']['token'] = token
    # from .util import calculate_team_handicap_per_hole
    # calculate_team_handicap_per_hole(request, team)



