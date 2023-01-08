# sublunar_subsolar_points
A project to create an api around the live ground tracks of the sun and moon. Later, this data will be used to estimate the tides given a lat long.

### Resources Used
* [DMS of Sun and Moon Location]()
* [Visualization Idea]()
* [DMS vs DD]()
* [DMS Resolution Reference]()

DMS to DD formula
'''
decimal degrees = degrees + (minutes / 60) + (seconds / 3600)
'''

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
