# restapi-cpprestsdk-conan



```
mkdir build
cd build
conan export .. helloworld-restapi-cpprestsdk-conan/1.0.0@mycpptutorial/stable

conan remote remove helloworld-restapi-cpprestsdk-conan/1.0.0@mycpptutorial/stable

conan remote add helloworld-restapi-cpprestsdk-conan/1.0.0@mycpptutorial/stable https://api.bintray.com/conan/mycpptutorial/restapi-cpprestsdk

conan user -p <APIKEY> -r helloworld-restapi-cpprestsdk-conan/1.0.0@mycpptutorial/stable yourbintrayusername


conan install helloworld-restapi-cpprestsdk-conan/1.0.0@mycpptutorial/stable --build=helloworld-restapi-cpprestsdk-conan

conan upload "helloworld-restapi-cpprestsdk-conan/1.0.0@mycpptutorial/stable" -r helloworld-restapi-cpprestsdk-conan/1.0.0@mycpptutorial/stable --all
```
