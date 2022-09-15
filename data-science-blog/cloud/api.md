
# Application Programming Interface (API)

## JSON Lines

The JSON format is one of the most popular ways of transmitting
information over any network. Why is this important for a Data
Scientist?

-   When you deploy a model as an endpoint, you will probably send and
    receive data from the deployed model in JSON format.

There are many ways to construct a JSON string. The best way, in my
opinion, is to use the JSON lines format.

-   Directly convert to and from Pandas dataframes!
-   One line is one row of data. No ambiguity about how to split rows!
-   Very readable where each key is the column name, and each value is
    the value of the row in that column. No ambiguity about which value
    belongs to which feature!
-   Easy to parallelize (e.g., using Sagemaker Batch Transform) since we
    can send each line to a different machine for inference.

While deploying ML models (e.g., in Sagemaker), you need to handle
converting to and from the JSON object. So keeping your deployment
consistent with JSON lines format will make your life much easier and
unambiguous.

<div style="overflow:hidden;margin-left:auto;margin-right:auto;border-radius:10px;width:100%;max-width:740px;position:relative"><div style="width:100%;padding-bottom:77.70270270270271%"></div><iframe width="740" height="575" title="Code snippet - json_lines" src="https://snappify.io/embed/6f162780-cc5c-4ea5-bad8-9a183b12a2d6?responsive" allow="clipboard-write" style="background:linear-gradient(354deg,  #FF75B5, #FFB86C);position:absolute;left:0;top:0;width:100%" frameborder="0"></iframe></div>
