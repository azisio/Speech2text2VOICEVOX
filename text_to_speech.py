import requests
import json
import time



def SynthesizeVoice(text , filename, speaker, max_retry=10):
    '''
    text      :喋らせたいテキスト
    filename  :出力ファイル名
    speaker   :喋らせるキャラ(http://localhost:50021/speakers)
    max_retry :最大リトライ回数
    '''

    query_payload = {"text":text, "speaker":speaker}
    for query in range(max_retry):
        req = requests.post("http://localhost:50021/audio_query", 
                        params=query_payload, timeout=(5.0, 100.0))
        if req.status_code == 200:
            query_data = req.json()
            break
        time.sleep(1)
    else:
        raise ConnectionError("リトライ回数が上限に到達。 audio_query : ", filename, "/", text, req.text)

    synth_payload = {"speaker": speaker}    
    for synth_i in range(max_retry):
        req = requests.post("http://localhost:50021/synthesis", params=synth_payload, 
                          data=json.dumps(query_data), timeout=(10.0, 300.0))
        if req.status_code == 200:
            with open(filename, "wb") as fp:
                fp.write(req.content)
            break
        time.sleep(1)
    else:
        raise ConnectionError("リトライ回数が上限に到達。 synthesis : ", filename, "/", text, req,text)
