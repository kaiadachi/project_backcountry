import requests
import pandas as pd
import codecs
import traceback

def saveImg(img_url, folder_name, isMatch):
    if(isMatch):
        return 0

    if("https:" not in img_url):
        img_url = "https:" + img_url

    re = requests.get(img_url)

    img_name = img_url.split('/')[-2:]
    img_name = "_".join(img_name)
    with open("{0}/{1}".format(folder_name, img_name), 'wb') as f:
        f.write(re.content)

    return img_name


def getAttribute(selenium_array, type):
    return [i.get_attribute(type) for i in selenium_array]

def createCsv(data, folder_csv, name, isHeader, sep):
    fliename = '{0}/{1}'.format(folder_csv, name)
    try:
        with codecs.open(fliename, mode='w' ,encoding="Shift_jis", errors='ignore') as f:
            data.to_csv(f, index=False, header=isHeader, sep=sep)
    except Exception as e:
        print(traceback.format_exc())
        try:
            data.to_csv(fliename, encoding="utf-8")
        except:
            data.to_csv(fliename)

def getMatch(df, name):
    if( (df.columns=='name').sum() == 0 ):
        return False

    df_match = ( df['name'] == name )
    count = df_match.sum()
    print(count)
    if(count > 0):
        return True
    else:
        return False