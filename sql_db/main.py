import asyncio
from prisma import Prisma
from prisma.models import Product


prisma = Prisma()

TYPE = (
    'Овощи', 
    "Фрукты"
)


def decorator_function(func):
    async def wrapper(*args, **kwargs):
        await prisma.connect()
        data = await func(*args, **kwargs)
        await prisma.disconnect()
        return data
    return wrapper



@decorator_function
async def create_product(title, type, color, calorie, description, short_desc):
    """Create a new product."""
    
    
    if type >= len(TYPE) or type < 0:
        raise ValueError("Invalid type")
    try:
        return await prisma.query_raw(
        'INSERT INTO product(title, type, color, calorie, description, short_desc) VALUES (?,?,?,?,?,?)',
        title,
        type,
        color,
        calorie,
        description,
        short_desc,
        )
    except Exception as e:
        print(e)


@decorator_function
async def get_all_product():
    """Get all products."""
    all_products = await prisma.query_raw('SELECT * FROM product')
    return all_products



@decorator_function
async def get_fruit():
    """Get all fruit products."""
    
    fruit_products = await prisma.query_raw(
        'SELECT * FROM product WHERE type = 1'
    )
    return fruit_products

@decorator_function
async def get_vegetable():
    """Get all vegetable products."""
    vegetable_products = await prisma.query_raw(
        'SELECT * FROM product WHERE type = 0'
    )
    return vegetable_products


# Отображение всех названий овощей и фруктов;
@decorator_function
async def get_all_names():
    all_names = await prisma.query_raw(
        'SELECT title FROM product VALUE '
    )
    return all_names

# Отображение всех цветов. Цвета должны быть уни-
# кальными;
@decorator_function
async def get_all_colors():
    all_colors = await prisma.query_raw(
        'SELECT DISTINCT color FROM product'
    )
    return all_colors


# ■ Отображение фруктов конкретного цвета;
@decorator_function
async def get_fruit_by_color(color, field:str|tuple='*', ):
    if isinstance(field, tuple):
        field_str = ', '.join(field)
    if isinstance(field, str):
        field_str = field
    fruit_by_color = await prisma.query_raw(
        f'SELECT {field_str} FROM product WHERE type = 1 AND color =?',
        color
    )
    return fruit_by_color


@decorator_function
async def get_vegetable_by_color(color, field:str|tuple='*'):
    if isinstance(field, tuple):
        field_str = ', '.join(field)
    if isinstance(field, str):
        field_str = field
    fruit_by_color = await prisma.query_raw(
        f'SELECT {field_str} FROM product WHERE type = 0 AND color =?',
        color
    )
    return fruit_by_color
    

async def main() -> None:

    # product = await create_product(
    #     'Банан2',
    #     1,
    #     'yellow',
    #     85,
    #     'Очень вкусный и полезный банан',
    #     'Бананы - один из самых популярных овощей'
    # )

    # products = await get_all_product()
    # vegetable = await get_vegetable()
    # fruit = await get_fruit()
    # all_names = await get_all_names()
    # all_colors = await get_all_colors()
    fruit_by_color = await get_vegetable_by_color('yellow', field=('title', 'color'))
    print(fruit_by_color)

if __name__ == '__main__':
    asyncio.run(main())