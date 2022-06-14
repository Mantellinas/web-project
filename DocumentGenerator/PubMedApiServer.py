from flask import Flask, json
import requests
from datetime import datetime
ES_ADDRESS = "http://elasticsearch:9200"
SPACY_ADDRESS = "http://spacy:8088/entities"

PubMedApi = Flask(__name__)

f = open('articles_bulk.json')
data = json.load(f)
print("caricato")
i = -1


@PubMedApi.route("/getData")
def getData():
    global i
    global data

    i += 1
    if i == len(data):
        i = 0
        
    article = data[i]
    print("articoloooo")
    print(article)
    text_full_text = article['full_text']['text']
    for item in article['full_text']['sections']:
        text_full_text += item['text']
    query = {
        "text": text_full_text,
    }
    
    try:
        query = { "pmcid": "string" , "text" : query['text']}
        resp = requests.post(url=SPACY_ADDRESS, json=query) 
        data = resp.json()
    
        nodesDict = []
        source = []

        for item in data['nodes']:
            nodesDict.append({"name" : item, "text": data['nodes'][item]['text'], "categories": data['nodes'][item]['categories'], "wid":data['nodes'][item]['wid'], "rho":data['nodes'][item]['rho']}) 
        
        for item in data['sentences']:
            for edge in item['edges']:
                source.append({"source": edge['src_pos'], "target": edge['dst_pos'], "value": edge['edge_name']})
        
        temp_dict = {"timestamp": datetime.now().isoformat(),"nodes": nodesDict, "links": source}
        graph_dict = json.dumps(temp_dict)

        return graph_dict   
    except:
        print("errore")
        return
    

    


if __name__ == "__main__":
    PubMedApi.run(debug=True,
            host='0.0.0.0',
            port=9000)