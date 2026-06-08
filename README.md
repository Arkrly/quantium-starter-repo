# Quantium starter repo

This repository contains starter materials and sample data used in the Quantium exercises.

**Setup**
- Create and activate a virtual environment (recommended): `python -m venv .venv && source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**Data**
- The `data/` folder contains sample CSV files used for exercises:
	- `daily_sales_data_0.csv`
	- `daily_sales_data_1.csv`
	- `daily_sales_data_2.csv`

These can be combined for analysis, for example by using `pandas` to concatenate all matching files.

**Quick usage**
- Merge and inspect the data from the command line:

```
python -c "import pandas as pd, glob; df=pd.concat([pd.read_csv(f) for f in glob.glob('data/daily_sales_data_*.csv')], ignore_index=True); print(df.shape); print(df.head())"
```

If you'd like, I can add example notebooks or scripts that demonstrate common analyses (data cleaning, aggregation, visualization).


