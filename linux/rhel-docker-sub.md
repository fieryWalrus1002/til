# Subcribing a RHEL8 docker image to package server 
When you first create a RHEL8 docker image, it will not be allowed to update or install any packages. You need to register the installation with Redhat. You'll need your username and password to redhat's site, and after that run the following at the command line:

```{linux}
$ subscription-manager register
Username:
Password:
$ subscription-manager attach --auto
```
This will attach the server to your account, and allow access to the package managers.
