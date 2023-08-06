# Open Graph Benchmark (OGB)

A collection of benchmark datasets, data-loaders and evaluators for graph machine learning in [PyTorch](https://pytorch.org/). Data loaders are fully compatible with [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/) and [Deep Graph Library (DGL)](https://www.dgl.ai/).
The goal is to have an easily-accessible standardized large-scale benchmark datasets to drive research in graph machine learning.


### Datasets available
Benchmark datasets are broadly classified into three categories. Datasets that are currently available are also listed (more to come soon).
- [**Node property prediction**](ogb/nodeproppred/README.md) : Prediction on single nodes.
    - Prediction of protein functionality in a protein-protein association network.

- [**Link property prediction**](ogb/linkproppred/README.md) : Prediction on pairs of nodes.
    - Prediction of protein-protein association and type in a protein-protein association network.

- [**Graph property prediction**](ogb/graphproppred/README.md) : Prediction on an entire graph/subgraph.
    - Prediction of chemical properties of molecules (12 kinds of datasets available).

### Installation
You can install OGB using Python's package manager pip. To avoid any conflict with your existing Python setup, it is suggested to work in a virtual environment with [`virtualenv`](https://docs.python-guide.org/dev/virtualenvs/). To install `virtualenv`:

```bash
pip install --upgrade virtualenv
virtualenv venv
source venv/bin/activate
```

#### Requirements
 - Python 3.7
 - PyTorch>=1.2
 - DGL>=0.4.1 or torch-geometric>=1.3.1
 - Numpy>=1.16.0
 - pandas>=0.24.0
 - urllib3>=1.24.0
 - scikit-learn>=0.20.0

#### Pip install
The recommended way to install OGB is using Python's package manager pip:
```bash
pip install ogb
```

#### From source
You can also install OGB from source. This is recommended if you want to contribute to OGB.
```bash
git clone https://github.com/snap-stanford/ogb
cd ogb
python setup.py install
```

## Example
We highlight two key features of OGB, namely, (1) easy-to-use data loaders, and (2) standardized evaluators.
#### (1) Data loaders
We prepare easy-to-use PyTorch Geometric and DGL data loaders. We handle dataset downloading as well as standardized dataset splitting.
Below, on PyTorch Geometric, we see that a few lines of code is sufficient to prepare and split the dataset! Needless to say, you can enjoy the same convenience for DGL!
```python
from ogb.graphproppred.dataset_pyg import PygGraphPropPredDataset
from torch_geometric.data import DataLoader

dataset = PygGraphPropPredDataset(name = "ogbg-mol-tox21") 
splitted_idx = dataset.get_idx_split() 

train_loader = DataLoader(dataset[splitted_idx["train"]], batch_size=32, shuffle=True)
valid_loader = DataLoader(dataset[splitted_idx["valid"]], batch_size=32, shuffle=False)
test_loader = DataLoader(dataset[splitted_idx["test"]], batch_size=32, shuffle=False)
```

#### (2) Evaluators
We also prepare standardized evaluators for easy evaluation and comparison of different methods. The evaluator takes `input_dict` (a dictionary whose format is specified in `evaluator.expected_input_format`) as input, and returns a dictionary storing the performance metric appropriate for the given dataset.
The standardized evaluation protocol allows researchers to reliably compare their methods.
```python
from ogb.graphproppred import Evaluator

evaluator = Evaluator(name = "ogbg-mol-tox21")
# We can learn the input and output format specification of the evaluator as follows.
# print(evaluator.expected_input_format) 
# print(evaluator.expected_output_format) 
input_dict = {"y_true": y_true, "y_pred": y_pred}
result_dict = evaluator.eval(input_dict) # E.g., {"ap": 0.3421, "rocauc": 0.7321}
```

## Citing OGB
Coming soon.
