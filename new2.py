file_path = r'C:\Users\KANISHKA SAKTHIVEL\Desktop\Jupyter\food_ingredients_and_allergens.csv'
df = pd.read_csv(file_path)


df['Allergens'] = df['Allergens'].str.split(',')
allergens_df = df.explode('Allergens')


allergens_df['Allergens'] = allergens_df['Allergens'].str.strip()


allergen_counts = allergens_df['Allergens'].value_counts()


plt.figure(figsize=(12, 8))
allergen_counts.sort_index().plot(kind='line', marker='o', color='skyblue')
plt.title('Frequency of Allergens in Food Products')
plt.xlabel('Allergens')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)



plt.tight_layout()
plt.show()