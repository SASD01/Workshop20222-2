import requests
env_url = "https://api-uat-001.ormuco.com"
keystone_port = '5000'
glance_port = '9292'
neutron_port = '9696'
nova_port = '8774'

def get_token(env_url, keystone_port):
    url = f"{env_url}:{keystone_port}/v3/auth/tokens"
    playload = {
        "auth": {
            "identity": {
                "methods": ["password"],"password": {
                    "user": {
                        "name": "workshop2022@utb.edu.co","domain": {
                            "name": "Default"},
                        "password": "ILOVECLOUD2022"}
                    }
                }
            }
        }
    
    token = requests.post(url=url, json=playload)
    token_id = token.json().get('token').get('id')
    headers = {'X-Auth-Token':token_id}
    return headers

def get_images(env_url, glance_port, headers):
    url = f"{env_url}:{glance_port}/v2/images"
    images = requests.get(url=url, headers=headers).json().get('images')
    return images

def get_networks(env_url, neutron_port, headers):
    url = f"{env_url}:{neutron_port}/v2.0/networks"
    networks = requests.get(url=url, headers=headers).json().get('networks')
    return networks

def get_flavors(env_url, nova_port, headers):
    url = f"{env_url}:{nova_port}/v2.1/flavors"
    flavors = requests.get(url=url, headers=headers).json().get('flavors')
    return flavors

def get_keypairs(env_url, nova_port, headers):
    url = f"{env_url}:{nova_port}/v2.1/os-keypairs"
    keypairs = requests.get(url=url, headers=headers).json().get('keypairs')
    keypairs = [k.get('keypair') for k in keypairs]
    return keypairs

def get_security_groups(env_url, nova_port, headers):
    url = f"{env_url}:{nova_port}/v2.1/os-security-groups"
    security_groups = requests.get(url=url, headers=headers).json().get('security_groups')
    return security_groups

def create_instance(env_url, nova_port, headers, server):
    url = f"{env_url}:{nova_port}/v2.1/servers"
    instance = requests.post(url=url, json=server, headers=headers)
    return instance.text