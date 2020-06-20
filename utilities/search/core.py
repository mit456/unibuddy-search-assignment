"""
Search core module

Entry point to search service. Present requirement
is to build search on book summary. Maybe in future
we may need search on text of book pages
"""

from summary import SearchSummary


class Core:
    def __init__(self, *args, **kwargs):
        """
        Initialization of core search module
        """
        self.search_type = None
        self.response_count = None
        self.query = None
        self.queries = []

    def search(self, *args, **kwargs):
        """
        Responsible to invoke different search
        submodules. For e.g summary, titles etc
        """

        # Check kwargs found
        if not kwargs:
            print("Kwargs not found. returning empty!")
            return None

        # Check search_type found in kwargs
        # depending on search type we invoke different utilities
        if "search_type" not in kwargs:
            print("Kwargs found, but search type not found.")
            return None
        else:
            self.search_type = kwargs["search_type"]

        # Check response_count found in kwargs
        if "response_count" not in kwargs:
            print("Kwargs found, but response count not found.")
            return None
        else:
            self.response_count = kwargs["response_count"]

        # Check query and queries found in kwargs
        # and it can raise multiple conditions
        if "query" in kwargs and "queries" in kwargs:
            print("Found both query and queries, Please request for one")
            return None

        elif "queries" in kwargs and isinstance(kwargs["queries"],
                                                list) is False:
            print("queries need to be of type list")
            return None

        elif "query" in kwargs and isinstance(kwargs["query"], str) is False:
            print("query need to be of type string")
            return None

        elif "query" in kwargs:
            self.query = kwargs["query"]
            self.queries = None
        elif "queries" in kwargs:
            self.queries = kwargs["queries"]
            self.query = None

        if (self.search_type == "summary"):
            # Create new object of summary search
            summary_search = SearchSummary()
            summary_search_resp = summary_search.search(response_count=self.response_count,
                                                        query=self.query,
                                                        queries=self.queries)
            print("Resp: ", summary_search_resp)


if __name__ == "__main__":
    search_type = "summary"
    response_count = 3
    query = "is your problems"
    queries = ["is your problems",
               "achieve take book"]

    core_obj = Core()

    # Test call for query
    resp_search = core_obj.search(search_type=search_type,
                                  response_count=response_count,
                                  query=query)

    # Test call for array of queries
    # resp_search = core_obj.search(search_type=search_type,
    #                               response_count=response_count,
    #                               queries=queries)
