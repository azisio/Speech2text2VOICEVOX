# マイク入力でずんだもんに喋らせる

## 動作概要

音声認識でテキスト化したあとずんだもんとかに喋らせる（遅延すごい）

```
マイク入力
↓
SpeechRecognition(Googleの音声認識)
↓
VOICEVOX ENGINEにリクエスト投げる
↓
WAVファイルを作ってもらう
↓
WAVファイルを再生（デバイス指定して）
```

## 必要動作環境

### 必須

- Python 3.9.6
- VOICEVOX Ver0.13.2 (GPU)

### 便利

- VoiceMeeter Banana（仮想オーディオデバイス＆ミキサー的な）
    - Discordとかでずんだもんに喋らせたいときに使える

