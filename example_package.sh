#!/bin/bash

echo "Generating example package..."

# You can put this on r/badcode if you want ;)
mkdir packages # If this folder doesn't exist 
mkdir packages/package
mkdir packages/package/releases
mkdir packages/package/releases/0/

echo "If you are seeing this file, everything works correctly" > packages/package/releases/0/message.txt
echo "{
        "author": "author",
        "name": "package-name",
        "title": "Package Title",
        "short_description": "example package",
        "release": 0
}" > packages/package/meta.json

cd packages/package/releases/0/
zip pack.zip message.txt

echo "Done!"
