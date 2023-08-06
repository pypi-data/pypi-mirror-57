# adobo.
#
# Description: An analysis framework for scRNA-seq data.
#  How to use: https://oscar-franzen.github.io/adobo/
#     Contact: Oscar Franzén <p.oscar.franzen@gmail.com>
"""
Summary
-------
This module contains a data storage class.
"""

import joblib
import pandas as pd
import numpy as np

import adobo

from ._constants import ASSAY_NOT_DONE

class dataset:
    """
    Storage container for raw, imputed and normalized data as well as analysis results.

    Attributes
    ----------
    _assays : `dict`
        Holding information about what functions have been applied.
    count_data : :class:`pandas.DataFrame`
        Raw read count matrix.
    imp_count_data : :class:`pandas.DataFrame`
        Raw data after imputing dropouts.
    _low_quality_cells : `list`
        Low quality cells identified with :py:meth:`adobo.preproc.find_low_quality_cells`.
    _norm_data : `dict`
        Stores all analysis results. A nested dictionary.
    meta_cells : `pandas.DataFrame`
        A data frame containing meta data for cells.
    meta_genes : `pandas.DataFrame`
        A data frame containing meta data for genes.
    desc : `str`
        A string describing the dataset.
    sparse : `bool`
        Represent the data in a sparse data structure. Will save memory at the expense
        of time. Default: True
    output_file : `str`, optional
        A filename that will be used when calling save().
    version : `str`
        The adobo package version used to create this data object.
    """
    def __init__(self, raw_mat, desc='no desc set', output_file=None, input_file=None,
                 sparse=True, verbose=False):
        # holding info about which assays have been done
        self.sparse = sparse
        self.hvg = []
        self.hvg_method = ASSAY_NOT_DONE
        self.desc = desc
        self.output_file = output_file
        self.input_file = input_file
        self._assays = {}
        if self.sparse:
            if verbose:
                print('Using a sparse matrix structure, please wait')
            self.count_data = raw_mat.astype(pd.SparseDtype("int", 0))
        else:
            self.count_data = raw_mat
        self._low_quality_cells = ASSAY_NOT_DONE
        self.imp_count_data = pd.DataFrame()
        # the nested dictionary containing results and analyses
        self._norm_data = {}
        # meta data for cells
        self.meta_cells = pd.DataFrame(index=raw_mat.columns)
        self.meta_cells['total_reads'] = raw_mat.sum(axis=0)
        self.meta_cells['status'] = ['OK']*raw_mat.shape[1]
        self.meta_cells['detected_genes'] = np.sum(raw_mat > 0, axis=0)
        # meta data for genes
        self.meta_genes = pd.DataFrame(index=raw_mat.index)
        if verbose:
            print('Generating cell summary statistics...')
        self.meta_genes['expressed'] = [np.sum(x>0) for _, x in raw_mat.iterrows()]
        self.meta_genes['expressed_perc'] = self.meta_genes.expressed/raw_mat.shape[1]*100
        self.meta_genes['status'] = ['OK']*raw_mat.shape[0]
        self.meta_genes['mitochondrial'] = [None]*raw_mat.shape[0]
        self.meta_genes['ERCC'] = [None]*raw_mat.shape[0]
        if verbose:
            print('Memory usage of loaded data: %s MB' % self.df_mem_usage('count_data'))
        self.version = adobo.__version__

    def df_mem_usage(self, var):
        """Memory usage for a data frame in mega bytes

        Parameters
        ----------
        var : `str`
            Variable name as a string.

        Returns
        -------
        `float`
            Mega bytes used with two decimals.
        """
        df = getattr(self, var)
        return '%.2f' % (df.memory_usage().sum()/1024/1024)

    def _print_raw_dimensions(self):
        genes = '{:,}'.format(self.count_data.shape[0])
        cells = '{:,}'.format(self.count_data.shape[1])
        return '%s genes and %s cells' % (genes, cells)

    def save(self, filename=None, compress=True, verbose=False):
        """Serializes the object

        Notes
        -----
        This is a method so that it is not needed to memorize the filename, instead the
        filename was already specified when the object was created with the
        `output_file` parameter. Load the object data with `joblib.load`.

        Parameters
        ----------
        filename : `str`
            Output filename. Default: None
        compress : `bool`
            Save with data compression or not. Default: True
        verbose : `bool`
            Be verbose or not. Default: False

        Returns
        -------
        Nothing.
        """
        if not self.output_file and not filename:
            raise Exception('No output filename set.')
        else:
            if self.output_file:
                fn = self.output_file
            else:
                fn = filename
            joblib.dump(self, filename=fn, compress=compress)
            if verbose:
                print('Wrote to %s' % fn)

    def get_assay(self, name, lang=False):
        """ Get info if a function has been applied. """
        if lang:
            return ('No', 'Yes')[name in self._assays]
        return name in self._assays

    def set_assay(self, name, key=1):
        """ Set the assay that was applied. """
        self._assays[name] = key
    
    def print_dict(self):
        q = []
        self._print_dict(self.norm_data, q)
        return '\n'.join(q)
        
    def _print_dict(self, d, q, indent=0):
        """Recursive function for printing content of norm_data """
        for key, value in d.items():
            s = '\t' * indent + str(key)
            q.append(s)
            if isinstance(value, dict):
                self._print_dict(value, q, indent+1)

    @property
    def norm_data(self):
        return self._norm_data

    @norm_data.setter
    def norm_data(self, val):
        self._norm_data = val

    @property
    def low_quality_cells(self):
        return self._low_quality_cells

    @low_quality_cells.setter
    def low_quality_cells(self, val):
        self._low_quality_cells = val

    def _describe(self):
        """ Helper function for __repr__. """
        genes_pre_filter = '{:,}'.format(self.count_data.shape[0])
        cells_pre_filter = '{:,}'.format(self.count_data.shape[1])
        genes_post_filter = (self.meta_genes.status=='OK').sum()
        cells_post_filter = (self.meta_cells.status=='OK').sum()
        genes_post_filter = '{:,}'.format(genes_post_filter)
        cells_post_filter = '{:,}'.format(cells_post_filter)
        s = """Filename (input): %s
Description: %s
Raw count matrix: %s genes and %s cells (filtered: %sx%s)

Commands executed:
""" % (self.input_file, self.desc, genes_pre_filter, cells_pre_filter, genes_post_filter,
       cells_post_filter)

        for key in self._assays:
            if self._assays[key] != 1:
                s += '%s (%s)\n' % (key, self._assays[key])
            else:
                s += '%s\n' % key
        s += '\nNormalizations available:\n'
        for item in self.norm_data:
            s += '%s\n' % item
        s += '\nnorm_data structure:\n%s\n' % self.print_dict()
        return s

    def assays(self):
        """
        Displays a basic summary of the dataset and what analyses have been performed on
        it.
        """
        if self.get_assay('find_mitochondrial_genes'):
            s = np.sum(self.meta_genes['mitochondrial'])
            print('Number of mitochondrial genes found: %s' % s)
        if self.get_assay('detect_ercc_spikes'):
            print('Number of ERCC spikes found: %s ' % np.sum(self.meta_genes['ERCC']))
        if self.get_assay('find_low_quality_cells'):
            print('Number of low quality cells found: %s ' % self.low_quality_cells.shape[0])
        #if self.get_assay('norm'):
        #    print('Normalization method: %s ' % self.norm_method)
        #    print('Log2 transformed? %s' % (self.norm_log2))
        s = 'Has HVG discovery been performed? %s' % self.get_assay('find_hvg', lang=True)
        print(s)
        if self.get_assay('pca'):
            print('pca has been performed')
        #cd = ', '.join([ item['algo'] for item in self.clusters ])
        #print('The following community detection methods have been invoked: %s' % cd)

    def __repr__(self):
        return self._describe()

    def is_normalized(self):
        """Checks if normalized data can be found

        Returns
        -------
        `bool`
            True if it is normalized otherwise False.
        """
        return True if len(self.norm_data) > 0 else False

    def add_meta_data(self, axis, key, data, type_='cat'):
        """Add meta data to the adobo object

        Notes
        -----
        Meta data can be added to cells or genes.

        The parameter name 'type_' has an underscore to avoid conflict with Python's
        internal type keyword.

        Parameters
        ----------
        axis : `{'cells', 'genes'}`
            Are the data for cells or genes?
        key : `str`
            The variable name for your data. No whitespaces and special characters.
        data : `numpy.ndarray`, `list` or `pandas.Series`
            Data to add. Can be a basic Python `list`, a numpy array or a Pandas Series
            with an index. If the data type is numpy array or list, then the length must
            match the length of cells or genes. If the data type is a Pandas series, then
            the length does not need to match as long as the index is there. Data can be
            continuous or categorical and this must be specified with `type_`.
        type_ : `{'cat', 'cont'}`
            Specify if data are categorical or continuous. `cat` means categorical data
            and `cont` means continuous data. Default: 'cat'

        Returns
        -------
        Nothing.
        """
        if not type_ in ('cat', 'cont'):
            raise Exception('`type_` can only be "cat" or "cont".')
        if not type(data) in (list, np.ndarray, pd.Series):
            raise Exception('`data` should be a numpy array or list.')
        if not axis in ('cells', 'genes'):
            raise Exception('Dimension must be "cells" or "genes".')
        if axis == 'cells':
            target = self.meta_cells
        elif axis == 'genes':
            target = self.meta_genes
        target[key] = data
        if type_ == 'cat':
            target[key] = target[key].astype('category')
    
    def delete(self, what):
        """Deletes analysis results from the norm_data dictionary 

        Parameters
        ----------
        what : `str`, `tuple`
            A string (or tuple of strings) specifying keys of what you want to delete.
            Each string should be a key in norm_data.
        
        Example
        -------
        >>> import adobo as ad
        >>> exp = ad.IO.load_from_file('pbmc8k.mat.gz', bundled=True)
        >>> ad.normalize.norm(exp)
        >>> ad.hvg.find_hvg(exp)
        >>> ad.dr.pca(exp)
        >>> ad.clustering.generate(exp)
        >>> exp.norm_data['standard']['clusters']['leiden']
            {'membership': V1        6
            V2        0
            V3        5
            V4        1
            V5        0
                     ..
            V8377     1
            V8378    10
            V8379    11
            V8380     3
            V8381     2
            Length: 8381, dtype: int64}
        >>> exp.delete(what=('clusters',))
        >>> exp.norm_data['standard']['clusters']['leiden']
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            KeyError: 'leiden'

        Returns
        -------
        Nothing.
        """
        try:
            for n in self.norm_data.keys():
                if n == what or n in what:
                    del self.norm_data[n]
                else:
                    for k in self.norm_data[n].keys():
                        if k == what or k in what:
                            self.norm_data[n][k] = {}
        except:
            pass
