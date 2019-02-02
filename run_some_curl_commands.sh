#!/bin/bash

echo "curl -i -H "Content-Type: application/json" -X POST -d '["category 3"]' http://localhost:5000/api/category/add"
curl -i -H "Content-Type: application/json" -X POST -d '["category 3"]' http://localhost:5000/api/category/add

echo "curl -i http://localhost:5000/api/category/list"
curl -i http://localhost:5000/api/category/list

echo "curl -i -H "Content-Type: application/json" -X DELETE -d '["category 3"]' http://localhost:5000/api/category/remove"
curl -i -H "Content-Type: application/json" -X DELETE -d '["category 3"]' http://localhost:5000/api/category/remove

echo "curl -i http://localhost:5000/api/category/list"
curl -i http://localhost:5000/api/category/list