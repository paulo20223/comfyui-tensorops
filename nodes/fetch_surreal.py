from .surreal import surreal_connect

SURREAL_TABLE = "processor"

class FetchJsonFromSurreal:
   
    @classmethod    
    def INPUT_TYPES(s):
        return {
            "required": {
                "database": ("STRING", {"multiline": False}),
                "id": ("STRING", {"multiline": False}),
                "key": ("STRING", {"multiline": False})
            },
        }

    RETURN_TYPES = ("JSON",)

    FUNCTION = "main"
    OUTPUT_NODE = True
    CATEGORY = "database_ops"
    
    def main(self, database: str, id: str, key: str):
        connection = surreal_connect(database)
        query = f"SELECT {key} from {SURREAL_TABLE}:`{id}`;"
        results = connection.query(query).result
        if len(results) > 0:
            return results[0][key]
        return {}

