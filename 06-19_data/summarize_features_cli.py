
import argparse
import pandas as pd

def summarize_dataset(csv_path):
    df = pd.read_csv(csv_path)

    # Skaitiniai (continuous) požymiai
    continuous = df.select_dtypes(include=['int64', 'float64'])
    continuous_summary = pd.DataFrame({
        'Feature': continuous.columns,
        'Count': continuous.count().values,
        '% Miss': continuous.isnull().mean().values * 100,
        'Card.': continuous.nunique().values,
        'Min': continuous.min().values,
        'Q1': continuous.quantile(0.25).values,
        'Mean': continuous.mean().values,
        'Median': continuous.median().values,
        'Q3': continuous.quantile(0.75).values,
        'Max': continuous.max().values,
        'Std. Dev.': continuous.std().values
    })

    # Kategoriniai požymiai
    categorical = df.select_dtypes(include=['object'])

    def mode_info(series):
        modes = series.mode()
        mode = modes[0] if not modes.empty else None
        second_mode = modes[1] if len(modes) > 1 else None
        freq = series.value_counts()
        mode_freq = freq.iloc[0] if not freq.empty else 0
        second_mode_freq = freq.iloc[1] if len(freq) > 1 else 0
        return pd.Series([mode, mode_freq,
                          (mode_freq / len(series.dropna())) * 100 if len(series.dropna()) else 0,
                          second_mode, second_mode_freq,
                          (second_mode_freq / len(series.dropna())) * 100 if len(series.dropna()) > 1 else 0])

    categorical_summary = categorical.apply(mode_info).T
    categorical_summary.columns = ['Mode', 'Mode Freq', 'Mode %', '2nd Mode', '2nd Mode Freq', '2nd Mode %']
    categorical_summary.insert(0, 'Card.', categorical.nunique())
    categorical_summary.insert(0, '% Miss', categorical.isnull().mean() * 100)
    categorical_summary.insert(0, 'Count', categorical.count())
    categorical_summary.insert(0, 'Feature', categorical.columns)

    return continuous_summary, categorical_summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate feature summaries from a CSV file.")
    parser.add_argument("csv_path", help="Path to the CSV file")
    parser.add_argument("--out_cont", help="Path to save continuous summary (CSV)", default="continuous_summary.csv")
    parser.add_argument("--out_cat", help="Path to save categorical summary (CSV)", default="categorical_summary.csv")

    args = parser.parse_args()

    cont_summary, cat_summary = summarize_dataset(args.csv_path)

    cont_summary.to_csv(args.out_cont, index=False)
    cat_summary.to_csv(args.out_cat, index=False)

    print(f"Saved continuous summary to {args.out_cont}")
    print(f"Saved categorical summary to {args.out_cat}")

"""
USE
python summarize_features_cli.py tavo_failas.csv
python summarize_features_cli.py tavo_failas.csv --out_cont cont.csv --out_cat cat.csv

# Šis įrankis automatiškai sugeneruos abi lenteles (skaitines ir kategorines) ir išsaugos kaip CSV. 
"""