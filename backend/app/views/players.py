# -*- coding: utf-8 -*-
import logging
from functools import partial
import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.dbmodels import models
from django.http import HttpResponse
from django.http import JsonResponse
from app.models import Player, Game, Shot
LOGGER = logging.getLogger('django')




class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player data"""
        print(playerID)
        # TODO: Complete API response, replace placeholder below with actual implementation that sources data from database
        print(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.dirname(os.path.abspath(__file__)) + '/sample_response/sample_response.json') as sample_response:
            data = json.load(sample_response)
        return Response(data)
    
    def home(request):
        return HttpResponse("Welcome to the Home Page")
    
    def player_summary(request, player_id):
        player = Player.objects.get(id=player_id)
        games = Game.objects.filter(player=player)
        summary = {
            "player_name": player.name,
            "team": player.team,
            "games": []
        }
        for game in games:
            shots = Shot.objects.filter(game=game)
            game_summary = {
                "date": game.date,
                "shots": [{"x": shot.x_coordinate, "y": shot.y_coordinate} for shot in shots]
            }
            summary["games"].append(game_summary)
        return JsonResponse(summary)
