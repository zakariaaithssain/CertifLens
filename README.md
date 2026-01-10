# IT Certifications Pipeline
 
This project scrapes, cleans, ml enforces, and plots metadata of IT certifications from providers: AWS, Microsoft, and CompTIA.

##  Features

-  Web scraping of certifications metadata.
-  Data cleaning, formatting, standardizing, concatenating and exporting.
-  Data enhancement using ML models.
-  Data analysis visualizations


##  Project Structure

- `scraping/` - Scrapers and source data
- `data/` - Cleaned, raw, and processed datasets
- `cleaning/` -Cleaners 
- `analysis/` - EDA and visualizations
- `imputing/` - machine learning based data imputers
- `a Streamlit UI`


# Note:
Web scraping classes are HTML-structure sensitive, so any changes in the layout of a website can damage the scraper.  
In this case, consider debugging the scraper's class to find and replace the tag(s) and/or attribute(s) that have been changed.
