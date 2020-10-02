#!/usr/bin/env bash

echo "--- Generate code ..."
cd /app/grpc_server
python proto_code_gen.py


cd ..
echo "--- Starting server..."

exec python main.py
