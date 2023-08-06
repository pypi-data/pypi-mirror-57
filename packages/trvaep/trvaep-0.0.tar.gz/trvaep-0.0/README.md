# trVAE
## Introduction
A pytorch  implementation of trVAE (transfer Variational Autoencoder). trVAE is a deep generative model which learns mapping between multiple different styles (conditions). trVAE can be used for style transfer on images, predicting single-cell perturbations responses and batch removal.
## Getting Started

## Installation

### Installation with pip
To install the latest version from PyPI, simply use the following bash script:
```bash
pip install trvaep
```
or install the development version via pip: 
```bash
pip install git+https://github.com/theislab/trvaep.git
```

or you can first install flit and clone this repository:
```bash
pip install flit
git clone https://github.com/theislab/trvaep
cd trvaep
flit install
```

## Examples
* For perturbation prediction check this [example](https://nbviewer.jupyter.org/github/theislab/trvaep/blob/master/example/sample_notebook.ipynb)
 for interferon (IFN)-β stimulation from [Kang et al.](https://www.nature.com/articles/nbt.4042).

## Reproducing paper results:
In order to reproduce paper results visit [here](https://github.com/Naghipourfar/trVAE_reproducibility).
