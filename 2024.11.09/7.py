from ListOfDict import list_of_dicts

def merge(dicts):
    merged = {}
    
    for i in dicts:
        for key, value in i.items():
            if key not in merged:
                merged[key] = set()
            merged[key].add(value)
    return merged
            

def main():
    result = merge(list_of_dicts)
    for key in sorted(result.keys()):
        value = sorted(result[key])
        print(f"{key:<20}: {','.join(map(str, value))}")
    
main()