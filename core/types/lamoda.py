from typing import Optional

from pydantic import Field

from core.types.base import DTO


class LamodaBasic(DTO):
    """
    Basic schema of Lamoda parser
    """

    ...


class SneakerInfo(DTO):
    """
    Schema of sneaker information for a specific brand
    """

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
    price: Optional[str] = Field(
        default=None,
        title="Цена",
        description="Цена конкретной модели конкретного бренда",
        examples=["120.00, 419,59, 999.99"],
    )


class SneakerParserBasic(LamodaBasic):
    """
    Base pydantic schema of sneaker parser
    """

    brand: str = Field(
        default=...,
        title="Brand",
        description="Some Brand of sneaker",
        examples=[
            {
                "brand": "New Balance",
            },
            {
                "brand": "adidas",
            },
        ],
    )
    info: SneakerInfo = Field(
        default=...,
        title="Info",
        description="Sneaker Info",
        examples=[
            {"info": {"model": "574", "price": "569.00"}},
            {"info": {"model": "STRUTTER", "price": "319.00"}},
        ],
    )


class SneakerParserHrefBasic(LamodaBasic):
    """
    Basic schema of href and other params by sneaker
    """

    sneaker: str = Field(
        default=...,
        title="Brand Model",
        description="Some Brand Model of sneaker",
        examples=[
            {
                "sneaker": "New Balance 530",
            },
            {
                "sneaker": "adidas DURAMO SL M",
            },
        ],
    )
    href: str = Field(
        default=...,
        title="sneaker href",
        description="some sneaker href",
        examples=[
            {"href": "/p/rtladl945501/shoes-newbalance-krossovki/"},
            {"href": "/p/rtlacx630701/shoes-adidas-krossovki/"},
        ],
    )


class SneakerDetail(LamodaBasic):
    """
    Schema of sneaker detail
    """

    title: str = Field(
        default=...,
        title="Title params",
        description="Title params of sneaker",
    )
    value: str = Field(
        default=...,
        title="Value params",
        description="Value params of sneaker",
    )
