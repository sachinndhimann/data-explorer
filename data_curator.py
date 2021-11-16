import pandas as pd
import datacompy
import argparse
import json
from autologging import logged, traced
import logging
from datetime import datetime
from polyfuzz import PolyFuzz
from polyfuzz.models import EditDistance, TFIDF, Embeddings
from flair.embeddings import TransformerWordEmbeddings


curr_time=datetime.now()
curr_time=curr_time.strftime("%d_%m_%Y__%H_%M_%S")
logging.basicConfig(filename="logs/test_"+curr_time+".log", level=logging.INFO)


@logged
@traced
def read_data_input(filename):
    data_frame=pd.read_csv(filename)
    return data_frame

@logged
@traced
def generate_config(dataframe1,dataframe2):
    keys=list(dataframe1.columns)
    keys=list(dataframe1.columns)
    master_map=["source","target"]
    master={}
    for val in master_map:
        map={}
        for k in keys:
            map[k]="N"
        master[val]=map
    
    with open("config.json","w") as fp :
        fp.write(json.dumps(master,indent=4))

    

    pass

@logged
@traced
def get_top_5_results(input_string,list_of_strings):
    embeddings = TransformerWordEmbeddings('bert-base-multilingual-cased')
    bert = Embeddings(embeddings, min_similarity=0.5, model_id="BERT")
    string_models = [bert]
    model = PolyFuzz(string_models)
    model.match( list_of_strings,[input_string])
    #model.group(link_min_similarity=0.75)
    matches=model.get_matches()
    matches=matches[matches["Similarity"] !=0.000]
    matches.sort_values(by = 'Similarity')
    list_of_matches=matches["Similarity"].tolist()
    print(len(list_of_matches))
    if len(list_of_matches) <5:
        return matches,"partialMatch"
    elif len(list_of_matches)==0:
        return None,"noMatch"
    else:
        return matches[:5],"partialMatch"

@logged
@traced
def get_recommendations(master_dict,df2):
    keys=master_dict.keys()
    for key in keys:
        if master_dict[key]==0:
            continue
        else:
            # add condition for index
            source_df=master_dict[key]
            source_list=source_df[key].tolist()


    pass

@logged
@traced
def data_curator(unmatched,df2):
    list_of_columns=unmatched.columns
    master=[]
    for column in list_of_columns:
        compare = datacompy.Compare(
        unmatched,
        df2,
        join_columns=column,  #You can also specify a list of columns
        abs_tol=0, #Optional, defaults to 0
        rel_tol=0, #Optional, defaults to 0
        df1_name='source', #Optional, defaults to 'df1'
        df2_name='target' #Optional, defaults to 'df2'
        )
        uncommon=compare.df1_unq_rows
        if len(uncommon)==0:
            master.append({column:0})
        else:
            master.append({column:uncommon})
    return master

@logged
@traced
def data_comparator(df1,df2):

    with open("config.json",) as fp:
        data=json.load(fp)

    compare = datacompy.Compare(
    df1,
    df2,
    join_columns=data["comparisonOn"],  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='source', #Optional, defaults to 'df1'
    df2_name='target' #Optional, defaults to 'df2'
    )
    
    compare.matches(ignore_extra_columns=False)
    #print(compare.report())
    common=compare.intersect_rows
    uncommon=compare.df1_unq_rows
    return common,uncommon
    
@logged
@traced
def generate_results():
    pass


@logged
@traced
def main(dataframe1=None,dataframe2=None):
    parser=argparse.ArgumentParser()
    parser.add_argument('--config')
    args = parser.parse_args()

    file1=r'E:\Tools and Framwoks\Ideas\DataExplorer\Source.csv'
    file2=r'E:\Tools and Framwoks\Ideas\DataExplorer\Target.csv'
    # read both dataframes
    source_df=read_data_input(file1)
    target_df=read_data_input(file2)

    if args.config=="Y":
        generate_config(source_df,target_df)
    common,uncommon=data_comparator(source_df,target_df)
    result=data_curator(uncommon,target_df)
    print(result)
    #recommendations=get_recommendations(result,target_df)

#main()
print(get_top_5_results("tested",["testing","testes","taste","teseted","tests","testink"]))