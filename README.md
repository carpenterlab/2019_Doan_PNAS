# 2019_DeepLearning_RBC
This is a vignette to perform supvervised classification and weakly supervised regression for Label-free assessment of red blood cell storage lesions, as well as a comparative analysis using conventional image processing (CellProfiler)


# Installation

Core requirement: [CellProfiler](http://cellprofiler.org) 3.1.8+, Python, Tensorflow, Scikit-learn and umap-learn libraries

1. Install [Python](https://www.python.org/downloads/) (>=3.6) and pip. Follow the instruction [here](https://packaging.python.org/tutorials/installing-packages/)

1. In Terminal (UNIX) or cmd (Windows), type :
    ``` r
    pip3 install --upgrade pip
    ```
    In OSX/Linux you may have to use "sudo", e.g: 
    ``` r
    sudo pip3 install --upgrade pip
    ```

1. If success, continue to run the following commands, one line at a time:
    ``` r
    pip3 install numpy
    pip3 install scipy
    pip3 install sklearn
    pip3 install pandas
    pip3 install matplotlib
    pip3 install jupyter
    pip3 install umap-learn
    pip3 install tensorflow
    ```
    
    **Note:** 
    
    Windows user can also use [Anaconda](https://www.anaconda.com/)

1. Once done, test if you can use jupyter notebook. In Terminal or cmd, type:
    ``` r
    jupyter notebook
    ```
    If it opens an interface in your default web-browser, you’re ready!

    If you have issues running jupyter, please visit [Jupyter website](https://jupyter.readthedocs.io/en/latest/install.html)
    
# Use

Use the provided Jupyter notebooks following the step-wise naming order.
