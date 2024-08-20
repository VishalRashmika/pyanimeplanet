import stats

def main():
    stats.setusername("AkiraArashikage")
    anilist = stats.get_animestats()
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
    # stats.get_full_info()

main()

'''
animeplanet.username("AkiraArashikage")
animeplanet.getstats()

'''