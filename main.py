import pyanimeplanet as pp

def main():
    pp.setusername("awdawdd")
    anilist = pp.anime_stats()
    print(anilist)

    # watchlist = stats.get_watched_list()
    # print(watchlist["Anime"][1])
    # print(watchlist["Anime"][1]["title"])
    # print(watchlist["Anime"][1]["rating"])
    # print(watchlist["Anime"][1]["episodes"])

    # stats.get_watching_list()
    # stats.get_want_to_watch_list()
    # stats.get_wont_watch_list()
    # stats.get_dropped_list()
    #stats.get_stalled_list()
    # print(pp.full_info())

main()

'''
animeplanet.username("AkiraArashikage")
animeplanet.getstats()

'''