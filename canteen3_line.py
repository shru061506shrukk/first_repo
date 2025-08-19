import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
def average_rating():
    conn = sqlite3.connect('cafeteria.db')
    rate_df = pd.read_sql_query("SELECT order_date, AVG(rating) as average_rating FROM orders GROUP BY order_date",conn)
    print(rate_df.head())
    plt.plot(rate_df['order_date'], rate_df['average_rating'], marker='o')
    plt.title('AVERAGE RATING EACH DAY')
    plt.xlabel('ORDER DATE')
    plt.ylabel('AVERAGE RATING')
    plt.xticks(rotation=45)
    plt.show()


    price_df = pd.read_sql_query("SELECT price, category, item_id FROM menu_items GROUP BY category",conn)

    quantity_df =pd.read_sql_query("SELECT quantity, item_id FROM orders",conn)
    
    revenue_df = pd.merge(price_df, quantity_df, on='item_id')
    revenue_df['revenue'] = revenue_df['price'] * revenue_df['quantity']
    revenue_df = revenue_df.groupby('category')['revenue'].sum().reset_index()
    print(revenue_df.head())

    plt.pie(revenue_df['revenue'], labels=revenue_df['category'], autopct='%1.1f%%')
    plt.title('REVENUE BY CATEGORY')
    print(revenue_df['revenue'])
    


                                   




    plt.show()
average_rating()

                   
                   