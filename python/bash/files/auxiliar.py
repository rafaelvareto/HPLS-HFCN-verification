import cv2 as cv
import matplotlib
import numpy as np
import random

matplotlib.use('Agg')

from itertools import cycle
from matplotlib import colors as mcolors
from matplotlib import pyplot as plt
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score, precision_recall_curve
from sklearn.metrics import roc_curve, roc_auc_score

def generate_probe_histogram(individuals, values, extra_name):
    plt.clf()
    plt.bar(range(len(individuals)), values)
    if sample_name == result[0][0]:
        plt.savefig('plots/' + extra_name + '_' + str(NUM_HASH) + '_' + str(counter) + '_' + sample_name + '_' + result[0][0])
    else:
        plt.savefig('plots/' + extra_name + '_' + str(NUM_HASH) + '_' + str(counter) + '_' + sample_name + '_' + result[0][0] + '_ERROR')


def generate_precision_recall(y_label_list, y_score_list):
    """
    A system with high recall but low precision returns many results, but most of its predicted labels are incorrect when compared to the training labels. 
    A system with high precision but low recall is just the opposite, returning very few results, but most of its predicted labels are correct when compared to the training labels. 
    An ideal system with high precision and high recall will return many results, with all results labeled correctly.
    """
    # Prepare input data
    label_list = [line[1] for line in y_label_list]
    score_list = [line[1] for line in y_score_list]
    label_array = np.array(label_list)
    score_array = np.array(score_list)

    # Compute micro-average ROC curve and ROC area
    pr = dict()
    pr['precision'], pr['recall'], pr['thresh'] = precision_recall_curve(label_array.ravel(), score_array.ravel())
    pr['avg_precision'] = average_precision_score(label_array, score_array, average="micro")
    return pr


def generate_roc_curve(y_label_list, y_score_list):
    """
    ROC curves typically feature true positive rate on the Y axis, and false positive rate on the X axis. 
    This means that the top left corner of the plot is the ideal point - a false positive rate of zero, and a true positive rate of one. 
    This is not very realistic, but it does mean that a larger area under the curve (AUC) is usually better.
    """
    # Prepare input data
    label_list = [line[1] for line in y_label_list]
    score_list = [line[1] for line in y_score_list]
    label_array = np.array(label_list)
    score_array = np.array(score_list)

    # Compute micro-average ROC curve and ROC area
    roc = dict()
    roc['fpr'], roc['tpr'], roc['thresh'] = roc_curve(label_array.ravel(), score_array.ravel())
    roc['auc']  = auc(roc['fpr'], roc['tpr'])
    return roc


def plot_cmc_curve(cmc_scores, extra_name):
    """
    The CMC shows how often the biometric subject template appears in the ranks (1, 5, 10, 100, etc.), based on the match rate.
    It is a method of showing measured accuracy performance of a biometric system operating in the closed-set identification task. 
    Templates are compared and ranked based on their similarity.
    """
    # Setup plot details
    color_dict = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    color_names = [name for name, color in color_dict.items()]
    colors = cycle(color_names)
    lw = 2

    # Plot Cumulative Matching Characteristic curve
    plt.clf()
    counter = 1
    for score, color in zip(cmc_scores, colors):
        x_axis = range(len(score))
        y_axis = score
        area = auc(x_axis, y_axis)/len(score)
        rank1 = score[0]
        plt.plot(x_axis, y_axis, lw=lw, color=color, label='CMC curve %d (area = %0.2f, rank-1 = %0.2f)' % (counter, area, rank1))
        counter += 1
    
    plt.xlim([0, len(score)])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Rank')
    plt.ylabel('Accuracy Rate')
    plt.title('Cumulative Matching Characteristic')
    plt.legend(loc="lower right")
    plt.grid()
    if extra_name == None:
        plt.show()
    else:
        plt.savefig('./plots/CMC_' + extra_name + '.pdf')
    plt.close()


def plot_precision_recall(prs, extra_name=None):
    # Setup plot details
    aucs = [pr['avg_precision'] for pr in prs]
    color_dict = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    color_names = [name for name, color in color_dict.items()]
    colors = cycle(color_names)
    lw = 2

    # Plot Precision-Recall curve
    plt.clf()
    for index, color in zip(range(len(prs)), colors):
        pr = prs[index]
        plt.plot(pr['recall'], pr['precision'], lw=lw, color=color, label='PR curve %d (area = %0.2f)' % (index+1, pr['avg_precision']))
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('Precision-Recall Curve (%0.3f - %0.3f)' % (np.mean(aucs),np.std(aucs)))
    plt.legend(loc="lower left")
    plt.grid()
    if extra_name == None:
        plt.show()
    else:
        plt.savefig('./plots/PR_' + extra_name + '.pdf')
    plt.close()


def plot_roc_curve(rocs, extra_name=None):
    # Setup plot details
    aucs = [roc['auc'] for roc in rocs]
    color_dict = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    color_names = [name for name, color in color_dict.items()]
    colors = cycle(color_names)
    lw = 2
    
    # Plot Receiver Operating Characteristic curve
    plt.clf()
    for index, color in zip(range(len(rocs)), colors):
        roc = rocs[index]
        plt.plot(roc['fpr'], roc['tpr'], color=color, lw=lw, label='ROC curve %d (area = %0.2f)' % (index+1, roc['auc']))
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (%0.3f - %0.3f)' % (np.mean(aucs),np.std(aucs)))
    plt.legend(loc="lower right")
    plt.grid()
    if extra_name == None:
        plt.show()
    else:
        plt.savefig('./plots/ROC_' + extra_name + '.pdf')
    plt.close()


def iteration_to_fold(prs, rocs):
    fold_prs = {}
    fold_rocs = {}
    
    # prs_avg = []
    # prs_pre = []
    # prs_rec = []
    # prs_thr = []
    # avg_prs = {}
    for row in prs:
        for col in range(len(row)):
            if fold_prs.has_key(col):
                fold_prs[col].append(row[col])
            else:
                fold_prs[col] = [row[col]]
    # for fold in fold_prs.values():
    #     for item in fold:
    #         prs_avg.append(item['avg_precision'])
    #         prs_pre.append(item['precision'])
    #         prs_rec.append(item['recall'])
    #         prs_thr.append(item['thresh'])
    #     avg_prs['avg_precision'] = np.mean(prs_avg, axis=0)
    #     avg_prs['precision'] = np.mean(prs_pre, axis=0)
    #     avg_prs['recall'] = np.mean(prs_rec, axis=0)
    #     avg_prs['thresh'] = np.mean(prs_thr, axis=0)

    # rocs_auc = []
    # rocs_fpr = []
    # rocs_thr = []
    # rocs_tpr = []
    # avg_rocs = {}
    for row in rocs:
        for col in range(len(row)):
            if fold_rocs.has_key(col):
                fold_rocs[col].append(row[col])
            else:
                fold_rocs[col] = [row[col]]
    # for fold in fold_rocs.values():
    #     for item in fold:
    #         rocs_auc.append(item['auc'])
    #         rocs_fpr.append(item['fpr'])
    #         rocs_thr.append(item['thresh'])
    #         rocs_tpr.append(item['tpr'])
    #     avg_rocs['auc'] = np.mean(rocs_auc, axis=0)
    #     avg_rocs['fpr'] = np.mean(rocs_fpr, axis=0)
    #     avg_rocs['thresh'] = np.mean(rocs_thr, axis=0)
    #     avg_rocs['tpr'] = np.mean(rocs_tpr, axis=0)
    
    return fold_prs, fold_rocs
