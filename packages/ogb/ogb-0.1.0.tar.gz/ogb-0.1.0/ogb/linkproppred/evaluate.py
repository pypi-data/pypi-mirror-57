from sklearn.metrics import roc_auc_score
import torch.nn as nn
import pandas as pd
import os
import numpy as np

### Evaluator for graph classification
class Evaluator:
    def __init__(self, name):
        self.name = name

        meta_info = pd.read_csv(os.path.join(os.path.dirname(__file__), "master.csv"), index_col = 0)
        if not self.name in meta_info:
            print(self.name)
            error_mssg = "Invalid dataset name {}.\n".format(self.name)
            error_mssg += "Available datasets are as follows:\n"
            error_mssg += "\n".join(meta_info.keys())
            raise ValueError(error_mssg)

        self.task_type = meta_info[self.name]["task type"]


    def _parse_and_check_input(self, input_dict):
        if self.task_type == "link prediction":
            if not "y_true" in input_dict:
                RuntimeError("Missing key of y_true")
            if not "y_pred" in input_dict:
                RuntimeError("Missing key of y_pred")

            y_true, y_pred = input_dict["y_true"], input_dict["y_pred"]

            """
                y_true: numpy ndarray of shape (num_node, num_tasks)
                y_pred: numpy ndarray of shape (num_node, num_tasks)
            """
            ## check type
            if not (isinstance(y_true, np.ndarray) and isinstance(y_true, np.ndarray)):
                raise RuntimeError("Arguments to Evaluator need to be numpy ndarray")

            if not y_true.shape == y_pred.shape:
                raise RuntimeError("Shape of y_true and y_pred must be the same")

            if not y_true.ndim == 1:
                raise RuntimeError("y_true and y_pred mush to 1-dim arrray, {}-dim array given".format(y_true.ndim))

            return y_true, y_pred

        else:
            raise ValueError("Undefined task type %s" (self.task_type))


    def eval(self, input_dict):
        """
            y_true: numpy ndarray of shape (num_data, num_tasks)
            y_pred: numpy ndarray of shape (num_data, num_tasks)

        """

        if self.task_type == "link prediction":
            y_true, y_pred = self._parse_and_check_input(input_dict)
            return self._eval_linkpred(y_true, y_pred)
        else:
            raise ValueError("Undefined task type %s" (self.task_type))

    @property
    def expected_input_format(self):
        desc = "==== Expected input format of Evaluator for {}\n".format(self.name)
        if self.task_type == "link prediction":
            desc += "{\"y_true\": y_true, \"y_pred\": y_pred}\n"
            desc += "- y_true: numpy.darray of shape (num_edge, )\n"
            desc += "- y_pred: numpy darray of shape (num_edge, )\n"
            desc += "each row corresponds to one edge.\n"
            desc += "y_true is either 0 or 1, indicating whether edges are present or not.\n"
            desc += "y_true should be valid_edge_label or test_edge_label.\n"
        else:
            raise ValueError("Undefined task type %s" (self.task_type))

        return desc

    @property
    def expected_output_format(self):
        desc = "==== Expected output format of Evaluator for {}\n".format(self.name)
        if self.task_type == "link prediction":
            desc += "{\"rocauc\": rocauc}\n"
            desc += "- rocauc (float): ROC-AUC score\n"
        else:
            raise ValueError("Undefined task type %s" (self.task_type))



        return desc

    def _eval_linkpred(self, y_true, y_pred):
        """
            compute ROC-AUC and AP score averaged across tasks
        """
        
        rocauc = []

        if np.sum(y_true == 1) > 0 and np.sum(y_true == 0) > 0:
            rocauc = roc_auc_score(y_true, y_pred)

        else:
            raise RuntimeError("No positively labeled link available. Cannot compute ROC-AUC.")

        return {"rocauc": rocauc}


if __name__ == "__main__":
    ### link prediction case
    evaluator = Evaluator(name = "ogbl-ppa")
    print(evaluator.expected_input_format)
    print(evaluator.expected_output_format)
    y_true = np.random.randint(2, size = (100,))
    y_pred = np.random.randn(100,)
    input_dict = {"y_true": y_true, "y_pred": y_pred}
    result = evaluator.eval(input_dict)
    print(result)

