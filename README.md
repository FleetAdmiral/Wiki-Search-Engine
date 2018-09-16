# Wiki-Search-Engine
Creating a search engine for Wikipedia (the entire 50GB+ datadump!)
Basic Stages (in order):
● XML parsing
● Tokenization
● Case folding
● Stop words removal
● Stemming
● Posting List / Inverted Index Creation
● Optimize
● Ranking (tf-idf/vector space/probabilistic)

Challenges tackled:
● multi-level indexing (retrieval speed)
● efficient use of data-structures, algorithms (indexing speed, memory)
● threading for long / multi-field queries (retrieval speed)
● index compression (index size reduction)
● arbitrary / long / multi-field queries (early search termination)
● efficient code debugging (it might take ~10 hours to index full dump)


Features:
● Support for Field Queries. Fields include Title, Infobox, Body, Category, Links, and
References of a Wikipedia page. This helps when a user is interested in searching for
the movie ‘Up’ where he would like to see the page containing the word ‘Up’ in the title
and the word ‘Pixar’ in the Infobox. You can store field type along with the word when
you index.
● Index size should be less than 1⁄4 of dump size. [You can experiment with different index
compressing techniques.]
● Scalable index construction

Sample Queries:
● he who must not be named
● t: the two towers i: 1954
● jon snow
● t: sachin b: e-commerce
