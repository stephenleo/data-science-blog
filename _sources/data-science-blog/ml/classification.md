
# Classification

## Multi-label Classification Stratified Split

Iterative Stratification: Easily stratify the train test split for
multi-label classification problems

-   In machine learning classification problems, when your input data
    has imbalanced classes, it’s necessary to stratify the train-test
    split so that we maintain the proportion of the minority class in
    both the train and test splits.
-   Unfortunately, sklearn’s train\_test\_split only allows stratified
    splits for single-label classification and does not support multiple
    labels.

Enter iterative-stratification:

-   Stratify the train test split across multiple labels concurrently
-   With K-Fold cross-validation!
-   Compatible with sklearn

<!-- -->

    pip install iterative-stratification

🌟 Github: <https://github.com/trent-b/iterative-stratification>

<div style="overflow:hidden;margin-left:auto;margin-right:auto;border-radius:10px;width:100%;max-width:740px;position:relative"><div style="width:100%;padding-bottom:65.27027027027027%"></div><iframe width="740" height="483" title="Code snippet - iterative-stratification" src="https://snappify.io/embed/a6dde5ec-806e-40c7-9125-d540ff350738?responsive" allow="clipboard-write" style="background:linear-gradient(337deg, #654ea3, #da98b4);position:absolute;left:0;top:0;width:100%" frameborder="0"></iframe></div>

## Efficient Metrics Calculation

Typically when you want to calculate multiple metrics for a machine
learning model, you’d import and run them one by one.

Instead, you can refactor your code to calculate multiple metrics with a
single `#!python get_scorer()` method, as shown in the image.

You could move metrics\_list to a config.yml so that we can change the
metrics calculated without changing any code!

<div style="overflow:hidden;margin-left:auto;margin-right:auto;border-radius:10px;width:100%;max-width:740px;position:relative"><div style="width:100%;padding-bottom:77.70270270270271%"></div><iframe width="740" height="575" title="Code snippet - get_scorer" src="https://snappify.io/embed/f377977b-6c54-4ab1-b7a1-94daa7766ca5?responsive" allow="clipboard-write" style="background:linear-gradient(337deg, #654ea3, #da98b4);position:absolute;left:0;top:0;width:100%" frameborder="0"></iframe></div>
