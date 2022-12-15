import requests
from flask import Flask, render_template
from flask import jsonify
from main import headers
from helper import get_images
from helper import get_networks
from helper import get_token
from helper import get_flavors
from helper import get_keypairs
from helper import get_security_groups
from flask import Flask
from main import server

app = Flask ('Final')

env_url = "https://api-uat-001.ormuco.com"
keystone_port = '5000'
glance_port = '9292'
neutron_port = '9696'
nova_port = '8774'
@app.route('/')
def index():
    headers = get_token(env_url, keystone_port)
    images = get_images(env_url, glance_port, headers)
    networks = get_networks(env_url, neutron_port, headers)
    flavors = get_flavors(env_url, nova_port, headers)
    keypairs = get_keypairs(env_url, nova_port, headers)
    security_groups = get_security_groups(env_url, nova_port, headers)
    return render_template("index.html", 
                        images = images, networks = networks, flavors = flavors, keypairs = keypairs, security_groups = security_groups)

@app.route('/CICreate', methods=['POST'])
def create_instance():
    server_on_cloud = requests.post(f'{env_url}:{nova_port}/v2.1/servers', json=server, headers=headers)
    print(server_on_cloud.reason)
    print(server_on_cloud.text)
    return "Server create"

app.run(debug=True)