import sys
import os

# Add the `scripts` directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

# Import the predict_stats module
from predict_stats import predict_stats
