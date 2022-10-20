from asyncore import read
import speech_recognition as sr
import pyaudio
import sounddevice as sd
import soundfile as sf
import text_to_speech as t2s

p = pyaudio.PyAudio()
r =  sr.Recognizer()
mic= sr.Microphone(3)

while True:
    with mic as source:
        print("なんか喋れ")
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    try:
        print ("解析中")
        
        # 日本語解析
        readText = r.recognize_google(audio, language='ja-JP')
        print(readText)

        # 出力音声ファイル名
        filepath = f"output/{readText}.wav"

        # 喋らせる
        t2s.synthesis(readText,filepath,14);

        # 再生デバイス設定
        sd.default.device = 10
        # sig: 信号, samp: サンプリング周波数
        sig, samp = sf.read(filepath, always_2d=True)
        sd.play(sig, samp)
        # 再生完了待ち
        sd.wait()

    # 以下は認識できなかったときに止まらないようにするため
    except sr.UnknownValueError:
        print("何言ってるかわからん")
    except sr.RequestError as e:
        print("ぐーぐるすぴーちオワタ; {0}".format(e))


