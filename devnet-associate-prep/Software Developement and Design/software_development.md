# Comparing data structures

## XML
- Mandatory XML header
- Mandatory top-most element
- List elements
- Standard data in "elements"
- Closing element prepended with forward slash "/" like HTML language
- Setting attributes like "type" bellow
- Useful but ofthen hard to translate
```
<?xml version="1.0" enconding="UTF-8"?>
<root>
    <customer_list type="private_customer">
        <name>Natan Nascimento</name>
        <idade>21</idade>
        <is_happy>true</is_happy>
    </customer_list>
    <customer_list type="public_customer">
        <name>Irineu</name>
        <idade>35</idade>
        <is_happy>false</is_happy>
    </customer_list>
</root>
```

## JSON
- Wrapped in { }
- Lists use []
- List of dictionaries
- Data Type: string, int and boolean atributes
- Comma-separated dicts
```
{
    "customer_list":[
        {
            "name":"Natan Nascimento",
            "idade":21,
            "is_happy": true
        },
        {
            "name":"Irineu",
            "idade":35,
            "is_happy": false
        }
    ]
}
```

