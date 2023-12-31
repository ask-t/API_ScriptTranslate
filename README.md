# API_ScriptTranslate

## Language and Framework

Python 3

Flask-RESTful

## URL
https://api-scripture.onrender.com

## Get Old Testament Request
```js
GET /api/ot?book={{book}}&chapter={{chapter}}&start={{start}}&end={{end}}
```
### Get Old Testament Reponse

```js
200 OK
```
```
{
  "chapter": <String>,
  "English": <String>,
  "Japanese":<String>
}
```


## Get New Testament Request
```js
GET /api/nt?book={{book}}&chapter={{chapter}}&start={{start}}&end={{end}}
```
### Get New Testament Reponse
```js
200 OK
```
```
{
  "chapter": <String>,
  "English": <String>,
  "Japanese":<String>
}
```

## Get Book of Mormon Request
```js
GET /api/bom?book={{book}}&chapter={{chapter}}&start={{start}}&end={{end}}
```
### Get Book of Mormon Response
```js
200 OK
```
```
{
  "chapter": <String>,
  "English": <String>,
  "Japanese":<String>
}
```

## Get Doctrine and Covenants
```js
GET /api/dc?chapter={{chapter}}&start={{start}}&end={{end}}
```
### Get Doctrine and Covenants Response

```js
200 OK
```
```
{
  "chapter": <String>,
  "English": <String>,
  "Japanese":<String>
}
```

## Get Pearl of Great Price Request
```js
GET /api/pgp?book={{book}}&chapter={{chapter}}&start={{start}}&end={{end}}
```
### Pearl of Great Price Reponse
```js
200 OK
```
```
{
  "chapter": <String>,
  "English": <String>,
  "Japanese":<String>
}
```
