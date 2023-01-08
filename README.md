# sublunar_subsolar_points
A project to create an api around the live ground tracks of the sun and moon. Later, this data will be used to estimate the tides given a lat long.

### Resources Used
* [DMS of Sun and Moon Location](https://www.timeanddate.com/worldclock/sunearth.html)
* [Visualization Idea](https://skymarvels.com/infopages/vids/Earth%20-%20Sub-lunar%20Point%20001.htm)
* [DMS vs DD](https://gisgeography.com/decimal-degrees-dd-minutes-seconds-dms/)
* [DMS Resolution Reference](https://www.usgs.gov/faqs/how-much-distance-does-degree-minute-and-second-cover-your-maps)

DMS to DD formula `decimal degrees = degrees + (minutes / 60) + (seconds / 3600)`

The approximate resolution error without seconds from DMS source is `max_error_radius = 1.847088 km`

Tentative JSON api return structure.
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

Tentative SQL DB structure.
| id | date (yyyy-mm-dd) | time (24 hour) | body | latitude (DD) | longitude (DD) | distance (km) |
|---|---|---|---|---|---|---|
| 123 | 2023-01-10 | 1520 | moon | -72.0234 | 25.3267 | 384,400 |
| 124 | 2023-01-10 | 1520 | sun | 34.3764 | 54.6107 | 150,000,000 |
