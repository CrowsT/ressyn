# Api for Ressyn

Api is over json.

version 1.0

# Common

## request

```
{
  "request": "[request method]",
  ... [ request parameters ] ...
}
```

## response

* succeed

```
{
  "response": "ok",
  ... [ resources or informations ] ...
}
```

* processing

```
{
  "response": "processing",
  "info": "[info]"
}

```

* failed

```
{
  "response": "fail",
  "info": [reason]
}
```

# Manage Sniffers

## Install

```
{
  "request": "install sniffer",
  "git-repo": "[URL of git repo]",
  "user": (option)"[user name]",
  "password": (option)"[password]"
}

{
  "response": "Ok",
  "info": "[Sniffer name], version [version]"
}
```

## Update

```
{
  "request": "update sniffers"
}

{
  "response": "Ok",
  "info": "[update][Sniffer name], version [version]"
}
```

## list

```
{
  "request": "list sniffers"
}

{
  "response": "Ok",
  "info": "[All][Sniffer name], version [version]"
}
```

## uninstall

```
{
  "request": "uninstall sniffer",
  "name": "[Sniffer name]"
}

{
  "response": "ok",
  "info": "[Sniffer name]"
}
```

# Crawl Resource

## SearchBook

```
{
  "request": "search book",
  "query": "[query string]"
}

{
  "response": "ok",
  "books": [
    {
      "id": "[book-id]",
      "name": "[book-name]",
      "brief": "[brief]",
    },
    ....
  ]
}
```

## Get Catelogue

```
{
  "request": "get catalogue",
  "book": "[book id]"
}

{
  "response": "ok",
  "book": "[book id]",
  (option)"type": "[type]",
  "catalogue": [
    {
      "id": "[section id]",
      "title": "[section title]",
      (option)"type": "[type]"
    },
    ....
  ],
}
```

## Get Resource Section

```
{
  "request": "get section",
  "book": "[book id]",
  "section": "[section id]"
}

{
  "response": "ok",
  "book": "[book id]",
  "section": "[section id]",
  (option)"type": "[type]",
  "items": [
    [item],
    ....
  ]
}
```

