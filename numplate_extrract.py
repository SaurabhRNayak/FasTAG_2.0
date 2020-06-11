import requests
import base64
import json
import credentials


def ocr(IMAGE_PATH):
    SECRET_KEY = credentials.secret_key
    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=ind&secret_key=%s' % (
        SECRET_KEY)  # Replace 'ind' with  your country code
    r = requests.post(url, data=img_base64)
    jsonRes = json.dumps(r.json(), indent=2)
    jsonRes = json.loads(jsonRes)
    # print(jsonRes)
    try:
        # print("Numplate_value:",jsonRes["results"][0]["plate"])
        return (jsonRes["results"][0]["plate"])

    except:
        print("No number plate found")


if __name__== "__main__":
    ans=ocr(r'E:\Hackerearth\Round 2\conda_tens\test_img\test11.jpeg')
    print("ans:",ans)