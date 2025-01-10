import sys
import os

# Add the `scripts` folder to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

# Now import predict_stats
from predict_stats import predict_stats
