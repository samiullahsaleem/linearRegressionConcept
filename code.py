from sklearn.linear_model import LinearRegression
# Load the data
X = [[1], [2], [3], [4], [5],[6],[7],[8],[9],[10]]
y = [8, 16, 24, 32, 40, 48,56,64,72,80]

# Create the model
model = LinearRegression()
X = np.array(X)
y = np.array(y)
# Train the model on the data
model.fit(X, y)
test = [[30000]]
z = model.predict(test)
print(int(z))


