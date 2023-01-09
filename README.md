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

### Data Dictionary
| variable | description |
|---|---|
| id | unique interger value |
| date | date of observation in `yyyy-mm-dd` format|
| time | time of observation in `hh:mm:ss` format |
| body | astronomical body (sun or moon). string |
| latitude | latitude of ground track in decimal degrees. float rounded 4 decimal places |
| longitude | longitude of ground track in decimal degrees. float rounded 4 decimal places |
| distance | the distance from earth to body type in kilometers. float rounded 4 decimal places |
