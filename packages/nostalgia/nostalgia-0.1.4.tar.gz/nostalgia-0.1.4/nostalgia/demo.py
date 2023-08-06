from nostalgia.sources.chrome_history import WebHistory, page_visit
from nostalgia.sources.fitbit.heartrate import Heartrate
from nostalgia.sources.google import GooglePlaces

web_history = WebHistory.load()
heartrate = Heartrate.load()
places = GooglePlaces.load()

web_history.last_week.during_office_hours.when_at(places.containing("amsterdam")).heartrate_above(0)

page_visit.at(places.containing("amsterdam zuid"))  # .containing("dark")

page_visit.at_time(
    "2019-09-27 18:50:36.747000", "2019-09-27 19:00:36.747000", minutes=3
).containing("dark")
