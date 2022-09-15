
# Clustering

Unsupervised grouping of related items

## KModes: Clustering of Categorical Data

KModes: Clustering of Categorical Data WITHOUT One-Hot encoding!

-   KMeans clustering using Euclidean distance to find clusters so you
    need to one-hot encode all categorical data
-   In KModes clustering, you can directly cluster categorical data
    without one-hot encoding!
-   KModes uses the number of dissimilar values between two categorical
    vectors as a distance metric to assign each data point to its
    nearest cluster at each clustering step.
-   Mode is the most observed value for each column in the cluster
-   Implement in one line of code!
-   It also supports the K-Prototypes algorithm for combining k-modes
    and k-means on mixed categorical + numerical data.

<!-- -->

    pip install kmodes

🌟 Github: <https://github.com/nicodv/kmodes>

<div style="overflow:hidden;margin-left:auto;margin-right:auto;border-radius:10px;width:100%;max-width:740px;position:relative"><div style="width:100%;padding-bottom:64.86486486486486%"></div><iframe width="740" height="480" title="Code snippet - kmodes" src="https://snappify.io/embed/c9b463e2-e263-4d94-a5f5-da9c4694a148?responsive" allow="clipboard-write" style="background:linear-gradient(337deg, #654ea3, #da98b4);position:absolute;left:0;top:0;width:100%" frameborder="0"></iframe></div>
