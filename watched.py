import requests
from bs4 import BeautifulSoup


def get_animestats(username):
    profile_link = f"https://www.anime-planet.com/users/{username}"

    r = requests.get(
        profile_link,
        headers = {
            'User-Agent': 'Popular browser\'s user-agent',
        }
    )
    source = BeautifulSoup(r.text, 'html.parser')
    animelist_data = source.find('div', class_="plr-list pure-1 md-1-2")
