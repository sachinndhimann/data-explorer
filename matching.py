from polyfuzz import PolyFuzz
from polyfuzz.models import EditDistance, TFIDF, Embeddings
from flair.embeddings import TransformerWordEmbeddings
embeddings = TransformerWordEmbeddings('bert-base-multilingual-cased')
bert = Embeddings(embeddings, min_similarity=0.5, model_id="BERT")
tfidf = TFIDF(min_similarity=0)
edit = EditDistance()
string_models = [bert]
to_list = ["testing","tast","tests","tist"]
from_list = ["test"]
print(to_list)
model = PolyFuzz(string_models)
model.match( to_list,from_list)
#model.group(link_min_similarity=0.75)
matches=model.get_matches()

#matches=matches[matches["Similarity"] !=0.000]
#matches.sort_values(by = 'Similarity')
print(matches)
print(type(matches))
#list_of_matches=matches["Similarity"].tolist()
#print(len(list_of_matches))