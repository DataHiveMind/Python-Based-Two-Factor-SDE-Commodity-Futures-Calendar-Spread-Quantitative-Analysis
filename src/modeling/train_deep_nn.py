"""
src/modeling/train_deep_nn.py

Purpose: This script is used to train a deep neural network model for a specific task using PyTorch.

Aim: The aim is to set up the training environment, define the model architecture, and execute the training process.
"""
import torch
import torch.nn as nn
import torch.optim as optim

#-----------------------------------------------------------
# Define the Deep Neural Network architecture
#-----------------------------------------------------------

class DeepNN(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super(DeepNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out
    
    
#-----------------------------------------------------------
# Function to train the model
#-----------------------------------------------------------
def train_model(model, train_loader, criterion, optimizer, num_epochs=10):
    model.train()
    for epoch in range(num_epochs):
        for i, (inputs, labels) in enumerate(train_loader):
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i+1) % 100 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

def save_model(model, filename):
    torch.save(model.state_dict(), filename)

#-----------------------------------------------------------
# Main function to execute the training process
#-----------------------------------------------------------

def main(): 
    # Example parameters
    input_size = 784  # e.g., for MNIST dataset
    hidden_size = 500
    output_size = 10   # e.g., number of classes in MNIST
    num_epochs = 5
    learning_rate = 0.001

    # Create model, define loss and optimizer
    model = DeepNN(input_size, hidden_size, output_size)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Assume train_loader is defined elsewhere and provides the training data
    train_loader = ...  # Placeholder for actual DataLoader

    # Train the model
    train_model(model, train_loader, criterion, optimizer, num_epochs)

#-----------------------------------------------------------
# Entry point for the script
#-----------------------------------------------------------
if __name__ == "__main__":
    main()