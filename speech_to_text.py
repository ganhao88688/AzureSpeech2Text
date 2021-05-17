# encoding: utf-8
'''
官方文件 https://docs.microsoft.com/zh-tw/azure/cognitive-services/speech-service/get-started-speech-to-text?tabs=windowsinstall&pivots=programming-language-python#prerequisites
'''
import azure.cognitiveservices.speech as speechsdk
import time

def from_file():
    speech_config = speechsdk.SpeechConfig(subscription="7f9a0e1c8311474b9718aa808216c360", region="westus")
    speech_config.speech_recognition_language="zh-TW"#指定輸入 (或來源) 語言
    audio_input = speechsdk.AudioConfig(filename=".\short.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    
    done = False
    #result = speech_recognizer.recognize_once_async().get()
    #錯誤處理
    
#    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#        print("Recognized: {}".format(result.text))
#    elif result.reason == speechsdk.ResultReason.NoMatch:
#        print("No speech could be recognized: {}".format(result.no_match_details))
#    elif result.reason == speechsdk.ResultReason.Canceled:
#       cancellation_details = result.cancellation_details
#       print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#        if cancellation_details.reason == speechsdk.CancellationReason.Error:
#            print("Error details: {}".format(cancellation_details.error_details))
    all_result = ""
    
    #停止
    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    
    def handle_final_result(evt):
        nonlocal all_result
        all_result += evt['combinedRecognizedPhrases']['lexical']
        println(all_result)
    
    #定義與顯示
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt[''])))#(lambda evt: handle_final_result(evt))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)
    all_result = speech_recognizer.start_continuous_recognition()
    
    while not done:
        time.sleep(.5)
    print('all_result: {}'.format(all_result))
    #print(all_result)
from_file()



