"""
Search summary module


"""

from __future__ import division
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SearchSummary:
    def __init__(self):
        """
        Initialization of summary search module
        """

    def search(self, *args, **kwargs):
        """
        Search in summaries and return
        """
        const_datapath = os.path.join(BASE_DIR, "../../constants/data.json")

        query = kwargs["query"]
        queries = kwargs["queries"]
        response_count = kwargs["response_count"]

        with open(const_datapath) as fh:
            data = json.load(fh)

        if query is not None and queries is None:
            # Collect all summaries to return
            # in response
            summaries = []

            # Build summaries data
            # Apply encoding to ascii
            for i, a_summary in enumerate(data["summaries"]):
                # This is decoded summary after removing chars
                # not in range of 128
                d_summary = "".join([i if ord(i) < 128 else " "
                                     for i in a_summary["summary"]])
                d_summary_parts = d_summary.split(":")

                # Search logic: Match words from the query in
                # words of the summary
                words_summary = d_summary.split(" ")
                words_query = query.split(" ")

                # Intersection list and ranking
                # Find out intersection of words between words from query
                # and words from summary
                isection_list = list(set(words_summary) & set(words_query))
                if (len(isection_list) >= 1):
                    # Matching score
                    score = len(isection_list) / len(words_query)
                    # max_score = score
                    summary_meta = {
                        "id": a_summary["id"],
                        "summary": d_summary,
                        "score": score
                    }
                    summaries.append(summary_meta)


            # Sort the summaries and select top summaries
            # equal to the response count
            top_summaries = sorted(summaries,
                                      key=lambda k: k['score'],
                                      reverse=True)[:response_count]
            return top_summaries

        elif queries is not None and query is None:
            # Collect all summaries for all queries
            # to return
            summaries = []

            for i, query in enumerate(queries):
                # Select summaries for each queries
                # and store in q_selected_summaries
                q_selected_summaries = []
                for j, a_summary in enumerate(data["summaries"]):
                    # This is decoded summary after removing chars
                    # not in range of 128
                    d_summary = "".join([j if ord(j) < 128 else " " for j in a_summary["summary"]])
                    d_summary_parts = d_summary.split(":")

                    # Search logic: Match words from the query in
                    # words of the summary
                    words_summary = d_summary.split(" ")
                    words_query = query.split(" ")

                    # Intersection list and ranking
                    # Find out intersection of words between words from query
                    # and words from summary
                    isection_list = list(set(words_summary) & set(words_query))
                    if (len(isection_list) >= 1):
                        # Matching score
                        score = len(isection_list) / len(words_query)
                        # max_score = score
                        summary_meta = {
                            "id": a_summary["id"],
                            "summary": d_summary,
                            "score": score
                        }
                        q_selected_summaries.append(summary_meta)


                # Sort the summaries and select top summaries
                # equal to the response count
                q_top_summaries = sorted(q_selected_summaries,
                                         key=lambda k: k['score'],
                                         reverse=True)[:response_count]
                summaries.append(q_top_summaries)
            return summaries


if __name__ == "__main__":
    print("Main function of search summary")
