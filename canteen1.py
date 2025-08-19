import sqlite3
import numpy as np
import pandas as pd
def prep_time_analysis():
    conn = sqlite3.connect('cafeteria.db')
    df = pd.read_sql_query("SELECT menu_items.prep_time, orders.rating FROM orders JOIN menu_items ON orders.item_id= menu_items.item_id",conn) 
    relation = df.groupby('prep_time')['rating'].mean()

    print(f"Relation between Prep time and customer Rating")
    for prep_time, avg_rating in relation.items():
        print(f"Prep Time: {prep_time} mins, Average Rating: {avg_rating:.2f}")


prep_time_analysis()