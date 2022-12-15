from helper import get_token
from helper import get_images
from helper import get_networks
from helper import get_flavors
from helper import get_keypairs
from helper import get_security_groups
from helper import create_instance
from flask import Flask
env_url = "https://api-uat-001.ormuco.com"
keystone_port = '5000'
glance_port = '9292'
neutron_port = '9696'
nova_port = '8774'
headers = get_token(env_url, keystone_port)
images = get_images(env_url, glance_port, headers)
networks = get_networks(env_url, neutron_port, headers)
flavors = get_flavors(env_url, nova_port, headers)
keypairs = get_keypairs(env_url, nova_port, headers)
security_groups = get_security_groups(env_url, nova_port, headers)


server = {
    "server": {
        "name": "Sergio_Instance",
        "imageRef": images[0].get('id'),
        "flavorRef": flavors[0].get('id'),
        "key_name": keypairs[0].get('name'),
        "security_groups": [{
            "name": security_groups[0].get('name')
        }],
        "networks": [{
            "uuid": networks[0].get('id')
        }]
    }
}

create_instance(env_url, nova_port, headers, server)
