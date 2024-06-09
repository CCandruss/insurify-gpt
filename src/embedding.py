from pymongo import MongoClient
import numpy as np
import faiss

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)
