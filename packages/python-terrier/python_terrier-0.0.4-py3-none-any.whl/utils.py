import pandas as pd
from jnius import autoclass, cast
import pytrec_eval
import json

class Utils:
    @staticmethod
    def parse_trec_topics_file(file_path):
        system = autoclass("java.lang.System")
        system.setProperty("TrecQueryTags.doctag","TOP");
        system.setProperty("TrecQueryTags.idtag","NUM");
        system.setProperty("TrecQueryTags.process","TOP,NUM,TITLE");
        system.setProperty("TrecQueryTags.skip","DESC,NARR");

        trec = autoclass('org.terrier.applications.batchquerying.TRECQuery')
        tr = trec(file_path)
        topics_lst=[]
        while(tr.hasNext()):
            topic = tr.next()
            qid = tr.getQueryId()
            topics_lst.append([qid,topic])
        topics_dt = pd.DataFrame(topics_lst,columns=['qid','query'])
        return topics_dt

    # Convert dataframe with columns: [qid,docno,score] into a dict {qid1: {doc1:score,doc2:score } qid2:...}
    @staticmethod
    def convert_df_to_pytrec_eval(df, score_int=False):
        run_dict_pytrec_eval = {}
        for index, row in df.iterrows():
            if row['qid'] not in run_dict_pytrec_eval.keys():
                run_dict_pytrec_eval[row['qid']] = {}
            if score_int:
                run_dict_pytrec_eval[row['qid']][row['docno']] = int(row['score'])
            else:
                run_dict_pytrec_eval[row['qid']][row['docno']] = float(row['score'])
        return(run_dict_pytrec_eval)

    @staticmethod
    def parse_qrels(file_path):
        dph_results=[]
        with (open(file_path, 'r')) as qrels_file:
            for line in qrels_file:
                split_line=line.strip("\n").split(" ")
                dph_results.append([split_line[0], split_line[2],split_line[3]])
        res_dt = pd.DataFrame(dph_results,columns=['qid','docno','score'])
        return res_dt

    # @staticmethod
    # def evaluate(res,qrels):
    #     batch_retrieve_results_dict = Utils.convert_df_to_pytrec_eval(res)
    #     qrels_dic=Utils.convert_df_to_pytrec_eval(qrels, True)
    #     evaluator = pytrec_eval.RelevanceEvaluator(qrels_dic, {'map', 'ndcg'})
    #     return json.dumps(evaluator.evaluate(batch_retrieve_results_dict), indent=1)


    @staticmethod
    def form_dataframe(query):
        if type(query)==type(pd.DataFrame()):
            return query
        elif type(query)==type(""):
            return pd.DataFrame([["1", query]],columns=['qid','query'])
        # if queries is a list or tuple
        elif type(query)==type([]) or type(query)==type(()):
            #if the list or tuple is made of strings
            if query!=[] and type(query[0])==type(""):
                indexed_query = []
                for i,item in enumerate(query):
                    # all elements must be of same type
                    assert type(item) is type(""), "%r is not a string" % item
                    indexed_query.append([str(i+1),item])
                return pd.DataFrame(indexed_query,columns=['qid','query'])
