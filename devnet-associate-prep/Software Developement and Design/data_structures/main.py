vegetables = [
    {
        "type":"fruit",
        "items":[
            {
                "color":"green",
                "items":[
                    "kiwi",
                    "grape"
                ]
            },
            {
                "color":"red",
                "items":[
                    "strawberry",
                    "apple"
                ]
            }
        ]
    },
    {
        "type":"vegs",
        "items":[
            {
                "color":"green",
                "items":[
                    "lettuce"
                ]
            },
            {
                "color":"red",
                "items":[
                    "pepper",
                ]
            }
        ]
    }
]

a = list(filter(lambda i: i[ 'type' ] == 'fruit', vegetables))

print (a[0]['items'][0]['items'][0])