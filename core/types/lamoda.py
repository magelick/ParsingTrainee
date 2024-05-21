from decimal import Decimal
from typing import Optional, Dict

from pydantic import Field, PositiveInt

from core.types.base import DTO


class LamodaBasic(DTO):
    """
    Basic schema of Lamoda parser
    """


class SneakerParserBasic(LamodaBasic):
    """
    Base pydantic schema of sneaker parser
    """

    # brand
    brand: str = Field(
        default=...,
        max_length=128,
        title="Бренд",
        description="Название бренда",
        examples=[
            "ASICS",
            "Anta",
            "Calvin Klein Jeans",
            "New Balance",
            "Nike",
            "PUMA",
        ],
    )
    # model
    model: Optional[str] = Field(
        default="",
        max_length=128,
        title="Модель",
        description="Название модели определённого бренда",
        examples=[
            "GEL-LYTE III",
            "WALKER",
            "",
            "530",
            "NIKE AIR MAX EXCEE",
            "Blktop Rider Preppy",
        ],
    )
    # price
    price: Optional[Decimal] = Field(
        default=None,
        max_digits=5,
        decimal_places=2,
        title="Цена",
        description="Цена конкретной модели конкретного бренда",
        examples=["120.00, 419,59, 999.99"],
    )


class SneakerParserAddForm(SneakerParserBasic):
    """
    Schema of add new sneaker
    """

    ...


class SneakerParserUpdateForm(SneakerParserBasic):
    """
    Schema of update exist sneaker
    """

    ...


class SneakerDetail(SneakerParserBasic):
    """
    Schema of sneaker detail
    """

    # id
    _id: Optional[PositiveInt] = Field(
        default=None, title="ID", description="ID кокнретной пары кроссовок"
    )
    # article
    article: Optional[str] = Field(
        default=None,
        title="Артикул",
        description="Артикул кокнретной пары кроссовок",
    )
    # kind of sport
    kind_of_sport: Optional[str] = Field(
        default=None,
        title="Вид спорта",
        description="Вид спорта, под который подходит данная пара кроссовок",
    )
    # internal material
    internal_material: Optional[str] = Field(
        default=None,
        title="Внутренний материал",
        description="Внутренний материал пары кроссовок",
    )
    # outer material
    outer_material: Optional[str] = Field(
        default=None,
        title="Внешний материал",
        description="Внешний материал пары кроссовок",
    )
    # sole material
    sole_material: Optional[str] = Field(
        default=None,
        title="Материал подошвы",
        description="Материал подошвы пары кроссовок",
    )
    # insole material
    insole_material: Optional[str] = Field(
        default=None,
        title="Материал стельки",
        description="Материал стельки пары кроссовок",
    )
    # season
    season: Optional[str] = Field(
        default=None,
        title="Сезон",
        description="Сезон, под который подходят данные кроссовки",
    )
    # country of production
    country_of_production: Optional[str] = Field(
        default=None,
        title="Страна производства",
        description="Страна, в которой произведена пара кроссовок",
    )
    # color
    color: Optional[str] = Field(
        default=None, title="Цвет", description="Цвет данной пары кроссовок"
    )
    # clasp
    clasp: Optional[str] = Field(
        default=None, title="Застёжка", description="Застёжка пары кроссовок"
    )


class SneakerParserHrefBasic(LamodaBasic):
    """
    Basic schema of href and other params by sneaker
    """

    # href
    href: Dict[str, str] = Field(
        default=...,
        title="Пара кроссовок",
        description="Кокретная пара кроссовок",
        examples=[
            "'361': {'model': 'AG4-CQT', 'price': '449.00'}",
            "'ASICS': {'model': 'GEL-LYTE III', 'price': " "'639.00 р.'}",
        ],
    )
