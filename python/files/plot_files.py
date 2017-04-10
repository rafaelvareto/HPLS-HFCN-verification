import numpy as np
import pickle

from auxiliar import generate_precision_recall, plot_precision_recall
from auxiliar import generate_roc_curve, plot_roc_curve

with open('./files/plot_set_1_label_100_hog_5.file') as infile:
    file_prs, file_rocs = pickle.load(infile)



plot_precision_recall(file_prs)
plot_roc_curve(file_rocs)