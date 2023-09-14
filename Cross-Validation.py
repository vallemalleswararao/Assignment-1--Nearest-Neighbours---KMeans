from sklearn.model_selection import cross_val_score

# Initialize KNN regressor
knn = KNeighborsRegressor(n_neighbors=5)  # Start with an arbitrary k value

# Perform cross-validation with different k values
k_values = [1, 3, 5, 7, 9, 11, 13, 15]
cv_scores = []

for k in k_values:
    knn.n_neighbors = k
    scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    cv_scores.append(-scores.mean())

# Find the best k value
best_k = k_values[cv_scores.index(min(cv_scores))]

print(f"Best k value: {best_k}")
