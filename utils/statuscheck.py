import requests
from bottle import route, run
from bottle import template
import json
from templates.info import INFORMATION_TEMPLATE, health_check_template
from pprint import pprint


@route('/')
def hello():
    return "Hello Inmobians!"



 #print(data['servers'][0])


@route('/status')
def status():
    """
    Return the template that is to be rendered
    :return:
    """

    with open('data.json') as data_file:
        data = json.load(data_file)
    #print(data['servers'])
    #print(data['columns'])

    for i in data['servers']:
        for j in data['columns']:
             if j!="0":
                  try:
                      # print(data['servers'][i][j])
                      print(get_status(data['servers'][i][j]))
                      data['servers'][i][j] = get_status(data['servers'][i][j])
                  except:
                      #return "Invalid Json!!!. Please insert a valid keyvalue inside data.json and Try again."
                      data['servers'][i][j] = 'white'

    return template(health_check_template,data=data)


def get_status(server_info):
    """
    Return the status of the pong response
    :param server_info:
    :return:
    """
    url = server_info
    try:
        resp = requests.get(url)
        if resp.text.__contains__("pong"):
            return "green"
        else:
            return "red"
    except requests.ConnectionError as e:
        #print(isinstance(e, requests.exceptions.ConnectTimeout))
        return "grey"
    except Exception as ex:
        return "white"


@route('/info')
def status():
    """
    Return the template that is to be rendered
    :return:
    """
    return template(INFORMATION_TEMPLATE)




if __name__ == '__main__':
    run(host='localhost', port=8022, debug=True)
