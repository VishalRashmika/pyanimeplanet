import requests
from bs4 import BeautifulSoup


def get_anime(username):

    url = f"https://www.anime-planet.com/users/{username}/anime/watched"

    r = requests.get(
        url,
        headers = {
            'User-Agent': 'Popular browser\'s user-agent',
        }
    )
    source = BeautifulSoup(r.text, 'html.parser')
    animelist_data = source.find('div', class_="pagination aligncenter").find('li')
    print(animelist_data)

get_anime("AkiraArashikage")