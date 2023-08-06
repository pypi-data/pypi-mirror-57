# Description: Config file JSON-schema
# Documentation: config.txt

# Remark 1.7.7
# Copyright (c) 2009 - 2019
# Kalle Rutanen
# Distributed under the MIT license (see license.txt).

configSchema = {
    "$schema": "http://json-schema.org/draft-04/schema#",

    "type" : "object",
    "properties" : {
        "disable" : {
            "$ref" : "#/definitions/string_set"
        },
        "flags" : {
            "$ref" : "#/definitions/string_set"
        },
        "include" : {
            "$ref" : "#/definitions/string_set"
        },
        "exclude" : {
            "$ref" : "#/definitions/string_set"
        },
        "lines" : 
        {
            "type" : "integer",
            "minimum" : 0
        },
        "max-file-size" : 
        {
            "type" : "integer",
            "minimum" : 0
        }
    },

    "definitions" : {
        "string_set" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            }
        }
    }
}
