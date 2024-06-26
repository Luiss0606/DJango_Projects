# Generated by Django 5.0.4 on 2024-04-17 15:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Pedidos", "0002_rename_pedido_id_lineapedido_pedido_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lineapedido",
            options={
                "ordering": ["id"],
                "verbose_name": "Línea Pedido",
                "verbose_name_plural": "Líneas Pedidos",
            },
        ),
        migrations.AlterModelOptions(
            name="pedido",
            options={
                "ordering": ["id"],
                "verbose_name": "Pedido",
                "verbose_name_plural": "Pedidos",
            },
        ),
        migrations.AlterModelTable(
            name="lineapedido",
            table="lineapedidos",
        ),
    ]
