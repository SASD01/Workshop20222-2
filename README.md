# Workshop20222-2
This project consists of developing a solution based on Openstack and Flask technologies, to implement a cloud computing platform. This platform will allow users to create and manage their own cloud computing instances, as well as instances of virtual machines, storage, networking, security and other services.

# Documentation:

## get_token()
Makes an authentication request to the OpenStack Keystone service and returns a dictionary of HTTP headers including the obtained authentication token.

## get_images()
Makes a request to the OpenStack Glance service for a list of available images and returns the list.

## get_networks()
Makes a request to the OpenStack Neutron service to get a list of available networks and returns the list.

## get_flavors()
Makes a request to the OpenStack Nova service to get a list of flavors or "types" of virtual machine instances and returns the list.

## get_keypairs()
Makes a request to the OpenStack Nova service to get a list of available key pairs and returns the list.

## get_security_groups()
Makes a request to the OpenStack Nova service to get a list of available security groups and returns the list.

## create_instance()
Makes a request to the OpenStack Nova service to create a new virtual machine instance with the specified configuration and returns the result of the request.
