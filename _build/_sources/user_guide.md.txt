# User Guide

`gesund` is python package that enables you to connect with [Gesund.ai](https://gesund.ai/) and utilize majority of the features and capabilities that you as a developer could integrate in your customized workflows to design and execute validation your datasets and model.

`gesund` is a python package that explicitly enables you to design and execute your customized machine learning validation workflows with our validation tools.
It is a set of tools that allow developers and researchers to measure the performance of AI models using specific evaluation metrics. In healthcare, these libraries are essential for determining whether AI models can safely and accurately function in real-world clinical environments. Validation libraries ensure models are not only statistically sound but also clinically relevant, addressing key considerations like patient fairness, accuracy across different demographics, and performance in handling different medical conditions.

This user guide provides a comprehensive overview of `gesund`, including installation instructions, basic usage examples, advanced features, and customization options. Whether you're a beginner or an experienced developer, this guide will help you get started and make the most of our package.



## Installation

**A. Create virtual environment**

1. Create a virtual environment using any of the following choices

- [Conda](https://www.anaconda.com/download) 
- [Pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/)
- [PDM](https://pdm-project.org/en/latest/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Venv](https://docs.python.org/3/library/venv.html)


Activate the environment before the next step

2. Install the requirements from the requirements text file

*TBA*


**B. Install the library**


Installation could be done either using one of the following

1. Pip

```
pip install --upgrade gesund
```

2. Github

```
git clone https://github.com/gesund-ai/gesund.git
cd gesund
```



## Getting-Started


### Basic usage

```
# import the required libraries
from gesund.validation import run_metrics
import pprint

# provide the json files for respective values
args = {
    'annotations_json_path': '/path/to/annotations.json',
    'predictions': '/path/to/predictions.json',
    'class_mappings': '/path/to/class_mappings.json',
    'problem_type': 'object_detection',
    'format': 'json_format',
    'write_results_to_json': True
}

# execute the validation metrics
result = run_metrics(args)

# display the results; the results are in dictionary format
pprint.pprint(result)

```

The supported `format` values are `coco`, `yolo`, `gesund_custom_format`. This indicates that the json file is structured in the mentioned format.
Under the hood, other formats are converted to `gesund_custom_format` and are used. 

The result is comprised of 
- The `result` dictionary containing key-value pairs of validation metrics
- The resultant plots are stored in the local as `.png` files
- The `output` directory consisting of results stored as `.json` files. The results are only produced if `write_results_to_json: True`



## Examples

### Run Validation

**1. Classification** 

Inorder to the run classification specific validation metrics, set `problem_type: classification` in the args dictionary and provide the respective path.

```
# import the required libraries
from gesund.validation import run_metrics
import pprint

# provide the json files for respective values
args = {
    'annotations_json_path': '/path/to/annotations.json',
    'predictions': '/path/to/predictions.json',
    'class_mappings': '/path/to/class_mappings.json',
    'problem_type': 'classification',
    'format': 'json_format',
    'write_results_to_json': True
}

# execute the validation metrics
result = run_metrics(args)

# display the results; the results are in dictionary format
pprint.pprint(result)

```



**2. Segmentation**


Inorder to the run segmentation specific validation metrics, set `problem_type: segmentation` in the args dictionary and provide the respective path.

```
# import the required libraries
from gesund.validation import run_metrics
import pprint

# provide the json files for respective values
args = {
    'annotations_json_path': '/path/to/annotations.json',
    'predictions': '/path/to/predictions.json',
    'class_mappings': '/path/to/class_mappings.json',
    'problem_type': 'segmentation',
    'format': 'json_format',
    'write_results_to_json': True
}

# execute the validation metrics
result = run_metrics(args)

# display the results; the results are in dictionary format
pprint.pprint(result)

```

**3. Object Detection**

Inorder to the run object detection specific validation metrics, set `problem_type: object_detection` in the args dictionary and provide the respective path.

```
# import the required libraries
from gesund.validation import run_metrics
import pprint

# provide the json files for respective values
args = {
    'annotations_json_path': '/path/to/annotations.json',
    'predictions': '/path/to/predictions.json',
    'class_mappings': '/path/to/class_mappings.json',
    'problem_type': 'object_detection',
    'format': 'json_format',
    'write_results_to_json': True
}

# execute the validation metrics
result = run_metrics(args)

# display the results; the results are in dictionary format
pprint.pprint(result)

```


### Sub Cohort Analysis

*TBA*
