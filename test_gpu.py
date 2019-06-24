
from __future__ import print_function
import os
import warnings
import argparse
import numpy as np
import pandas as pd
import lightgbm as lgb
from timer import elapsed
from azureml.core import Run
import azureml.core
print('azureml.core.VERSION={}'.format(azureml.core.VERSION))

warnings.filterwarnings(action='ignore', category=UserWarning, module='lightgbm')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Fit and evaluate a model'
                                     ' based on train-test datasets.')
    parser.add_argument('--data-folder', help='the path to the data',
                        dest='data_folder', default='.')
    parser.add_argument('--inputs', help='the inputs directory',
                        default='data')
    parser.add_argument('--data', help='the training dataset name',
                        default='HIGGS_train.csv')
    parser.add_argument('--test', help='the test dataset name',
                        default='HIGGS_test.csv')
    parser.add_argument('--estimators',
                        help='the number of learner estimators',
                        type=int, default=50)
    parser.add_argument('--min_child_samples',
                        help='the minimum number of samples in a child(leaf)',
                        type=int, default=1)
    parser.add_argument('--device', help='the device type', default='gpu')
    parser.add_argument('--threads', help='the number of threads',
                        type=int, default=-1)
    parser.add_argument('--verbose',
                        help='the verbosity of the estimator',
                        type=int, default=1)
    args = parser.parse_args()

    # Get a run logger.
    run = Run.get_context()
    
    print('Prepare the training data.')
    
    # Paths to the input data.
    data_path = args.data_folder
    inputs_path = os.path.join(data_path, args.inputs)
    data_path = os.path.join(inputs_path, args.data)
    test_path = os.path.join(inputs_path, args.test)

    # Load the data.
    print('Reading {}'.format(data_path))
    train = pd.read_csv(data_path, sep=',', header=None, encoding='latin1')
    train.columns = ["y"] + ["x{}".format(i) for i in range(1, train.shape[1])]

    print('Reading {}'.format(test_path))
    test = pd.read_csv(test_path, sep=',', header=None, encoding='latin1')
    test.columns = train.columns

    # Define the input data columns.
    feature_columns = train.columns[1:]
    label_column = train.columns[0]

    # Report on the dataset.
    print('train: {:,} rows'.format(train.shape[0]))
    print('test: {:,} rows'.format(test.shape[0]))
    
    # Select and format the training data.
    train_X = train[feature_columns]
    train_y = train[label_column]
    test_X = test[feature_columns]
    test_y = test[label_column]

    # Select the training hyperparameters.
    n_estimators = args.estimators
    min_child_samples = args.min_child_samples
    device_type = args.device
    num_threads = args.threads
    verbose = args.verbose

    # Verify that the hyperparameter settings are valid.
    if n_estimators <= 0:
        raise Exception('n_estimators must be > 0')
    if min_child_samples <= 0:
        raise Exception('min_child_samples must be > 0')
    if device_type not in ["gpu", "cpu"]:
        raise Exception("device must be one of 'gpu' or 'cpu'")
    if num_threads < -1:
        raise Exception('threads must be >= -1')

    # Define the estimator.
    # estimator = lgb.LGBMClassifier(n_estimators=n_estimators,
    #                                min_child_samples=min_child_samples,
    #                                verbose=verbose,
    #                                device_type=device_type,
    #                                num_threads=num_threads,
    #                                metric="auc",
    #                                max_bin=63,
    #                                num_leaves=255,
    #                                min_sum_hessian_in_leaf=100,
    #                                sparse_threshold=1.0)
    estimator = lgb.LGBMClassifier(n_estimators=n_estimators,
                                   min_child_samples=min_child_samples,
                                   verbose=verbose,
                                   device_type=device_type,
                                   num_threads=num_threads)
    
    # Report the featurization.
    print('Estimators={:,}'.format(n_estimators))
    print('Min child samples={}'.format(min_child_samples))
    print('Device={}'.format(device_type))
    print('Threads={}'.format(num_threads))

    # Fit the model.
    print('Fitting the model.')
    elapsed(estimator.fit)(train_X, train_y,
                           eval_set=[(test_X, test_y)],
                           eval_names=["test"], verbose=False)
