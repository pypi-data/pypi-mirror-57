# client-python

A Python client for the Rancher API

## Installing

**Note: This package requires Python 3+**

```
pip install git+https://github.com/rancher/client-python.git@master
```

## Using API

```python

import rancher

client = rancher.Client(url='https://localhost:8443/v3',
                        access_key='<some valid access key>',
                        secret_key='<some valid secret key>')

# curl -s https://localhost:8443/v3/users?me=true
client.list_user(me='true')

# curl -s -X POST https://localhost:8443/v3/users -H 'Content-Type: application/json' -d '{ "username" : "user1", "password": "Password1" }'
client.create_user(username='user1', password='Password1')

# curl -s -X PUT https://localhost:8443/v3/users/user-xyz123 -H 'Content-Type: application/json' -d '{ "description" : "A user" }'
user = client.by_id_user('user-xyz123')
client.update(user, description='A user')

# curl -s -X DELETE https://localhost:8443/v3/users/user-xyz123
user = client.by_id_user('user-xyz123')
client.delete(user)

# Links
# curl -s https://localhost:8443/v3/clusterRoleTemplateBindings?userId=user-xyz123
user = client.by_id_user('user-xyz123')
user.clusterRoleTemplateBindings()
```

## Examples

### Actions [Rancher API spec](https://github.com/rancher/api-spec/blob/master/specification.md#actions)
From the spec 
> "Actions perform an operation on a resource and (optionally) return a result."

To perform the `setpodsecuritypolicytemplate` action on a project object these are the steps.

This first method has built-in retry logic inside of `client.action()` when the error returned is 409
```python
#creates a project and handles cleanup
project =  admin_pc.project 
# create an api_client from a management context
api_client = admin_mc.client
# perform the action via the client api
api_client.action(obj=project, action_name="setpodsecuritypolicytemplate",
                    podSecurityTemplateId=pspt.id)
```
Or alternatively, performing the action from the project context (which does not have built-in retry logic)
```python

project = api_client.create_project(name="test-project", clusterId="local")
project.setpodsecuritypolicytemplate(podSecurityPolicyTemplateId="my-pspt")

```

# Contact
For bugs, questions, comments, corrections, suggestions, etc., open an issue in
 [rancher/rancher](//github.com/rancher/rancher/issues) with a title starting with `[rancher-python] `.

Or just [click here](//github.com/rancher/rancher/issues/new?title=%5Brancher-python%5D%20) to create a new issue.
