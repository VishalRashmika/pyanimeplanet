import requests
from bs4 import BeautifulSoup

username = ""

def setusername(name):
    username = name


def count_extract(source):
    return str(str(source).split('>')[1]).split('<')[0]

def calculate_time_minutes(min,hours,days,weeks,months,years):
    hours_min = int(hours) * 60
    days_min = int(days) * 24 * 60
    weeks_min = int(weeks) * 7 * 24 * 60
    months_min = int(months) * 30 * 7 * 24 * 60
    years_min = int(years) * 12 * 30 * 7 * 24 * 60    
    total_minutes = int(min) + hours_min + days_min + weeks_min + months_min + years_min
    
    return total_minutes

def calculate_time_hours(min,hours,days,weeks,months,years):
    in_minutes = calculate_time_minutes(min,hours,days,weeks,months,years)
    return format(float(in_minutes / 60),".2f")

def get_total_anime_rating(source):
    total_anime_rating = int(str(str(source.find('p', class_= "plr-total pure-1-4")).split('>')[1]).split('\n')[1])
    return total_anime_rating

def get_animestats():
    profile_link = f"https://www.anime-planet.com/users/{username}"

    r = requests.get(
        profile_link,
        headers = {
            'User-Agent': 'Popular browser\'s user-agent',
        }
    )
    source = BeautifulSoup(r.text, 'html.parser')
    animelist_data = source.find('div', class_="plr-list pure-1 md-1-2")

    # watched
    watched = (animelist_data.find('li',class_="status1")).find('span',class_="slCount")
    watched_count = count_extract(watched)

    # watching
    watching = (animelist_data.find('li',class_="status2")).find('span',class_="slCount")
    watching_count = count_extract(watching)

    want_to_watch = (animelist_data.find('li',class_="status4")).find('span',class_="slCount")
    want_to_watch_count = count_extract(want_to_watch)

    stalled = (animelist_data.find('li',class_="status5")).find('span',class_="slCount")
    stalled_count = count_extract(stalled)

    dropped = (animelist_data.find('li',class_="status3")).find('span',class_="slCount")
    dropped_count = count_extract(dropped)

    wont_watch = (animelist_data.find('li',class_="status6")).find('span',class_="slCount")
    wont_watch_count = count_extract(wont_watch)

    total_episodes = (animelist_data.find('i', id="totalEps"))
    total_episodes_count = count_extract(total_episodes).replace(',','')

    life_on_anime_data = str(source.find('ul', class_= "loa-labels pure-g")).split('>')
    minutes = str(life_on_anime_data[2]).split('\n')[0]
    hours = str(life_on_anime_data[6]).split('\n')[0]
    days = str(life_on_anime_data[10]).split('\n')[0]
    weeks = str(life_on_anime_data[14]).split('\n')[0]
    months = str(life_on_anime_data[18]).split('\n')[0]
    years = str(life_on_anime_data[22]).split('\n')[0]
    life_on_anime_min = calculate_time_minutes(minutes,hours,days,weeks,months,years)
    life_on_anime_hours = calculate_time_hours(minutes,hours,days,weeks,months,years)
    total_anime_rating = get_total_anime_rating(source)

    animestats = {
        "watched": int(watched_count), 
        "watching" : int(watched_count), 
        "want to watch" : int(want_to_watch_count), 
        "stalled" : int(stalled_count), 
        "dropped" : int(dropped_count), 
        "won't watch" : int(wont_watch_count),
        "total episodes" : int(total_episodes_count),
        "total watchtime (in minutes)" : life_on_anime_min,
        "total watchtime (in hours)" : float(life_on_anime_hours),
        "total anime ratings" : total_anime_rating,
    }

    return animestats


def get_watched_list():
    pass