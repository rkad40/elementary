from django.contrib import admin
from django.http import HttpResponse
from .models import Team, TeamAccess, Cache
import csv, json
import datetime
import ru

from .util import create_random_password

from django_summernote.utils import get_attachment_model

admin.site.unregister(get_attachment_model())

admin.site.site_header = 'Back to School Challenge'
admin.site.index_title = 'Admin Dashboard'
admin.site.site_title = 'Site Administration'

def get_queryset_data(meta, queryset):
    opts = meta
    data = []
    fields = [field for field in opts.get_fields() \
        if not field.many_to_many and not field.one_to_many]
    for obj in queryset:
        row = {}
        for field in fields:
            value = getattr(obj, field.name)
            if value is None or isinstance(value, (int, bool, str, float)):
                pass
            elif field.many_to_one:
                value = dict(model=ru.stype(value), id=value.id, value=str(value))
            elif isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            else:
                raise Exception(f'Invalid export type "{type(value)}".')
            row[field.name] = value
        data.append(row)
    return data

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}Data.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response) #, delimiter='\t')
    fields = [field for field in opts.get_fields() \
        if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

def export_to_json(modeladmin, request, queryset):
    import json
    data = get_queryset_data(modeladmin.model._meta, queryset)
    content_disposition = f'attachment; filename={modeladmin.model._meta.object_name}.json'
    txt = json.dumps(data, indent=2)
    response = HttpResponse(txt, content_type="text/json")
    response['Content-Disposition'] = content_disposition
    return response
export_to_json.short_description = 'Export to JSON'

def export_to_yaml(modeladmin, request, queryset):
    import yaml
    data = get_queryset_data(modeladmin.model._meta, queryset)
    content_disposition = f'attachment; filename={modeladmin.model._meta.object_name}.yml'
    txt = yaml.safe_dump(data)
    response = HttpResponse(txt, content_type="application/yaml")
    response['Content-Disposition'] = content_disposition
    return response
export_to_yaml.short_description = 'Export to YAML'

def add_random_passwords(modeladmin, request, queryset):
    for team in queryset:
        password = create_random_password()
        team.password = password
        team.save()
add_random_passwords.short_description = 'Add random passwords'

def add_debug_passwords(modeladmin, request, queryset):
    for team in queryset:
        password = '1234'
        team.password = password
        team.save()
add_debug_passwords.short_description = 'Add debug passwords'

def clear_team_data(modelamdin, request, queryset):
    from .views import load_team_data, load_challenge_data
    challenges = load_challenge_data()
    for team in queryset:
        team.data = ""
        team_data = load_team_data(team)
        team.data = json.dumps(team_data, indent=2)
        team.save()
clear_team_data.short_description = 'Clear team data'

def random_team_data(modelamdin, request, queryset):
    from .views import load_team_data, load_challenge_data
    challenges = load_challenge_data()
    for team in queryset:
        team.data = ""
        team_data = load_team_data(team)
        skip = [ru.rint(2, len(challenges)), len(challenges)]
        print(skip)
        for challenge_key in sorted(challenges):
            challenge = challenges[challenge_key]
            if challenge['number'] in skip:
                continue
            print(f"Adding data for challenge {challenge['number']} ...")
            team_data['challenge']['data'][challenge_key]['has_started'] = True
            team_data['challenge']['data'][challenge_key]['is_completed'] = True
            team_data['challenge']['data'][challenge_key]['total_time'] = ru.rint(6*60, 12*60) 
        team.data = json.dumps(team_data, indent=2)
        team.save()
random_team_data.short_description = 'Create random team data'

def complete_random_team_data(modelamdin, request, queryset):
    from .views import load_team_data, load_challenge_data
    challenges = load_challenge_data()
    for team in queryset:
        team.data = ""
        team_data = load_team_data(team)
        for challenge_key in sorted(challenges):
            challenge = challenges[challenge_key]
            print(f"Adding data for challenge {challenge['number']} ...")
            team_data['challenge']['data'][challenge_key]['has_started'] = True
            team_data['challenge']['data'][challenge_key]['is_completed'] = True
            team_data['challenge']['data'][challenge_key]['total_time'] = ru.rint(6*60, 12*60) 
        team.data = json.dumps(team_data, indent=2)
        team.save()
complete_random_team_data.short_description = 'Create complete random team data'

from .forms import TeamForm
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    list_display = ['name', 'password', 'data', 'active']
    ordering = ['name']
    actions = [add_random_passwords, add_debug_passwords, export_to_csv, export_to_json, export_to_yaml, clear_team_data, random_team_data, complete_random_team_data]
    list_editable = ['active']

@admin.register(TeamAccess)
class TeamAccessAdmin(admin.ModelAdmin):
    list_display = ['token', 'team']
    ordering = ['team']
    actions = [export_to_csv, export_to_json, export_to_yaml]

from .forms import CacheForm
@admin.register(Cache)
class CacheAdmin(admin.ModelAdmin):
    form = CacheForm
    list_display = ['id', 'game', 'active']
    ordering = ['id']


