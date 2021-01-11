#!/usr/bin/python

import json
import requests
import sys

if len(sys.argv) == 1:
    print("To few arguments: use as following translate.py <sentence_to_translate> optional: <target_lang: DE/EN>")
    exit()

if len(sys.argv) > 2 and (sys.argv[2] == "DE" or sys.argv[2] == "EN"):
    target_lang = sys.argv[2]
else:
    target_lang = "DE"

payload = {"jsonrpc":"2.0","method": "LMT_handle_jobs",
        "params":{"jobs":
            [{"kind":"default","raw_en_sentence":sys.argv[1],
            "raw_en_context_before":[],"raw_en_context_after":[],
            "preferred_num_beams":4,"quality":"fast"}],
            "lang":{"user_preferred_langs":["DE","EN"],"source_lang_user_selected":"auto",
                "target_lang":target_lang},
            "priority":-1,"commonJobParams":{},"timestamp":1610369694627},
        "id":60490012}

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post("https://www2.deepl.com/jsonrpc", data=json.dumps(payload), headers=headers)
resp = json.loads(r.text)
translations = []
for xs in resp["result"]["translations"]:
    for x in xs["beams"]:
        translations.append(x["postprocessed_sentence"])
print(translations)
