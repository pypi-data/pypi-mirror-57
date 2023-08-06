# -*- coding: utf-8 -*-

"""
Defines utilities pertaining to (local) read / write operations
"""

__all__ = ["FileReader", "TemporaryDirectory", 
           "zip_folder_to_archive", "unzip_archive_to_folder", 
           "rm_folder_content", "mv_folder_content",
           "convert_to_svmlight_like_file_format_line", 
           "persist_to_svmlight_like_file", 
           "decode_svmlight_like_file_format_line_vector_data", 
           "decode_svmlight_like_file_format_line_to_sparse_vector", 
           "decode_svmlight_like_file_format_line_to_dense_vector", 
           "load_from_svmlight_like_file", 
           ]

import os
import shutil
import tempfile
import zipfile
import numpy
from scipy import sparse


class FileReader(object):
    """ Class used to provide an iterator over the lines of a file identified by its file path.
    
    Once this class has been created, it can be used to create as many iterator over the file as 
    necessary.
    
    Arguments:
        file_path: string, path to the file to read
        
        encoding: string, to specify which encoding to use to read the file
    
    Attributes:
        file_path: string, path to the file to read
        
        encoding: string, to specify which encoding to use to read the file
        
        line_nb: int, number of lines that has been read from the file up until now
    """
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding
        self.line_nb = 0
    
    def __iter__(self):
        """ Creates a generator over the lines of the file.
        
        Yields:
            string, a line of the file
        """
        with open(self.file_path, "r", encoding=self.encoding) as f:
            for line_nb, line in enumerate(f, 1):
                self.line_nb = line_nb
                yield line


class TemporaryDirectory(object):
    """ Class used to create a local temporary directory in combination with a use as a context manager.
    
    The actual temporary directory is created when entering the contextualized code part, and may 
    be destroyed (default behavior) when exiting the contextualized code part.
    Behind the scene, it is the 'mkdtemp' function of the 'tempfile' library that is used.
    
    Arguments:
        temporary_root_folder_path: string, or None; path to an existing local folder that will be 
            used as the root folder, where the temporary directories shall be created.
        
        suffix: string; if not the empty string, will be appended to the name of created temporary 
            directories
        
        delete_upon_exit: boolean; if True (default), the temporary directory will be destroyed 
            when exiting the contextualized code part. If False, it will not, and it will be up to the 
            user to dispose of it if necessary.
    
    Attributes:
        temporary_root_folder_path: string; input value used to instantiate this class
        
        suffix: string; input value used to instantiate this class
        
        delete_upon_exit: boolean; input value used to instantiate this class
        
        temporary_folder_path: string; path to the created temporary directory
    """
    def __init__(self, temporary_root_folder_path=None, suffix="", delete_upon_exit=True):
        self.temporary_root_folder_path = temporary_root_folder_path
        self.suffix = suffix
        self.delete_upon_exit = delete_upon_exit
        self.temporary_folder_path = None
    
    def __enter__(self):
        # We remove the temporary folder
        self.temporary_folder_path = tempfile.mkdtemp(suffix=self.suffix, dir=self.temporary_root_folder_path)
        return self
    
    def __exit__(self, *args):
        # We remove the temporary folder if asked to
        if self.delete_upon_exit:
            if os.path.isdir(self.temporary_folder_path):
                shutil.rmtree(self.temporary_folder_path)


# Process '.zip' archive files
def zip_folder_to_archive(folder_path, archive_file_path):
    """ Creates a '.zip' archive file from the content of a folder specified by its path.
    
    Args:
        folder_path: string, path to the folder whose content shall be turned into a '.zip' archive
        archive_file_path: string, path to the archive file to be created. If it dos not end with 
            '.zip', then '.zip' will be appended to it.

    Returns:
        string, the path to the created archive file that has been effectively used
    """
    if not archive_file_path.endswith(".zip"):
        archive_file_path = archive_file_path + ".zip"
    # Check that we can write in destination folder
    with zipfile.ZipFile(archive_file_path, "w", zipfile.ZIP_STORED) as ziph:
        # Write file in archive
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for name in sorted(dirnames):
                path = os.path.join(dirpath, name)
                arcname = os.path.relpath(path, folder_path)
                ziph.write(path, arcname)
            for name in filenames:
                path = os.path.join(dirpath, name)
                arcname = os.path.relpath(path, folder_path)
                if os.path.isfile(path):
                    ziph.write(path, arcname)
    return archive_file_path

def unzip_archive_to_folder(archive_file_path, folder_path):
    """ Extracts the content of an archive file into a specified folder.
    
    Args:
        archive_file_path: string, path to the archive whose content is to be extracted
        folder_path: string, path to folder into which the extracted content will be placed
    """
    with zipfile.ZipFile(archive_file_path, "r", zipfile.ZIP_STORED) as ziph:
        ziph.extractall(path=folder_path)



# Carry out operations on local folders
def rm_folder_content(folder_path):
    """ Removes the entire content of the folder specified by its path.
    
    Args:
        folder_path: string, path to the local folder whose content is to be removed
    """
    for name in os.listdir(folder_path):
        path = os.path.join(folder_path, name)
        if os.path.isfile(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

def mv_folder_content(src_folder_path, dst_folder_path):
    """ Moves the content of a source folder into a destination folder.
    
    Args:
        src_folder_path: path to the local folder to mv
        dst_folder_path: path to the location where to folder should be moved
    """
    if not os.path.isdir(dst_folder_path):
        msg = "Destination folder path '{}' does not refer to an existing folder."
        msg = msg.format(dst_folder_path)
        raise ValueError(msg)
    for _, dirnames, filenames in os.walk(src_folder_path, topdown=True, followlinks=False): #dirpath
        # Files
        for file_name in filenames:
            src_path = os.path.join(src_folder_path, file_name)
            dst_path = os.path.join(dst_folder_path, file_name)
            shutil.move(src_path, dst_path)
        # Folders
        for folder_name in dirnames:
            src_path = os.path.join(src_folder_path, folder_name)
            dst_path = os.path.join(dst_folder_path, folder_name)
            shutil.move(src_path, dst_path)



# Persist and load from svmlight-like formatted files
def convert_to_svmlight_like_file_format_line(vector, label):
    """ Returns a string representing a sample using a format derived from the 'SVMLight' sparse data 
    file format, dubbed "'svmlight'-like".
    
    A line is written this way::
    
        'label_value' 'column_nb' 'sparse vector description'
    
    Args:
        vector: numpy array, or scipy.sparse.SparseMatrix, of shape (1,N)
        label: label value of thr sample (for instance, class label if in the frame of 
            a classification machine learning problem)

    Returns:
        the svmlight-like string representation of the sample
    
    Examples::
        
        >>> convert_to_svmlight_like_file_format_line(numpy.array([[2, 0, 0, -9, 0, 45.63]]), 1)
        '1 6 0:2 3:-9 5:45.63'
        >>> convert_to_svmlight_like_file_format_line(scipy.sparse.csr_matrix([[1, 0, 0, -5, 0, 12.65, 0, 0, 42]]), 0)
        '0 9 0:1 3:-5 5:12.65 8:42' 
    """
    features_string = " ".join("{}:{}".format(col_id+1, vector[0,col_id]) for col_id in vector.nonzero()[1])
    column_nb = vector.shape[1]
    return "{} {} {}".format(label, column_nb, features_string)

def persist_to_svmlight_like_file(file_path, vector_label_pairs_iterable):
    """ Persists data present in an iterable of (vector; label) pairs into a svmlight-like formatted 
    file.
    
    Args:
        file_path: string, path to the file to be created
        vector_label_pairs_iterable: iterable over (vector; label) pairs
    """
    with open(file_path, "w", encoding="utf-8") as f:
        vectors_file_content = "\n".join(convert_to_svmlight_like_file_format_line(vector, label)\
                                         for vector, label in vector_label_pairs_iterable)
        f.write(vectors_file_content)

def decode_svmlight_like_file_format_line_vector_data(line):
    """ Converts a svmlight-like formatted line into a (label_value; column_nb; column_index_data_value_pairs)
    tuple.
    
    Args:
        line: string

    Returns:
        the corresponding (label_value; column_nb; column_index_data_value_pairs) tuple
    
    Examples::
    
        >>> decode_svmlight_like_file_format_line_vector_data("'1 6 0:2 3:-9 5:45.63')
        ("1", 6, ((0,2.), (3,-9.) (5,45.63)))
    """
    label, column_nb, string_vector = line.split(sep=" ", maxsplit=2)
    column_index_data_value_pairs = tuple((int(column_index_str), float(value_str))\
                                          for column_index_str, value_str in string_vector.split(" ")
                                          )
    return label, column_nb, column_index_data_value_pairs
    
def decode_svmlight_like_file_format_line_to_sparse_vector(line):
    """ Converts a svmlight-like formatted line back into a (label_value, one row sparse matrix) pair.
    
    Args:
        line: string

    Returns:
        the corresponding (label_value; one row sparse matrix) tuple
    
    Examples::
    
        >>> label, vector = decode_svmlight_like_file_format_line_vector_data("'1 6 0:2 3:-9 5:45.63')
        >>> label
        "1"
        >>> vector.A
        [[2.,  0.,  0.,  -9.,   0.,  45.63]]
    """
    label, column_nb, column_index_data_value_pairs = decode_svmlight_like_file_format_line_vector_data(line)
    vector = sparse.lil_matrix(shape=(1, column_nb), dtype=numpy.float)
    column_indices, data_values = tuple(zip(*column_index_data_value_pairs))
    vector[0,column_indices] = data_values
    vector = vector.csr_matrix()
    return label, vector

def decode_svmlight_like_file_format_line_to_dense_vector(line):
    """ Converts a svmlight-like formatted line back into a (label_value, (1,N)-shaped numpy array) 
    pairs.
    
    Args:
        line: string

    Returns:
        the corresponding (label_value; (1,N)-shaped numpy array) tuple
    
    Examples::
    
        >>> label, vector = decode_svmlight_like_file_format_line_vector_data("'1 6 0:2 3:-9 5:45.63')
        >>> label
        "1"
        >>> vector
        [[2.,  0.,  0.,  -9.,   0.,  45.63]]
    """
    label, column_nb, column_index_data_value_pairs = decode_svmlight_like_file_format_line_vector_data(line)
    vector = numpy.zeros(shape=(1, column_nb), dtype=numpy.float)
    column_indices, data_values = tuple(zip(*column_index_data_value_pairs))
    vector[0,column_indices] = data_values
    return label, vector

def load_from_svmlight_like_file(file_path, sparse=True):
    """ Creates a generator over the (label value; vector) pairs encoded in a 'svmlight'-like 
    formatted file.
    
    Args:
        file_path: string, path to 'svmlight'-like formatted file
        sparse: boolean; if True, yield vectors as one row sparse matrices; else yields vectors as 
            (1,Ni) numpy-arrays

    Yields:
        (label value; vector) pair
    """
    decode_svmlight_format_file_line_fct = decode_svmlight_like_file_format_line_to_sparse_vector
    if not sparse:
        decode_svmlight_format_file_line_fct = decode_svmlight_like_file_format_line_to_dense_vector
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield decode_svmlight_format_file_line_fct(line)
