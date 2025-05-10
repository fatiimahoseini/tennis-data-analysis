# 🎾 Tennis Data Analysis Project

This repository contains an in-depth analysis of professional tennis matches over a two-month period, using structured daily datasets. The analysis is focused on answering 17 specific questions using raw match data, player statistics, rankings, and other performance metrics.

## 📁 Dataset Structure

The dataset is organized by daily folders from `2024-02-01` to `2024-03-31`, each containing six subfolders:
- `raw_match_parquet`
- `raw_odds_parquet`
- `raw_point_by_point_parquet`
- `raw_statistics_parquet`
- `raw_tennis_power_parquet`
- `raw_votes_parquet`

Each subfolder contains hundreds of `.parquet` files, and efficient column selection and memory optimization techniques were used to manage the large dataset.

## ❓ Analysis Questions

The analysis aims to answer the following 17 questions:

1. **How many tennis players are included in the dataset?**  
2. **What is the average height of the players?**  
3. **Which player has the highest number of wins?**  
4. **What is the longest match recorded in terms of duration?**  
5. **How many sets are typically played in a tennis match?**  
6. **Which country has produced the most successful tennis players?**  
7. **What is the average number of aces per match?**  
8. **Is there a difference in the number of double faults based on gender?**  
9. **Which player has won the most tournaments in a single month?**  
10. **Is there a correlation between a player's height and their ranking?**  
11. What is the average duration of matches?  
12. What is the average number of games per set in men's matches compared to women's matches?  
13. What is the distribution of left-handed versus right-handed players?  
14. What is the most common type of surface used in tournaments?  
15. How many distinct countries are represented in the dataset?  
16. Which player has the highest winning percentage against top 10 ranked opponents?  
17. What is the average number of breaks of serve per match?

✅ So far, **questions 1–10** have been fully answered. The rest are in progress.

## 🛠️ Tools & Technologies

- **Python 3.10**
- **Pandas & PyArrow**
- **Polars** (for high-speed parquet handling)
- **Matplotlib / Seaborn** (for visualizations)
- **Jupyter Notebook** (for interactive analysis)

## 📊 Example Insights

- Over 1200 unique players identified.
- Average height: ~185 cm.
- Player with most wins: 🏆 Basilashvili, Nikoloz - 🟢 Wins: 56
- Longest match: 4h 38min.
- Positive correlation (r ≈ 0.32) between height and ranking.

👉 Full answers and visualizations are available in the [notebooks folder](./notebooks).

## 🚧 Work in Progress

- Questions 11 to 17 will be completed in upcoming commits.
- Final report and cleaned dataset will be added soon.

## 📎 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis notebooks
jupyter notebook
```

## 📬 Contact
For questions, feedback, or collaboration:
  - Email: fatiimahoseini@gmail.com
  - Linkedin: [fatima hosseini](https://www.linkedin.com/in/fatiimahoseini/)
