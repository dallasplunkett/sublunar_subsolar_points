# Real Time Ground Track of Sun and Moon
A project to create an api around a real time ground track of the sun and moon. I'd like to predicte the tides of a given location with this information. Lastly, I want to create some visualization around this information.

### Objectives
1. Practice aquiring and creating data via web scrapping.
2. Practice creating, deploying, and linking a database with a data ingestion system.
3. Learn to create an api/server around a database and deploy it with a cloud based service.
4. Explore predictive modeling methods and techniques.
5. Learn geospatial visualization techniques.

### Resources Used
* [DMS of Sun and Moon Location](https://www.timeanddate.com/worldclock/sunearth.html)
* [Visualization Idea](https://skymarvels.com/infopages/vids/Earth%20-%20Sub-lunar%20Point%20001.htm)
* [DMS vs DD](https://gisgeography.com/decimal-degrees-dd-minutes-seconds-dms/)
* [DMS Resolution Reference](https://www.usgs.gov/faqs/how-much-distance-does-degree-minute-and-second-cover-your-maps)

### Temp Notes
* DMS to DD formula: `decimal degrees = degrees + (minutes / 60) + (seconds / 3600)` The approximate resolution without the seconds is about `max_error = 1.847088 km`
* Tentative JSON api return structure.
```
{
    "moon":
        [
 	    {
	 	"id":        Int()
		"date":      Date("yyyy-mm-dd"),
		"time":      Time("hhmm"),
		"latitude":  Float(Decimal Degree),
		"longitude": Float(Decimal Degree),
		"distance":  Float(Kilometers)
	    },
	],
    "sun": ...
}
```
* Tentative SQL DB structure.

| id | date (yyyy-mm-dd) | time (24 hour) | body | latitude (DD) | longitude (DD) | distance (km) |
|---|---|---|---|---|---|---|
| 123 | 2023-01-10 | 1520 | moon | -72.0234 | 25.3267 | 384,400 |
| 124 | 2023-01-10 | 1520 | sun | 34.3764 | 54.6107 | 150,000,000 |
