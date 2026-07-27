# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 11:46:07 2025

@author: Ganesh Gajjala
"""

import os
import pandas as pd
from sklearn.cluster import HDBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns

# Suppress chained assignment warning
pd.options.mode.chained_assignment = None  

# Configuration Constants
INPUT_FILE = 'TH4_20240301_030202.csv'
MIN_DEPTH = -1000
MAX_DEPTH = -10
PLOT_FREQUENCY = 10
LEGEND_MAP = {
    -2: 'Outliers', 
    -1: 'Wasserstandbereich', 
     0: 'Gasphase',
     1: 'Flüssigphase'
}

def load_and_prepare_data(file_path: str) -> pd.DataFrame:
    """Loads CSV file without transposing to keep memory footprints low."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target data file {file_path} not found.")
    return pd.read_csv(file_path, encoding='unicode_escape', header=None)

def process_column(data: pd.DataFrame, col_idx: int):
    """Processes a single column slice, filters ROI, and applies HDBSCAN."""
    # Slice rows using direct column indexes instead of transposing the full matrix
    # CONFIDENTIAL
    # CONFIDENTIAL
    # CONFIDENTIAL
    
    # Extract depth array (row 0 contains headers/times, drop it for extraction)
    # CONFIDENTIAL
    # CONFIDENTIAL
    # CONFIDENTIAL
    
    # Construct processing dataframe
    # CONFIDENTIAL
    # CONFIDENTIAL
    # CONFIDENTIAL
    
    # Filter the Region of Interest (ROI)
    # CONFIDENTIAL
    # CONFIDENTIAL
    # CONFIDENTIAL
    
    if df_roi.empty:
        return log_time, df_slice, df_roi
        
    # Scale ROI data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_roi[['Depth', 'Temp']])
    
    # Apply HDBSCAN clustering
    # CONFIDENTIAL
    # CONFIDENTIAL
    # CONFIDENTIAL
    
    return log_time, df_slice, df_roi

def generate_plots(df_slice: pd.DataFrame, df_roi: pd.DataFrame, log_time: str, index: int):
    """Generates and saves the evaluation subplots."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 16))
    
    # Plot 1: Temperature with depth (all data)
    sns.scatterplot(
        data=df_slice, x='Temp', y='Depth', hue='Temp', 
        palette='seismic', s=50, alpha=1, linewidth=0, ax=ax1
    )
    ax1.legend(title='Temperatur [°C]')
    ax1.set_title(f'Temperatur mit der Tiefe\n{log_time}')
    ax1.set_xlabel('Temperatur [°C]')
    ax1.set_ylabel('Tiefe [m]')
    ax1.grid(True)
    
    # Dynamic positioning for reference arrow based on current temperature data
    temp_mid = df_slice['Temp'].median()
    ax1.annotate('', xy=(temp_mid + 5, -500), xytext=(temp_mid, -500), 
                 arrowprops=dict(facecolor='orange', shrink=0.05))
    
    # Highlight specific target domain box
    rect = patches.Rectangle(
        (df_slice['Temp'].min() - 2, MIN_DEPTH), 
        (df_slice['Temp'].max() - df_slice['Temp'].min() + 4), 
        abs(MIN_DEPTH), 
        linewidth=4, edgecolor='orange', linestyle='-', facecolor='none'
    )
    ax1.add_patch(rect)
    
    # Plot 2: HDBSCAN Clustering
    sns.scatterplot(
        data=df_roi, x='Temp', y='Depth', 
        hue=df_roi['h_labels'].map(LEGEND_MAP),
        palette='bright', s=50, alpha=1, edgecolor='none', 
        ax=ax2, legend='full'
    )
    ax2.legend(title='Labels')
    ax2.set_title('HDBSCAN-Clustering \nvon Temperaturdaten')
    ax2.set_xlabel('Temperatur [°C]')
    ax2.set_ylabel('Tiefe [m]')
    ax2.grid(True)
    
    # File output handling
    plt.tight_layout()
    plt.savefig(f'SLS_Temp_sensing_HDBSCAN_n2{index}.png', dpi=120)
    plt.show()
    plt.close(fig) # Free up memory allocation

def main():
    # Load source matrix
    raw_data = load_and_prepare_data(INPUT_FILE)
    
    # Setup track log containers
    acq_dates = []
    
    # Iteration bounds (Loop over rows now instead of columns due to no transposition)
    num_rows = len(raw_data)
    
    for i in range(1, num_rows):
        log_time, df_slice, df_roi = process_column(raw_data, col_idx=i)
        acq_dates.append(log_time)
        
        # Plot evaluation visualization frames
        if i % PLOT_FREQUENCY == 0 and not df_roi.empty:
            generate_plots(df_slice, df_roi, log_time, i)

if __name__ == '__main__':
    main()
