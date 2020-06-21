"""
Search summary module

Method help is searching in three sentence
summaries of book
"""

from __future__ import division
import json
import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "../../constants/config.json")


class SearchSummary:
    def __init__(self):
        """
        Initialization of summary search module
        """

        with open(CONFIG_PATH) as cf:
            self.config = json.load(cf)

    def search(self, *args, **kwargs):
        """
        Search in summaries and return
        """
        const_datapath = os.path.join(BASE_DIR, "../../constants/data.json")

        query = kwargs["query"]
        queries = kwargs["queries"]
        response_count = kwargs["response_count"]

        # Load dataset
        with open(const_datapath) as fh:
            data = json.load(fh)

        # Whether request was made with query
        # or queries
        if query is not None and queries is None:
            query = query.strip()
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
                        "summary": d_summary,
                        "id": a_summary["id"],
                        "query": query,
                        "score": score
                    }
                    summaries.append(summary_meta)

            # Sort the summaries and select top summaries
            # equal to the response count
            top_summaries = sorted(summaries,
                                   key=lambda k: k['score'],
                                   reverse=True)[:response_count]
            for k, a_top_summary in enumerate(top_summaries):
                del a_top_summary["score"]

                # Get author name corresponding to book_id
                resp_author_ms = self.get_author_name(a_top_summary["id"])
                a_top_summary["author"] = resp_author_ms

            return top_summaries

        elif queries is not None and query is None:
            # Collect all summaries for all queries
            # to return
            summaries = []

            for i, query in enumerate(queries):
                query = query.strip()
                # Select summaries for each queries
                # and store in q_selected_summaries
                q_selected_summaries = []
                for j, a_summary in enumerate(data["summaries"]):
                    # This is decoded summary after removing chars
                    # not in range of 128
                    d_summary = "".join([j if ord(j) < 128 else " " for j in a_summary["summary"]])

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
                            "summary": d_summary,
                            "id": a_summary["id"],
                            "query": query,
                            "score": score
                        }
                        q_selected_summaries.append(summary_meta)

                # Sort the summaries and select top summaries
                # equal to the response count
                q_top_summaries = sorted(q_selected_summaries,
                                         key=lambda k: k['score'],
                                         reverse=True)[:response_count]

                # Remove score key from each top summary
                for k, a_top_summary in enumerate(q_top_summaries):
                    del a_top_summary["score"]

                    # Get author name corresponding to book_id
                    resp_author_ms = self.get_author_name(a_top_summary["id"])
                    a_top_summary["author"] = resp_author_ms

                summaries.append(q_top_summaries)
            return summaries

    def get_author_name(self, book_id):
        """
        Method to get author metadata
        for another microservice
        """

        req_data = {
            "book_id": book_id
        }

        req = requests.post(self.config["author_ms_api"]["endpoint"],
                            json=req_data)
        resp_json = req.json()

        if resp_json:
            return resp_json["author"]
        else:
            return ""


if __name__ == "__main__":
    print("Main function of search summary")
