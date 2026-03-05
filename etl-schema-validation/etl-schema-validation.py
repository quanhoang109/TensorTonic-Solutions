def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    # Write code here
    ## Create result list
    result = []
    for idx, record in enumerate(records):
        errors = []
    ## Create column to check
        for col in schema:
            col_name = col["column"]
            expected_type = col["type"]
            nullable = col.get("nullable", False)
            min_val = col.get("min",None)
            max_val = col.get("max",None)
            ## 1. Missing Check
            if col_name not in record:
                errors.append(f"{col_name}: missing")
                continue
            value = record[col_name]
            ## 2. Null Check:
            if value is None:
                if not nullable:
                    errors.append(f"{col_name}: null")
                continue
            ## 3. Type check

            if expected_type == "float":
                # accept int and float but NOT bool
                type_ok = type(value) in (int, float)
            else:
                type_map = {"int": int, "str": str, "bool": bool}
                expected = type_map.get(expected_type)
                type_ok = type(value) == expected
            
            if not type_ok:
                actual_type = type(value).__name__
                errors.append(f"{col_name}: expected {expected_type}, got {actual_type}")
                continue  # skip range if type fails
            # 4. Range check
            if min_val is not None or max_val is not None:
                if (min_val is not None and value < min_val) or \
                   (max_val is not None and value > max_val):
                    errors.append(f"{col_name}: out of range")
        result.append((idx, len(errors) == 0, errors))
    return result