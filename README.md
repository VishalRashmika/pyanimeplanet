# pyanimeplanet
A package that allows to extract information from anime planet website without login. This module uses the selenium web driver to scrap details from the web.

# Usage

1. setup the username first
```python
import pyanimeplanet as anime

anime.set_username("AkiraArashikage")
```
2. request information

available functions:
- anime_stats() => returns the overall information listed in profile
- watched_list => returns the watched anime list
- watching_list => returns the watching anime list
- want_to_watch_list => returns the want to watch anime list
- stalled_list => returns the stalled anime list
- dropped_list => returns the dropped anime list
- wont_watch_list => returns the won't watch anime list
- full_info => returns the all information  (stats, watched, watching, want to watch, stalled, dropped, won't watch and dropped)

### example
1. program
```python 
import pyanimeplanet as anime

anime.set_username("AkiraArashikage")
print(anime.watching_list())
```

2. output
```json
{'Anime': [{'title': 'A Journey Through Another World: Raising Kids While Adventuring', 'rating': 3.0, 'episodes': 8, 'watched episodes': 8}, {'title': 'Alya Sometimes Hides Her Feelings in Russian', 'rating': 3.0, 'episodes': 7, 'watched episodes': 7}, {'title': 'Bartender Glass of God', 'rating': 3.0, 'episodes': 12, 'watched episodes': 1}, {'title': 'Bleach', 'rating': 4.0, 'episodes': 366, 'watched episodes': 3}, {'title': 'Days with My Stepsister', 'rating': 3.0, 'episodes': 7, 'watched episodes': 3}]}
```