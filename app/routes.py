from fastapi import APIRouter
from app.db import get_db_connection
from app.models import Item

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hello DevOps World"}


@router.get("/items")
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM items;")
    rows = cur.fetchall()

    items = []
    for row in rows:
        items.append({
            "id": row[0],
            "name": row[1]
        })

    cur.close()
    conn.close()

    return {"items": items}


@router.post("/items")
def create_item(item: Item):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO items (name) VALUES (%s) RETURNING id;",
        (item.name,)
    )

    new_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return {"id": new_id, "name": item.name}
