from asyncore import read
import speech_recognition as sr
import pyaudio
import sounddevice as sd
import soundfile as sf
import text_to_speech as t2s

# 音声デバイス毎のインデックス番号を一覧表示
# pAudio = pyaudio.PyAudio()
# for x in range(0, pAudio.get_device_count()): 
#     print(pAudio.get_device_info_by_index(x))

reco = sr.Recognizer()
mic  = sr.Microphone()

while True:
    with mic as source:
        print("------喋りタイム------")
        reco.adjust_for_ambient_noise(source) #雑音対策
        audio = reco.listen(source)

    try:
        print ("解析中")
        
        # 日本語解析
        readText = reco.recognize_google(audio, language='ja-JP')
        print(readText)

        # 出力音声ファイル名
        filepath = f"output/{readText}.wav"

        # VOIVEVOXに喋らせる(音声ファイル出力)
        t2s.SynthesizeVoice(readText,filepath,3);

        # 再生デバイス設定
        # sd.default.device = 10
        
        # sig: 信号, samp: サンプリング周波数
        sig, samp = sf.read(filepath, always_2d=True)
        sd.play(sig, samp)
        # 再生完了待ち
        sd.wait()

    # 以下は認識できなかったときに止まらないようにするため
    except sr.UnknownValueError:
        print("うまく聞き取れませんでした")
    except sr.RequestError as e:
        print("GoogleSpeechのリクエスト死亡; {0}".format(e))


