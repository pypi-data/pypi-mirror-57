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

        self.num_tasks = int(meta_info[self.name]["num tasks"])
        self.task_type = meta_info[self.name]["task type"]


    def _parse_and_check_input(self, input_dict):
        if self.task_type == "binary classification":
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

            if not y_true.ndim == 2:
                raise RuntimeError("y_true and y_pred mush to 2-dim arrray, {}-dim array given".format(y_true.ndim))

            if not y_true.shape[1] == self.num_tasks:
                raise RuntimeError("Number of tasks for {} should be {} but {} given".format(self.name, self.num_tasks, y_true.shape[1]))

            return y_true, y_pred

        else:
            raise ValueError("Undefined task type %s" (self.task_type))


    def eval(self, input_dict):
        """
            y_true: numpy ndarray of shape (num_data, num_tasks)
            y_pred: numpy ndarray of shape (num_data, num_tasks)

        """

        if self.task_type == "binary classification":
            y_true, y_pred = self._parse_and_check_input(input_dict)
            return self._eval_bincls(y_true, y_pred)
        else:
            raise ValueError("Undefined task type %s" (self.task_type))

    @property
    def expected_input_format(self):
        desc = "==== Expected input format of Evaluator for {}\n".format(self.name)
        if self.task_type == "binary classification":
            desc += "{\"y_true\": y_true, \"y_pred\": y_pred}\n"
            desc += "- y_true: numpy.ndarray of shape (num_node, num_task)\n"
            desc += "- y_pred: numpy ndarray of shape (num_node, num_task)\n"
            desc += "where num_task is {} and ".format(self.num_tasks)
            desc += "each row corresponds to one node.\n"
        else:
            raise ValueError("Undefined task type %s" (self.task_type))

        return desc

    @property
    def expected_output_format(self):
        desc = "==== Expected output format of Evaluator for {}\n".format(self.name)
        if self.task_type == "binary classification":
            desc += "{\"rocauc\": rocauc}\n"
            desc += "- rocauc (float): ROC-AUC score averaged across {} task(s)\n".format(self.num_tasks)
        else:
            raise ValueError("Undefined task type %s" (self.task_type))



        return desc

    def _eval_bincls(self, y_true, y_pred):
        """
            compute ROC-AUC and AP score averaged across tasks
        """
        
        rocauc_list = []
        ap_list = []

        for i in range(y_true.shape[1]):
            #AUC is only defined when there is at least one positive data.
            if np.sum(y_true[:,i] == 1) > 0 and np.sum(y_true[:,i] == 0) > 0:
                is_valid = y_true[:,i] == y_true[:,i]
                rocauc_list.append(roc_auc_score(y_true[is_valid,i], y_pred[is_valid,i]))

        if len(rocauc_list) == 0:
            raise RuntimeError("No positively labeled data available. Cannot compute ROC-AUC.")

        return {"rocauc": sum(rocauc_list)/len(rocauc_list)}

if __name__ == "__main__":
    ### binary classification case
    evaluator = Evaluator("ogbn-proteins")
    print(evaluator.expected_input_format)
    print(evaluator.expected_output_format)
    y_true = np.random.randint(2, size = (100,112))
    y_pred = np.random.randn(100,112)
    input_dict = {"y_true": y_true, "y_pred": y_pred}
    result = evaluator.eval(input_dict)
    print(result)



