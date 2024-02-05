import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity 
customer_id = int(input("Enter a valid Customer ID from the dataset : ")) 
dataset = pd.read_excel(r"C:\Users\finugalu\Desktop\intrainz\onlineretail.xlsx") 
df = dataset[['CustomerID', 'StockCode', 'Description']] 
df = df.dropna()   
df['CustomerID'] = df['CustomerID'].astype(int)   
df['StockCode'] = df['StockCode'].astype(str) 
matrix = df.pivot_table(index='CustomerID', columns='Description', 
aggfunc=len, fill_value=0) 
cosine_sim = cosine_similarity(matrix) 
def get_product_recommendations(customer_id, cosine_sim=cosine_sim, 
    matrix=matrix, df=df): 
    idx = matrix.index.get_loc(customer_id) 
    sim_scores = list(enumerate(cosine_sim[idx])) 
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) 
    sim_scores = sim_scores[1:11] 
    customer_indices = [i[0] for i in sim_scores] 
    recommendations = matrix.iloc[customer_indices,:].sum().sort_values(ascending=False).head(10) 
    return recommendations 
recommended_products = get_product_recommendations(customer_id) 
print("Recommended Products for Customer ID", customer_id) 
print(recommended_products) 
