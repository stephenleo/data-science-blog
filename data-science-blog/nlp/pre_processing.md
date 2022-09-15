
# Text Pre-Processing

-   Textual data, especially those scrapped from the internet, can be
    incredibly messy with tons of inconsistencies
-   Text pre-processing techniques aim to clean up the text data and
    prepare it for Machine Learning

## ftfy: fixes text for you

One of the most frustrating parts about working with tons of text in the
real world is identifying and fixing “noise” in the text such as this

🙅 Noisy text: `"The Mona Lisa doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have eyebrows."`

🙆 Actual text: `"The Mona Lisa doesn't have eyebrows."`

👉 Enter “ftfy”, a nifty little python library by [Elia
Lake](https://www.linkedin.com/in/elia-lake-13277335/) that fixes
Unicode text that’s broken in various ways. Take a look at the image
below for some examples!

-   [x] Fix multiple layers of mojibake (encoding mix-ups) including
    “curly quotes”, by detecting patterns of characters that were
    clearly meant to be UTF-8 but were decoded as something else.
-   [x] Decode HTML entities that appear outside of HTML
-   [x] Strongly avoids false positives (should never change a
    correctly-decoded text to something else)

🌟 Github: <https://github.com/rspeer/python-ftfy>

<div style="overflow:hidden;margin-left:auto;margin-right:auto;border-radius:10px;width:100%;max-width:740px;position:relative"><div style="width:100%;padding-bottom:64.86486486486486%"></div><iframe width="740" height="480" title="Code snippet - ftfy" src="https://snappify.io/embed/d4d6d9bc-9431-49f5-b15c-7fd656eb27b3?responsive" allow="clipboard-write" style="background:linear-gradient(337deg, #654ea3, #da98b4);position:absolute;left:0;top:0;width:100%" frameborder="0"></iframe></div>
