from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound


def convert_to_voice():
    # the model of TTS
    key = '{yourApiKey}'
    url = '{url}'

    # Authenticate
    authenticator = IAMAuthenticator(key)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)

    # Reading from a File
    with open('output.txt', 'r') as f:
        text = f.readlines()

    # replace of  " to space
    text = [line.replace('"', '') for line in text]
    text = ''.join(str(line) for line in text)

    # output as mp3 file
    with open('./voiceReply.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
        audio_file.write(res.content)

def main():

    # calling function to convert to speech
    convert_to_voice()



if __name__ == "__main__":
    main()


