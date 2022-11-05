# CSC591GraphP2
> This project implementation is done towards fullfillment of Project 2 of CSC 591 Graph Data Mining

## Reaserch Paper
The paper implemented is given under `research_paper` folder. The paper is [Efficient Identification of Overlapping
Communities](https://www.researchgate.net/publication/221246973_Efficient_Identification_of_Overlapping_Communities)

## Goal
To implement the given community detection algorithm for realworld graphs. Objective is stated [here](https://github.com/tusharkini/CSC591GraphP2/blob/main/objective/P1CommunityDetection.pdf). To do that, your team will need to:
- Implement the algorithm assigned to your team with an “obsession” with the highest
performance possible.
- Provide a detailed analysis of the performance of your algorithm/implementation.  


---
## Data  

Realworld graph datasets with groundtruth communities:

- Amazon.
- DBLP.
- YouTube.  

For each type of different sizes with ground truth communities: a small graph (≈2,500 nodes), a medium
graph (≈5,000 nodes), a large graph (<100,000 nodes), and the original graph (>300,000 nodes). Please note that you do not have to run experiments using graphs of all sizes.
Selecting one size for each type of graph is enough. Make sure you specify on your
report which size you used for each graph.

---


## Getting Started

### Installation

- Install Python3 from [here](https://www.python.org/downloads/) and finish the required setup in the executable file.
- Install pip package manager fo rfuture downloads-
    ```bash
    $ python -m ensurepip --upgrade
    ```
- Upgrade the version of pip-
    ```
    $ python -m pip install --upgrade pip
    ```
- Install NetworkX for graph processing-
    ```bash
    $ pip install networkx
    ```
- Upgrade the version of pip-
    ```
    $ pip install --upgrade networkx
    ```
- Install decorator-
    ```bash
    $ pip install decorator
    ```

- Create working directory named `Community_detection_P2` and go inside it
    ```bash
    $ mkdir Community_detection_P2
    $ cd Community_detection_P2
    ```
- Clone this repository from [here](https://github.com/tusharkini/CSC591GraphP2) or use the following in GitBash
    ```bash
    $ git clone https://github.com/tusharkini/CSC591GraphP2
    ```
### Running the Algorithm Code
- Run the algorithm code using- 
    ```bash
    $ cd code
    $ python main.py <path_to_graph_file> <prefix_to_output_file>

    ```
    For example to run algorithm on `dblp.graph.small` use the following code-
    ```bash
    $ python main.py ../datasets/dblp/dblp.graph.small dblp_small

    ```
    This will create an output file named `results/dblp_small_output.txt`
### Running the Metrics Code
- Run th emetrcis code using-
    ```bash
    $ cd results
    $ python ../metrics_code/metrics.py <path_to_graph_file> <path_to_ground_truth_file> <path_to_output_file> <prefix_to_output_file>
    ```
    For example to run metrics code for graph `dblp.graph.small` use the following code-
    ```bash
    $ cd results
    $ $ python ../metrics_code/metrics.py ../datasets/dblp/dblp.graph.small ../datasets/dblp/dblp.comm.small ../results/dblp_small_output.txt  dblp_small

    ```
    This will create output files named `results/dblp_small.pmetrics.csv` and `results/dblp.small.pmetrics.csv`


---


## Authors

- Tushar Kini [Github](https://github.com/tusharkini)

---

## Technical Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


-----