# 🛡️ Network Anomaly Detection
This project explores classical and modern techniques for detecting network anomalies, particularly focusing on identifying suspicious activities such as Denial of Service (DoS) attacks and non-signature-based threats.

# 🔍 Signature-Based Detection
We can detect known DoS activities by analyzing the uniformity of IP addresses. However, this method relies on predefined signatures and cannot detect new or unknown anomalies. It is a foundational approach in cybersecurity, and I am currently studying it as part of my academic journey.

# 🚀 Non-Signature-Based Anomaly Detection
These methods aim to detect anomalies without relying on known attack signatures. They are more complex but capable of identifying novel threats such as viruses and worms that have not yet been registered.

## Techniques:
Principal Component Analysis (PCA)
Sketch-Based Detection
Signal Analysis-Based Detection
# ⚠️ Why Non-Signature Detection Is Challenging
Signature-based systems require exact data on known threats. A hacker can bypass detection simply by modifying the code of a virus. Non-signature-based systems aim to detect behavioral patterns instead.

# 📈 Causes of Network Anomalies
Sudden changes in traffic volume
Distribution shifts in IP sources or destinations
Flash crowds (large traffic to a single destination)
Routing table changes
Port scans (probing multiple ports on few IPs)
Virus and worm activity (e.g., scanning for vulnerable hosts)
# 📊 PCA-Based Approaches
PCA transforms data into new axes (principal components) to reduce dimensionality and highlight anomalies.

Objectives:
Detect anomalies
Identify origin-destination flows causing anomalies
Estimate traffic volume involved
PCA Concepts:
First principal component: direction of maximum variance
Second component: variance remaining after the first is removed
Requires understanding of:

Covariance and variance
Matrix manipulation
Statistical estimation
# 📉 Sketch-Based Approaches
Used for scalable anomaly detection in large data streams.

Techniques:
Sliding window averaging
Exponential smoothing
Box-Jenkins ARIMA
Sketching uses probabilistic summaries and random projections to efficiently process data with constant update cost.

# 🧪 Implementation Plan
Start with PCA-based detection for small, correlated anomalies.
Separate traffic into normal and abnormal flows.
Use existing PCA libraries for implementation.
Provide a mathematical breakdown of PCA in a separate module.
# 🔮 Future Work
My next project will focus on using AI for anomaly detection, targeting unknown threats and behavioral patterns in real-time systems.
