import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect('cafeteria.db')
def max_item():
    order_df = pd.read_sql_query("SELECT item_id, SUM(quantity) as highest FROM orders GROUP BY item_id",conn)
    item_df = pd.read_sql_query("SELECT item_id, item_name FROM menu_items",conn)
    df = pd.merge(order_df, item_df, on='item_id')
    max_5 = df.nlargest(5, 'highest')
    print(max_5)
    plt.bar(max_5['item_name'],max_5['highest'])
    plt.title('TOP % ITEMS ')
    plt.xlabel('ITEM NAME')
    plt.ylabel('QUANTITY SOLD')
    plt.xticks(rotation=45)
    plt.show()
max_item()
    


