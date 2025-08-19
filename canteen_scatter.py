import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
conn= sqlite3.connect('cafeteria.db')
def preptime_rating():
    prep_df = pd.read_sql_query("SELECT prep_time, item_id FROM menu_items",conn)
    rating_df = pd.read_sql_query("SELECT rating, item_id FROM orders",conn)
    vs_df = pd.merge( prep_df, rating_df, on='item_id')
    vs_df = vs_df.groupby('prep_time')['rating'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.scatter(vs_df['prep_time'], vs_df['rating'], s=100, alpha=0.8)
    plt.title('prepare time vs rating')
    plt.xlabel('preptime')
    plt.ylabel('trend')

    z= np.polyfit(vs_df['prep_time'], vs_df['rating'], 1)
    p = np.poly1d(z)
    plt.plot(vs_df['prep_time'],p(vs_df['prep_time']), color='red')
    plt.show()
    print(vs_df)
preptime_rating()
