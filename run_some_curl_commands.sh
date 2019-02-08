#!/bin/bash

echo "curl -i -H "Content-Type: application/json" -X POST -d '["category3"]' http://localhost:5000/api/category/add"
curl -i -H "Content-Type: application/json" -X POST -d '["category3"]' http://localhost:5000/api/category/add

echo "curl -i -H "Content-Type: application/json" -X GET -d '{}' http://localhost:5000/api/category/list"
curl -i -H "Content-Type: application/json" -X GET -d '{}' http://localhost:5000/api/v1/categories

echo "curl -i -H "Content-Type: application/json" -X DELETE -d '["category2"]' http://localhost:5000/api/category/remove"
curl -i -H "Content-Type: application/json" -X DELETE -d '["category2"]' http://localhost:5000/api/category/remove

echo "curl -i -H "Content-Type: application/json" -X GET -d '{}' http://localhost:5000/api/category/list"
curl -i -H "Content-Type: application/json" -X GET -d '{}' http://localhost:5000/api/category/list

echo "curl -i -H "Content-Type: application/json" -X DELETE -d '{}' http://localhost:5000/api/v1/acts/1234"
curl -i -H "Content-Type: application/json" -X DELETE -d '{}' http://localhost:5000/api/v1/acts/1234

echo "curl -i -H "Content-Type: application/json" -X POST -d '{"username":"shashank","password":"8b832b62abf2bd5180f6a225e4b99cac1392ea10"}' http://localhost:5000/api/v1/users"
curl -i -H "Content-Type: application/json" -X POST -d '{"username":"shashank","password":"8b832b62abf2bd5180f6a225e4b99cac1392ea10"}' http://localhost:5000/api/v1/users

curl -i -H "Content-Type: application/json" -X DELETE -d '{}' http://localhost:5000//api/v1/users/shashank

curl -i -H "Content-Type: application/json" -X POST -d '["category3"]' http://localhost:5000/api/v1/categories

curl -i -H "Content-Type: application/json" -X DELETE -d '{}' http://localhost:5000/api/v1/categories/category1

#add user done
