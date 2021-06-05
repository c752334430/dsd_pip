# dsd_pip

This package contains three algorithms that solve dense subgraph problem exactly or approximately, including Goldberg's max flow based algorithm [1], charikar's greedy peeling algorithm [2], and state-of-the-art flowless (greedy++) algorithm [3].

We also leverage all algorithms to find k-clique dense subgraph, given list of k-cliques in a certain graph. Remind this can be done with algorithms like KClist [5].
We follow [4] when contructing clique based max flow graph.

To install the package, run

    pip install dsd

Check https://github.com/tsourolampis/dense-subgraph-discovery/blob/main/code/dsd_package/tests/simple_test.py to see how to use the package.

[1] A. V. Goldberg. Finding a maximum density subgraph. University of California Berkeley, CA, 1984.

[2] M. Charikar. Greedy approximation algorithms for finding dense components in a graph. In
International Workshop on Approximation Algorithms for Combinatorial Optimization, pages
84–95. Springer, 2000

[3] Boob D., Gao Y., Peng R., Sawlani S., Tsourakakis C.~E., Wang D., Wang J., Flowless: Extracting Densest Subgraphs Without Flow Computations, <i>arXiv e-prints</i>, 2019.

[4] Shuguang Hu, Xiaowei Wu, and T-H. Hubert Chan. 2017. Maintaining Densest Subsets Efficiently in Evolving Hypergraphs. Proceedings of the 2017 ACM on Conference on Information and Knowledge Management. Association for Computing Machinery, New York, NY, USA, 929–938. DOI:https://doi.org/10.1145/3132847.3132907

[5] Maximilien Danisch, Oana Balalau, and Mauro Sozio. 2018. Listing k-cliques in Sparse Real-World Graphs*. In Proceedings of the 2018 World Wide Web Conference (WWW '18). International World Wide Web Conferences Steering Committee, Republic and Canton of Geneva, CHE, 589–598. DOI:https://doi.org/10.1145/3178876.3186125
