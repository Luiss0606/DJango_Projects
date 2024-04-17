# Generated by Django 5.0.4 on 2024-04-17 15:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Pedidos", "0004_auto_20240417_1041"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lineapedido",
            options={
                "ordering": ["id"],
                "verbose_name": "linea de pedido",
                "verbose_name_plural": "lineas de pedido",
            },
        ),
        migrations.AlterModelOptions(
            name="pedido",
            options={
                "ordering": ["id"],
                "verbose_name": "pedido",
                "verbose_name_plural": "pedidos",
            },
        ),
        migrations.AlterModelTable(
            name="lineapedido",
            table="linea_pedidos",
        ),
    ]
