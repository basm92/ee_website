import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm # A progress bar for long loops

# --- 1. Simulation Parameters ---
N_FIRMS = 500             # Number of firms
T_PERIODS = 252 * 4       # Total time periods (e.g., 4 years of trading days)
EVENT_WINDOW_START = -5   # K: Start of the event window to plot
EVENT_WINDOW_END = 5      # L: End of the event window to plot

# Market model parameters
MARKET_MEAN_RETURN = 0.0003
MARKET_STD_DEV = 0.01

# Firm-specific parameters
ALPHA_MEAN, ALPHA_STD = 0.0, 0.0005
BETA_MEAN, BETA_STD = 1.0, 0.3
EPSILON_STD = 0.02 # Idiosyncratic risk

# Define the "true" abnormal returns (delta_k) we want to recover
TRUE_EFFECTS = {
    -5: 0.001,   # Small anticipation effect
    -4: 0.001,
    -3: -0.002,
    -2: -0.001,
    -1: 0.000,
     0: 0.025,   # 2.5% abnormal return on event day
     1: 0.015,   # 1.5% post-event drift
     2: 0.008,
     3: 0.003,
     4: 0.001,
     5: 0.000
}

def simulate_finance_event_data():
    """
    Simulates panel data for a financial event study using the Market Model.
    
    Returns:
        pandas.DataFrame: A DataFrame with columns 
        ['firm_id', 'time', 'firm_return', 'market_return', 'event_date'].
    """
    #print("--- Simulating Financial Market Data (Market Model) ---")
    
    # --- a. Create basic panel structure ---
    firm_ids = range(N_FIRMS)
    time_periods = range(T_PERIODS)
    panel_index = pd.MultiIndex.from_product([firm_ids, time_periods], names=['firm_id', 'time'])
    df = pd.DataFrame(index=panel_index).reset_index()

    # --- b. Simulate Market Returns ---
    market_returns = np.random.normal(MARKET_MEAN_RETURN, MARKET_STD_DEV, T_PERIODS)
    df['market_return'] = df['time'].map(lambda t: market_returns[t])

    # --- c. Assign Firm-Specific Market Model Parameters (alpha_i, beta_i) ---
    alphas = np.random.normal(ALPHA_MEAN, ALPHA_STD, N_FIRMS)
    betas = np.random.normal(BETA_MEAN, BETA_STD, N_FIRMS)
    df['alpha'] = df['firm_id'].map(lambda i: alphas[i])
    df['beta'] = df['firm_id'].map(lambda i: betas[i])

    # --- d. Calculate "Normal" Returns using the Market Model ---
    # R_it = alpha_i + beta_i * R_mt + epsilon_it
    epsilon = np.random.normal(0, EPSILON_STD, len(df))
    df['firm_return'] = df['alpha'] + df['beta'] * df['market_return'] + epsilon
    
    # --- e. Assign a random event date for each firm (staggered design) ---
    # Ensure firms have a sufficient pre-event estimation window and post-event window
    min_event_time = 150 # Need at least this many days for estimation window
    max_event_time = T_PERIODS - 30
    event_dates = np.random.randint(min_event_time, max_event_time + 1, size=N_FIRMS)
    df['event_date'] = df['firm_id'].map(lambda i: event_dates[i])

    # --- f. Add the True Event Effect (Abnormal Return) ---
    # This is the "delta_k" that we will try to recover
    df['event_time'] = df['time'] - df['event_date']
    
    # Create a mapping from event_time to the true effect
    event_effect_map = pd.Series(TRUE_EFFECTS)
    # Add the effect to the firm's return. If event_time is not in the map, add 0.
    df['firm_return'] += df['event_time'].map(event_effect_map).fillna(0)

    #print("Simulation complete.")
    return df.drop(columns=['alpha', 'beta']) # Drop true alpha/beta, as we don't observe them

def estimate_abnormal_returns(df):
    """
    Estimates Average Abnormal Returns (AAR) using the standard event study methodology.

    Args:
        df (pandas.DataFrame): The simulated panel data.
    Returns:
        pandas.DataFrame: A DataFrame with AARs (our delta_k estimates) and CIs.
    """
    #print("\n--- Estimating Abnormal Returns (Standard Finance Method) ---")
    
    # Define estimation and event windows relative to the event date
    ESTIMATION_WINDOW = (-150, -31)
    EVENT_WINDOW = (EVENT_WINDOW_START, EVENT_WINDOW_END)
    
    all_abnormal_returns = []

    # Loop over each firm to perform its specific estimation
    # tqdm adds a helpful progress bar
    for firm_id in df['firm_id'].unique():
        firm_data = df[df['firm_id'] == firm_id].set_index('time')
        event_date = firm_data['event_date'].iloc[0]

        # --- Step 1: Define Estimation Period for this firm ---
        est_start = event_date + ESTIMATION_WINDOW[0]
        est_end = event_date + ESTIMATION_WINDOW[1]
        estimation_df = firm_data.loc[est_start:est_end]
        
        # --- Step 2: Estimate Market Model Parameters (alpha, beta) ---
        # Add a constant for the intercept (alpha)
        X = sm.add_constant(estimation_df['market_return']) 
        y = estimation_df['firm_return']
        
        model = sm.OLS(y, X).fit()
        alpha_hat, beta_hat = model.params['const'], model.params['market_return']

        # --- Step 3: Calculate Abnormal Returns in the Event Window ---
        evt_start = event_date + EVENT_WINDOW[0]
        evt_end = event_date + EVENT_WINDOW[1]
        event_df = firm_data.loc[evt_start:evt_end].copy()
        
        # Predicted "normal" return
        event_df['normal_return'] = alpha_hat + beta_hat * event_df['market_return']
        # Abnormal return
        event_df['abnormal_return'] = event_df['firm_return'] - event_df['normal_return']
        
        all_abnormal_returns.append(event_df[['event_time', 'abnormal_return']])

    # --- Step 4: Aggregate Abnormal Returns across all firms ---
    ar_df = pd.concat(all_abnormal_returns)
    
    # Calculate Average Abnormal Return (AAR) and statistics for each event day
    # AAR_k is our estimate of delta_k
    results = ar_df.groupby('event_time')['abnormal_return'].agg(['mean', 'std', 'count'])
    results = results.rename(columns={'mean': 'coef'}) # 'coef' is our AAR/delta_k

    # --- Step 5: Calculate Significance (t-stats and CIs) ---
    results['std_err'] = results['std'] / np.sqrt(results['count'])
    results['t_stat'] = results['coef'] / results['std_err']
    
    # 95% confidence interval
    z_score = 1.96 
    results['ci_lower'] = results['coef'] - z_score * results['std_err']
    results['ci_upper'] = results['coef'] + z_score * results['std_err']

    #print("\n--- Estimated Coefficients (Average Abnormal Returns) ---")
    #print(results)
    
    return results

def plot_event_study(results_df):
    """
    Plots the event study coefficients (AARs) and confidence intervals.
    (This function remains unchanged as it was correct).
    """
    #print("\n--- Generating Plot ---")
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 7))

    # Plot the point estimates (the AAR coefficients)
    plt.plot(results_df.index, results_df['coef'], marker='o', linestyle='-', color='b', label='Estimated Effect (AAR_k)')

    # Add the confidence interval as a shaded area
    plt.fill_between(results_df.index, results_df['ci_lower'], results_df['ci_upper'], color='b', alpha=0.2, label='95% Confidence Interval')

    # Add a horizontal line at y=0 for reference
    plt.axhline(0, linestyle='--', color='r', linewidth=1)
    
    # Add a vertical line to separate pre- and post-event periods
    plt.axvline(-0.5, linestyle='--', color='k', linewidth=1)

    # Customize the plot
    plt.title('Event Study: Average Abnormal Returns Around Event Date', fontsize=16)
    plt.xlabel('Event Time (k, days relative to event)', fontsize=12)
    plt.ylabel('Average Abnormal Return (AAR)', fontsize=12)
    plt.xticks(np.arange(EVENT_WINDOW_START, EVENT_WINDOW_END + 1, 1))
    # Format y-axis as percentage
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter('{:.1%}'.format))
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    plt.show()

