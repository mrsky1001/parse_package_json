# perfectly package json
The script reduces the dependency versions to a single number (it also removes ^ and ~ from the dependency lines).

The script accepts the path to the reference `package.json` as input and to the file being checked.  

Example use:  
`
python good_packages.py  package_template.json package.json
`

Example package_template.json

```
{
  "name": "client",
  "version": "1.0.0",
  "description": "",
  "scripts": {},
  "author": "Mr.Sky1001",
  "dependencies": {
    "axios": "0.21.1",
    "bootstrap": "4.6.0",
    "font-awesome": "4.7.0",
    "react": "16.14.0"
  },
  "devDependencies": {
    "eslint": "5.16.0",
    "parcel": "1.12.3"
  }
}
```


Example package.json

```
{
  "name": "client",
  "version": "1.0.0",
  "description": "",
  "scripts": {},
  "author": "Mr.Sky1001",
  "dependencies": {
    "axios": "^0.20.1",
    "bootstrap": "~4.6.0",
    "font-awesome": "4.7.0",
    "react": "14.14.0",
    "react-bootstrap-table": "^4.3.1",
    "react-bootstrap-table-next": "^3.3.5",
    "react-bootstrap-table2-editor": "^1.4.0",
    "react-bootstrap-table2-filter": "^1.3.3",
    "react-bootstrap-table2-overlay": "2.0.0",
    "react-bootstrap-table2-paginator": "2.1.2",
    "react-bootstrap-table2-toolkit": "2.1.3",
  },
  "devDependencies": {
    "eslint": "3.0.0",
    "parcel": "^1.10.3"
  }
}
```

Result package:
```
{
  "name": "client",
  "version": "1.0.0",
  "description": "",
  "scripts": {},
  "author": "Mr.Sky1001",
  "dependencies": {
    "axios": "0.21.1",
    "bootstrap": "4.6.0",
    "font-awesome": "4.7.0",
    "react": "16.14.0",
    "react-bootstrap-table": "4.3.1",
    "react-bootstrap-table-next": "3.3.5",
    "react-bootstrap-table2-editor": "1.4.0",
    "react-bootstrap-table2-filter": "1.3.3",
    "react-bootstrap-table2-overlay": "2.0.0",
    "react-bootstrap-table2-paginator": "2.1.2",
    "react-bootstrap-table2-toolkit": "2.1.3",
  },
  "devDependencies": {
    "eslint": "5.16.0",
    "parcel": "1.12.3"
  }
}
```

And Log:

```
====================== Starting compare files: ==========================
src: packagetemp.json
dst: package.json
"axios":: "^0.20.1" --> : "0.21.1"
"bootstrap":: "~4.6.0" --> : "4.6.0"
"react":: "14.14.0" --> : "16.14.0"
Warning! That dependency not exist in template!
 --->"react-bootstrap-table": "^4.3.1"
Warning! That dependency not exist in template!
 --->"react-bootstrap-table-next": "^3.3.5"
Warning! That dependency not exist in template!
 --->"react-bootstrap-table2-editor": "^1.4.0"
Warning! That dependency not exist in template!
 --->"react-bootstrap-table2-filter": "^1.3.3"
Warning! That dependency not exist in template!
 --->"react-bootstrap-table2-overlay": "2.0.0"
Warning! That dependency not exist in template!
 --->"react-bootstrap-table2-paginator": "2.1.2"
Warning! That dependency not exist in template!
 --->"react-bootstrap-table2-toolkit": "2.1.3"
"eslint":: "3.0.0" --> : "5.16.0"
"parcel":: "^1.10.3" --> : "1.12.3"
Replace all [^, ~]!
Finish parse!
```

