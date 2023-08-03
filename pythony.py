# a code of anomalies detection using PCA approach
import numpy as np
from sklearn.decomposition import PCA
def libPCA():
  data = np.loadtxt('data.txt')#data loading
  pca = PCA(n_components=2)
  pca.fit(data)
  transformed_data = pca.transform(data)
  distances = np.linalg.norm(transformed_data, axis=1)# Calculate the distance from the center of the data for each point
  anomalies = np.where(distances > np.mean(distances) + 3 * np.std(distances))[0]  # Identify the points that are potential anomalies and threats to the data system
  print(anomalies)
def PCA():
  data = np.loadtxt('data.txt')
  # first : Calculate the covariance matrix
  covariance_matrix = np.cov(data.T)
  # second : Calculate the eigenvalues and eigenvectors of the covariance matrix
  eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
  # third : Sort the eigenvalues and eigenvectors in descending order
  idx = eigenvalues.argsort()[::-1]
  eigenvalues = eigenvalues[idx]
  eigenvectors = eigenvectors[:, idx]
  # finally :Select the top n eigenvectors and project the data onto the resulting subspace
  n = 2
  projected_data = data.dot(eigenvectors[:, :n])
  distances = np.linalg.norm(projected_data, axis=1)
  anomalies = np.where(distances > np.mean(distances) + 3 * np.std(distances))[0]  # Identify the points that are more than 3 standard deviations from the mean distance
  # Print the indices of the anomalous points
  print(anomalies)
