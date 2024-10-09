# backend/scripts/load_data.py
import os
import json
from django.core.management.base import BaseCommand
from app.models import Player, Game, Shot

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **kwargs):
        raw_data_path = 'backend/raw_data'
        for filename in os.listdir(raw_data_path):
            with open(os.path.join(raw_data_path, filename)) as file:
                data = json.load(file)
                player, created = Player.objects.get_or_create(name=data['player_name'], team=data['team'])
                game, created = Game.objects.get_or_create(player=player, date=data['game_date'])
                for shot in data['shots']:
                    Shot.objects.get_or_create(game=game, x_coordinate=shot['x'], y_coordinate=shot['y'])