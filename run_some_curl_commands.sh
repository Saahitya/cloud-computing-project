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
 data:image/png;base64,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
