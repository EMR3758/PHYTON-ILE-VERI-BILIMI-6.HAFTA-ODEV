import numpy as np
import matplotlib.pyplot as plt

#Ürün Satış Analizi
#Ürün isimleri
products = ["Phone", "Computer", "Headphones", "Watch", "Tablet"]

#Satış miktarlarını simüle etmek için (her ürün için 30 günlük satış)
sales_data = {product: np.random.randint(10, 101, size=30) for product in products}

#Her ürünün toplam ve ortalama satış miktarlarını hesaplama
sales_summary = {
    product: {
        "total_sales": np.sum(sales_data[product]),
        "average_sales": np.mean(sales_data[product])
    }
    for product in products
}

#Ürün bazında çubuk grafiği çizme
total_sales = [sales_summary[product]["total_sales"] for product in products]
plt.figure(figsize=(10, 6))
plt.bar(products, total_sales, color='skyblue')
plt.title("Total Sales for Each Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

