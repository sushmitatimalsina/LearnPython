def transform_data(sale):
    clean_sales = []

    for item in sale:
        if item["price"] is None:
            item["price"] = "Not Available"

        item["total_price"] = item["quantity"] * item["price"] if isinstance(item["price"], (int, float)) else 0
        clean_sales.append(item)


    return clean_sales
