customers = []


def create_customer(data):
    customer = {
        "id": len(customers) + 1,
        **data.dict()
    }

    customers.append(customer)

    return customer


def get_customer(customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    return None


def get_all_customers():
    return customers


def update_customer(customer_id, data):
    customer = get_customer(customer_id)

    if not customer:
        return None

    update_data = data.dict(exclude_unset=True)

    for key, value in update_data.items():
        customer[key] = value

    return customer


def delete_customer(customer_id):
    global customers

    customer = get_customer(customer_id)

    if not customer:
        return False

    customers = [c for c in customers if c["id"] != customer_id]

    return True