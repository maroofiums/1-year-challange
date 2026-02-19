import numpy as np

class NeuralNetwork:
    
    def __init__(self, input_size):
        """
        input_size: number of input features
        """
        np.random.seed(42)
        self.weights = np.random.randn(input_size, 1)
        self.bias = np.zeros((1,))
    
    
    # -----------------------------
    # Activation Functions
    # -----------------------------
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def sigmoid_derivative(self, a):
        return a * (1 - a)
    
    
    # -----------------------------
    # Forward Propagation
    # -----------------------------
    
    def forward(self, X):
        """
        X shape: (m, input_size)
        """
        self.z = np.dot(X, self.weights) + self.bias
        self.a = self.sigmoid(self.z)
        return self.a
    
    
    # -----------------------------
    # Loss Function (Binary Cross Entropy)
    # -----------------------------
    
    def compute_loss(self, y_true, y_pred):
        m = y_true.shape[0]
        
        loss = -1/m * np.sum(
            y_true * np.log(y_pred + 1e-8) +
            (1 - y_true) * np.log(1 - y_pred + 1e-8)
        )
        
        return loss
    
    
    # -----------------------------
    # Backward Propagation
    # -----------------------------
    
    def backward(self, X, y, y_pred):
        m = X.shape[0]
        
        dz = y_pred - y
        dw = (1/m) * np.dot(X.T, dz)
        db = (1/m) * np.sum(dz)
        
        return dw, db
    
    
    # -----------------------------
    # Training Loop
    # -----------------------------
    
    def train(self, X, y, learning_rate=0.1, epochs=1000):
        
        for i in range(epochs):
            
            # Forward
            y_pred = self.forward(X)
            
            # Loss
            loss = self.compute_loss(y, y_pred)
            
            # Backward
            dw, db = self.backward(X, y, y_pred)
            
            # Update
            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db
            
            if i % 100 == 0:
                print(f"Epoch {i}, Loss: {loss:.4f}")
    
    
    # -----------------------------
    # Prediction
    # -----------------------------
    
    def predict(self, X):
        y_pred = self.forward(X)
        return (y_pred > 0.5).astype(int)
    
    
    # -----------------------------
    # Accuracy
    # -----------------------------
    
    def accuracy(self, y_true, y_pred):
        return np.mean(y_true == y_pred)


# ==================================================
# Example Usage
# ==================================================

if __name__ == "__main__":
    
    # Simple Dataset
    # Hours studied vs Pass(1)/Fail(0)
    X = np.array([[1], [2], [3], [4], [5], [6]])
    y = np.array([[0], [0], [0], [1], [1], [1]])
    
    # Create model
    model = NeuralNetwork(input_size=1)
    
    # Train model
    model.train(X, y, learning_rate=0.1, epochs=1000)
    
    # Predictions
    predictions = model.predict(X)
    
    print("\nPredictions:")
    print(predictions)
    
    print("\nActual:")
    print(y)
    
    acc = model.accuracy(y, predictions)
    print(f"\nAccuracy: {acc * 100:.2f}%")
