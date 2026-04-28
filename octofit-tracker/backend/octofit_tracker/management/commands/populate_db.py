from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Sample data for superheroes and teams
USERS = [
    {"username": "superman", "email": "superman@dc.com", "team": "dc"},
    {"username": "batman", "email": "batman@dc.com", "team": "dc"},
    {"username": "wonderwoman", "email": "wonderwoman@dc.com", "team": "dc"},
    {"username": "ironman", "email": "ironman@marvel.com", "team": "marvel"},
    {"username": "spiderman", "email": "spiderman@marvel.com", "team": "marvel"},
    {"username": "captainamerica", "email": "captainamerica@marvel.com", "team": "marvel"},
]

TEAMS = [
    {"name": "marvel"},
    {"name": "dc"},
]

ACTIVITIES = [
    {"user": "superman", "activity": "flight", "duration": 60},
    {"user": "batman", "activity": "martial arts", "duration": 45},
    {"user": "ironman", "activity": "engineering", "duration": 30},
]

LEADERBOARD = [
    {"user": "superman", "score": 100},
    {"user": "ironman", "score": 90},
    {"user": "batman", "score": 80},
]

WORKOUTS = [
    {"name": "strength", "description": "Strength training"},
    {"name": "agility", "description": "Agility drills"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        db.users.create_index("email", unique=True)
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
