# import jnius_config
# jnius_config.add_classpath("../terrier-project-5.1-jar-with-dependencies.jar")
# from jnius import autoclass, cast

# import pytrec_eval
import os, json, wget
import numpy as np
import pandas as pd

def setup_terrier(file_path):
    file_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isfile(os.path.join(file_path,"terrier-assemblies-5.1-jar-with-dependencies.jar")):
        print('JAR file not found, downloading')
        url = 'https://repo.maven.apache.org/maven2/org/terrier/terrier-assemblies/5.1/terrier-assemblies-5.1-jar-with-dependencies.jar'
        wget.download(url, file_path)

file_path = os.path.dirname(os.path.abspath(__file__))
print(file_path)
setup_terrier(file_path)
import jnius_config
jnius_config.add_classpath(os.path.join(file_path,"terrier-assemblies-5.1-jar-with-dependencies.jar"))
from jnius import autoclass, cast
from utils import *
from batchretrieve import *

if __name__ == "__main__":
    JIR = autoclass('org.terrier.querying.IndexRef')
    indexref = JIR.of("../index/data.properties")
    topics = Utils.parse_trec_topics_file("../vaswani_npl/query-text.trec")
    topics_light = Utils.parse_trec_topics_file("../vaswani_npl/query_light.trec")

    feat_retrieve = FeaturesBatchRetrieve(indexref, ["WMODEL:BM25","WMODEL:PL2"])
    feat_res = feat_retrieve.transform(topics_light)
    print(feat_res)

    # retr = BatchRetrieve(indexref)
    # batch_retrieve_results=retr.transform(topics_light)
    # print(batch_retrieve_results)
    # retr.saveLastResult("dph.res")
    # retr.saveResult(batch_retrieve_results,"/home/alex/Documents/Pyterrier/result.res")

    # qrels = Utils.parse_qrels("./vaswani_npl/qrels")
    # eval = Utils.evaluate(batch_retrieve_results,qrels)
    # print(eval)
