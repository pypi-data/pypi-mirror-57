#!/usr/bin/env python


"""GraphEmbed.

Compute a 2D embedding of a data matrix given supervised class information.
A discrete label for each instance is expected.
A graph is built where nodes are instances and there exist two types
of edges: the 'knn' edges and the 'k_shift' edges.
A knn edge is an edge to the k-th nearest instance that has the same
label.
A k_shift edge is an edge to the k-th nearest instance that is denser
and has a different label.
The density is defined as the sum of the pairwise cosine similarity between
an instance and all the other instances.
The desired edge length is the euclidean distance between the instances.
If the endpoints of an edge have the same label then the desired distance
is divided by 1 + class_bias.
A k-shift edge is deleted if at least one of the endpoints of is an
outlier.
Outlier nodes are defined as those instances that have no mutual
k neighbors.

Finally the embedding is computed as the 2D coordinates of the
corresponding graph embedding using the force layout algorithm from
Tomihisa Kamada, and Satoru Kawai. "An algorithm for drawing general
undirected graphs.", Information processing letters 31, no. 1 (1989): 7-15.

Version: 2.4
Author: Fabrizio Costa [costa@informatik.uni-freiburg.de]

Usage:
  graph_embed -i <file> -t <file> [-o NAME]
              [-c N, --class_confidence=N] [-k N] [-d N] [-z N] [-l N]
              [--correlation_transformation] [--normalization]
              [--feature_selection]
              [--min_threshold=N] [--max_threshold=N] [--random_state=N]
              [--display] [--figure_size=N] [--cmap_name=NAME]
              [--verbose] [--do_not_add_timestamp]
  graph_embed (-h | --help)
  graph_embed --version

Options:
  -i <file>                         Specify input data file in CSV format.
  -t <file>                         Specify classes data file in CSV format.
  -o NAME                           Output directory name [default: out].
  -c N, --class_confidence=N        Confidence bias for clustering
                                    [default: 1.0].
  -k N                              Number of links towards closest neighbors
                                    with same class [default: 5].
  -d N                              Number of links towards denser neighbors
                                    with a different class [default: 1]
  -z N                              Number of nearest neighbors to limit the
                                    horizon to limit search of denser neighbors
                                    of a different class [default: 10]
  -l N                              Number of mutual nearest neighbors that
                                    define outlier instances [default: 0]
  --normalization                   Convert data matrix to normalized matrix.
  --feature_selection               Select most discriminative features.
  --correlation_transformation      Convert data matrix to corr coeff matrix.
  --min_threshold=N                 Min num instances per class [default: 5]
  --max_threshold=N                 Max num instances per class [default: 400]
  --random_state=N                  Random seed [default: 1]
  --display                         Display graphs on terminal.
  --figure_size=N                   Figure size [default: 15].
  --cmap_name=NAME                  Color scheme [default: gist_ncar].
  --do_not_add_timestamp            Do not use timestamp as suffix for
                                    output directory name.
  -h --help                         Show this screen.
  --version                         Show version.
  --verbose                         Print more text.


"""
import os
import sys
import time
import logging
import logging.handlers
import collections
from docopt import docopt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import normalize
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.linear_model import SGDClassifier
from graph_layout_embedder import GraphEmbedder
from toolz import memoize

logger = logging.getLogger(__name__)


def serialize_dict(the_dict, full=True, offset='small'):
    """serialize_dict."""
    if the_dict:
        text = []
        for key in sorted(the_dict):
            if offset == 'small':
                line = '%10s: %s' % (key, the_dict[key])
            elif offset == 'large':
                line = '%25s: %s' % (key, the_dict[key])
            elif offset == 'very_large':
                line = '%50s: %s' % (key, the_dict[key])
            else:
                raise Exception('unrecognized option: %s' % offset)
            line = line.replace('\n', ' ')
            if full is False:
                if len(line) > 100:
                    line = line[:100] + '  ...  ' + line[-20:]
            text.append(line)
        return '\n'.join(text)
    else:
        return ""


def configure_logging(logger, verbosity=0, filename=None):
    """Utility to configure the logging aspects.

    If filename is None then
    no info is stored in files.
    If filename is not None then everything that is logged is dumped to
    file (including program traces).
    Verbosity is an int that can take values:
    0 -> warning, 1 -> info, >=2 -> debug.
    All levels are displayed on stdout, not on stderr.
    Please use exceptions and asserts
    to output on stderr.
    """
    logger.propagate = False
    logger.handlers = []
    log_level = logging.WARNING
    if verbosity == 1:
        log_level = logging.INFO
    elif verbosity >= 2:
        log_level = logging.DEBUG
    logger.setLevel(logging.DEBUG)
    # create console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(log_level)
    # create formatter
    cformatter = logging.Formatter('%(message)s')
    # add formatter to ch
    ch.setFormatter(cformatter)
    # add handlers to logger
    logger.addHandler(ch)

    if filename is not None:
        # create a file handler
        fh = logging.handlers.RotatingFileHandler(filename=filename,
                                                  maxBytes=10000000,
                                                  backupCount=10)
        fh.setLevel(logging.DEBUG)
        # create formatter
        fformatter = logging.Formatter('%(asctime)s | %(levelname)-6s | %(name)10s | %(filename)10s |\
   %(lineno)4s | %(message)s')
        # add formatter to fh
        fh.setFormatter(fformatter)
        # add handlers to logger
        logger.addHandler(fh)


@memoize
def _loaddata_matrix(fname):
    logger.info('Reading data from file: %s' % fname)
    data_matrix_original = []
    instance_names = []
    gene_names = []
    with open(fname) as f:
        for i, line in enumerate(f):
            if i == 0:
                instance_names = line.strip().split()[1:]
            if i > 0:
                tokens = line.strip().split('\t')
                gene_names.append(tokens[0])
                value_list = tokens[1:]
                vals = [float(j) for j in value_list]
                data_matrix_original.append(vals)
    data_matrix = np.array(data_matrix_original).T
    rows, cols = data_matrix.shape
    logger.info('#instances:%d  #features:%d' % (rows, cols))
    return data_matrix, gene_names, instance_names


@memoize
def _load_target(fname):
    logger.info('Reading data from file: %s' % fname)
    targets = []
    with open(fname) as f:
        for line in f:
            tokens = line.strip().split()
            targets.append(tokens[1])
    logger.info('read %d values ' % len(targets))
    target_names = list(sorted(set(targets)))
    lenc = LabelEncoder()
    y = lenc.fit_transform(targets)
    targets = np.array(y)
    return targets, target_names


def _select_targets(y, min_threshold=10, max_threshold=None):
    """_select_targets.

    Return the set of targets that are occurring a number of times bounded
    by min_threshold and max_threshold.
    """
    c = collections.Counter(y)
    y_sel = []
    for y_id in c:
        if c[y_id] > min_threshold:
            if max_threshold and c[y_id] < max_threshold:
                y_sel.append(y_id)
            else:
                y_sel.append(y_id)
    return y_sel


def _filter_dataset(data_matrix, y, y_sel):
    """_filter_dataset.

    Filter data matrix and target vector selecting only instances that
    belong to y_sel.
    """
    targets = []
    instances = []
    for target, instance in zip(y, data_matrix):
        if target in y_sel:
            targets.append(target)
            instances.append(instance)
    y = np.array(np.hstack(targets))
    _data_matrix = np.array(np.vstack(instances))
    return _data_matrix, y


@memoize
def pre_process(data_fname=None,
                target_fname=None,
                correlation_transformation=None,
                normalization=None,
                feature_selection=None,
                min_threshold=None,
                max_threshold=None,
                random_state=1):
    """Process data."""
    # load data
    data_matrix, gene_names, instance_names = _loaddata_matrix(data_fname)

    # prepare target
    y_orig, target_names = _load_target(target_fname)
    y_sel = _select_targets(y_orig,
                            min_threshold=min_threshold,
                            max_threshold=max_threshold)
    logger.info('original num classes: %d' % len(set(y_orig)))
    logger.info('selected %d classes with more than %d instances' %
                (len(y_sel), min_threshold))
    data_matrix, y_orig_sel = _filter_dataset(data_matrix, y_orig, y_sel)
    rows, cols = data_matrix.shape
    logger.info('num instances:%d  num features:%d' % (rows, cols))
    lenc = LabelEncoder()
    y = lenc.fit_transform(y_orig_sel)
    y = np.array(y)
    target_dict = dict()
    for i, c in enumerate(lenc.classes_):
        target_dict[i] = target_names[c]

    # normalization
    if normalization:
        logger.info('Normalization')
        data_matrix = normalize(data_matrix)

    # feature selection
    if feature_selection:
        estimator = SGDClassifier(random_state=random_state)
        cv = StratifiedKFold(n_splits=5,
                             shuffle=True,
                             random_state=random_state)
        selector = RFECV(estimator, step=20, cv=cv)
        data_matrix = selector.fit_transform(data_matrix, y)
        logger.info('Feature selection')
        rows, cols = data_matrix.shape
        logger.info('num instances:%d  num features:%d' % (rows, cols))

    # prepare data matrix
    if correlation_transformation:
        data_matrix = np.corrcoef(data_matrix)
        logger.info('Correlation coefficient transformation')
        rows, cols = data_matrix.shape
        logger.info('num instances:%d  num features:%d' % (rows, cols))
    return data_matrix, y, target_dict


def main(args):
    """Main."""
    # setup variables
    data_fname = args['-i']
    target_fname = args['-t']
    name = args['-o']
    k = int(args['-k'])
    k_quick_shift = int(args['-d'])
    knn_horizon = int(args['-z'])
    k_outliers = int(args['-l'])
    class_bias = float(args['--class_confidence'][0])
    correlation_transformation = args['--correlation_transformation']
    normalization = args['--normalization']
    feature_selection = args['--feature_selection']
    display = args['--display']
    min_threshold = int(args['--min_threshold'])
    max_threshold = int(args['--max_threshold'])
    cmap_name = args['--cmap_name']
    figure_size = int(args['--figure_size'])
    random_state = int(args['--random_state'])
    do_not_add_timestamp = args['--do_not_add_timestamp']

    # output setup
    timestamp = time.strftime('%Y_%m_%d_%H_%M_%S')
    if do_not_add_timestamp is False:
        dir_name = name + '_' + timestamp
    else:
        dir_name = name
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # logger
    if args['--verbose']:
        verbosity = 2
    else:
        verbosity = 1
    configure_logging(logger,
                      verbosity=verbosity,
                      filename=os.path.join(dir_name, 'log'))
    logger.debug(serialize_dict(args))

    # process data
    data_matrix, y, target_dict = pre_process(data_fname,
                                              target_fname,
                                              correlation_transformation,
                                              normalization,
                                              feature_selection,
                                              min_threshold,
                                              max_threshold,
                                              random_state=random_state)

    # run embedder
    logger.info('Writing to files in directory: %s' % dir_name)
    file_name = os.path.join(dir_name, 'img')

    ge = GraphEmbedder(
        class_bias=class_bias,
        k=k,
        k_quick_shift=k_quick_shift,
        k_outliers=k_outliers,
        knn_horizon=knn_horizon,
        metric='cosine')
    data_matrix_2d = ge.transform(data_matrix=data_matrix, target=y)

    # make images
    ge.display(target_dict=target_dict,
               display=display,
               display_outliers=True,
               cmap=cmap_name,
               file_name=file_name,
               figure_size=figure_size)

    ge.display_links(target_dict=target_dict,
                     display=display,
                     display_outliers=True,
                     cmap=cmap_name,
                     file_name=file_name,
                     figure_size=figure_size)

    ge.display_hull(target_dict=target_dict,
                    true_target=y,
                    display=display,
                    remove_outer_layer=False,
                    cmap=cmap_name,
                    file_name=file_name,
                    figure_size=figure_size)

    ge.display_hull_link(target_dict=target_dict,
                         true_target=y,
                         display=display,
                         remove_outer_layer=False,
                         cmap=cmap_name,
                         file_name=file_name,
                         figure_size=figure_size)

    # write additional files
    out_fname = os.path.join(dir_name, '2D_coords.txt')
    logger.info('Writing 2D coordinates to file: %s' % out_fname)
    with open(out_fname, 'w') as f:
        for row in data_matrix_2d:
            for val in row:
                f.write('%.4f ' % val)
            f.write('\n')

    out_fname = os.path.join(dir_name, 'classes.txt')
    logger.info('Writing classes to file: %s' % out_fname)
    with open(out_fname, 'w') as f:
        for t in ge.target:
            f.write('%d\n' % t)


if __name__ == '__main__':
    args = docopt(__doc__, version='graph_embed v2.4')
    main(args)
