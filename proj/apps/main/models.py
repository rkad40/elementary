from datetime import datetime

from colorfield.fields import ColorField
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.db import models
from django.db.models import Q
from django.template import Context, Template
from django.template.loader import render_to_string
from django.utils import timezone

from rex import Rex

DEBUG = False

def localize_now():
  val = datetime.now()
  current_tz = timezone.get_current_timezone()
  return current_tz.localize(val)

r"""
 _____
|_   _|__  __ _ _ __ ___
  | |/ _ \/ _` | '_ ` _ \
  | |  __/ (_| | | | | | |
  |_|\___|\__,_|_| |_| |_|

"""

class Team(models.Model):
  name = models.CharField('Name', max_length=50, unique=True, null=False, blank=False)
  color = ColorField(default='#FF0000')
  player1 = models.CharField('Player 1', max_length=100, unique=False, null=True, blank=True)
  player2 = models.CharField('Player 2', max_length=100, unique=False, null=True, blank=True)
  player3 = models.CharField('Player 3', max_length=100, unique=False, null=True, blank=True)
  player4 = models.CharField('Player 4', max_length=100, unique=False, null=True, blank=True)
  player5 = models.CharField('Player 5', max_length=100, unique=False, null=True, blank=True)
  player6 = models.CharField('Player 6', max_length=100, unique=False, null=True, blank=True)
  password = models.CharField('Password', max_length=100, unique=False, null=True, blank=True)
  start_time = models.DateTimeField('Start Time', null=True, blank=True)
  finish_time = models.DateTimeField('Finish Time', null=True, blank=True)
  completed = models.BooleanField('Is Completed?', default=False, null=False, blank=False)
  data = models.CharField('Data', max_length=10_000, unique=False, null=False, default="", blank=True)
  active = models.BooleanField('Active', default=True, null=False, blank=False)
  class Meta:
    verbose_name = 'Team'
    verbose_name_plural = 'All Teams'
  def __str__(self): 
    return self.name

r"""
 _____                       _
|_   _|__  __ _ _ __ ___    / \   ___ ___ ___  ___ ___
  | |/ _ \/ _` | '_ ` _ \  / _ \ / __/ __/ _ \/ __/ __|
  | |  __/ (_| | | | | | |/ ___ \ (_| (_|  __/\__ \__ \
  |_|\___|\__,_|_| |_| |_/_/   \_\___\___\___||___/___/

"""

class TeamAccess(models.Model):
  token = models.CharField('Token', max_length=100, unique=True, null=False, blank=False)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
  class Meta:
    verbose_name = 'Team Access Token'
    verbose_name_plural = 'Team Access Tokens'

r"""
  ____           _
 / ___|__ _  ___| |__   ___
| |   / _` |/ __| '_ \ / _ \
| |__| (_| | (__| | | |  __/
 \____\__,_|\___|_| |_|\___|

"""

class Cache(models.Model):
  game = models.CharField('game', max_length=50_000, unique=False, null=False, blank=True, default="")
  active = models.BooleanField('Active', default=True, null=False, blank=False)
  class Meta:
    verbose_name = 'Cache'
    verbose_name_plural = 'Cache'

