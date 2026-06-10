from datetime import datetime

categories = []


def create_category(data):

    category = {
        "id": len(categories) + 1,

        **data.dict(),

        "created_at": str(
            datetime.now()
        ),

        "updated_at": str(
            datetime.now()
        )
    }

    categories.append(category)

    return category


def get_category(category_id):

    for category in categories:

        if category["id"] == category_id:
            return category

    return None


def get_all_categories():
    return categories


def update_category(
    category_id,
    data
):

    category = get_category(
        category_id
    )

    if not category:
        return None

    update_data = data.dict(
        exclude_unset=True
    )

    for key, value in update_data.items():

        category[key] = value

    category["updated_at"] = str(
        datetime.now()
    )

    return category


def delete_category(
    category_id
):

    global categories

    category = get_category(
        category_id
    )

    if not category:
        return False

    categories = [
        c for c in categories
        if c["id"] != category_id
    ]

    return True