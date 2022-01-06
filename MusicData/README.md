# Information Visualization of Music Data

Get insights from data on musicians, bands, albums, and the US music recording industry.

## Data Sources

The data on musicians, bands, and albums is sourced from the music database run by Metason for their ArtistInfo application. ArtistInfo is available as App for iOS and macOS as well as a Web front-end at https://music.metason.net.

### Albums

- Recommended albums
  - Data: `data/recomAlbums.json`
  - Web: https://music.metason.net/greatRecords.html 
- Data was collected in 2019 by Web scrapping of
  - best-of lists of music community Web sites ()
  - top ratings of e-commerce Web sites (e.g., Amazon)

### Artists

- Famous artists and bands
  -  Data: `data/famousArtists.json`
  -  Web: https://music.metason.net/famousArtists.html 
- Data was collected in 2019 by Web scrapping of
  - Top100 lists of music community Web sites




### US Music Industry Revenues
Sales Data from Recording Industry Association of America (RIAA)
- 50+ years of sales by media, from vinyl to streaming
- Data: `data/USMusicMarket.csv`
- Sourcse: https://www.riaa.com/u-s-sales-database/ 
- Revenue in Millions USD (adjusted for inflation)



## Info Vis Process

Crreating convincing Info Vis is typically an iterative process:

1. Data Processing
2. Data Analytics & Cleansing --> `analytics/*Analytics.py`
3. Data Enhancing --> `analytics/*Enhancing.py`
4. Visual Data Mining by creating data graphics
5. Back to step 2 to improve insights into data
6. Information Visualization
   - Story: open questions, interesting insights, messages, ...
   - Layout: chart type(s), dimensions, data mappings, ...
   - Styling: color palletes, typography
   - Text Messages: title, subtitle, captions, highlights
   - Interactions & Animations (optional)
7. Back to step 1 or 2 to improve information visualization

![](infovis/images/DataVizWorkflow.png)

The good news:
- Data Processing is already done for you
- Content is unified according to classifications for
  - Music instruments:
  - Musical genres & styles:
  - World regions & countries: 
- sdsds

## Data Analytics

### Python Libraries

Gender from name in Python:

https://github.com/Bemmu/gender-from-name


## Information Visualization

### Open Questions

- Who gets more famous: Artists or Bands? --> `artistsDistribution.py`
- Get individual artists more famous than bands in recent years? --> `artistsDistributionOverTime.py`
- Top 10 countries artist split (indiv/bands)
- What are the top 10 countries of famous albums
- Where are artists coming from shown on a world map
- US vs. UK artists over years
- US vs. UK albums releases over years
- Important events in the music industry
- Genres / counry relation matrix?
- What are the most used words in album titles?  --> `wordsInTitle.py`
- Gender artists (not bands)
- Score mean or score distribution per genre
- Genres distribution
- Genres distribution over years

### Interesting Insights (Messages)

- Individual artists get more famous than bands
- Today bands are out of the game (rock bands are gone)
- ...


### Python Libraries

Word Cloud

https://github.com/amueller/word_cloud

## Tips and Tricks

- ?