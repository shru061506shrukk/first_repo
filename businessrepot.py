import sqlite3
import pandas as pd
import numpy as np
conn = sqlite3.connect('cafeteria.db')
def business_report():
    price_df = pd.read_sql_query("SELECT price, item_id, item_name FROM menu_items",conn)
    quantity_df = pd.read_sql_query("SELECT quantity, item_id, rating FROM orders",conn)
    revenue_df = pd.merge(price_df,quantity_df, on='item_id')
    revenue_df['revenue'] = revenue_df['price'] * revenue_df['quantity']
    total_revenue= revenue_df['revenue'].sum()
    print("TOTAL REVENUE = ",total_revenue)



    # max ordered item
    revenue_df = revenue_df.groupby(['item_id', 'item_name'])['revenue'].sum()
    print(revenue_df)

    avg_rating= quantity_df['rating'].mean()
    print("AVERAGE CUSTOMER SATISFACTION =",avg_rating)
    
   
business_report()

