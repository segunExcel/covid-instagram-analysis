# Five Years of COVID-19 Discourse on Instagram

**Multilingual sentiment, emotion and topic analysis of 500,153 Instagram posts (2020–2024).**

## Overview
This project analyses COVID-19-related Instagram posts to understand how public discourse changed over time. The work combines Python, R and Power BI across data preparation, multilingual processing, sentiment analysis, emotion classification, topic modelling and visualisation.

## Dataset
- 500,153 Instagram posts
- January 2020 to September 2024
- 161 languages in the source dataset
- English and Spanish selected for the multilingual analysis

The original dataset was supplied as part of the MSc research project and is not committed to this repository.

## Methods
### Python
- Exploratory data analysis
- Language filtering
- English/Spanish dataset creation
- Spanish-to-English translation
- Text preprocessing
- Gensim LDA topic modelling
- Coherence-based topic selection
- Topic trends by year and language

### R
- Syuzhet lexicon-based sentiment scoring
- Positive / neutral / negative classification
- NRC Emotion Lexicon analysis
- Temporal emotion trends

### Power BI
- Interactive visualisation of selected analytical outputs

## Topics identified
1. Public Health and Medical Information
2. Social Media Engagement and Online Communication
3. Societal Concerns and Emotional Responses

## Repository structure
```text
project-01-covid-instagram/
├── README.md
├── data/
│   └── README.md
├── notebooks/
│   └── 30094250_thesis_python.ipynb
├── R/
│   └── 30094250_Thesis_r.Rmd
├── src/
│   └── analysis.py
└── visuals/
    ├── sentiment-over-time.png
    ├── emotion-trends.png
    ├── topic-terms.png
    ├── topic-evolution.png
    └── language-comparison.png
```
