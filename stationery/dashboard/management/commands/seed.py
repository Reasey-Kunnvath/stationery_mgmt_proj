from django.core.management.base import BaseCommand
from yourappname.models import Categories, Items

class Command(BaseCommand):
    help = 'Seeds the database with static data for Categories and Items'

    def handle(self, *args, **options):
        # Delete existing data to avoid duplicates (optional)
        Categories.objects.all().delete()
        Items.objects.all().delete()

        # Seed Categories
        category1 = Categories.objects.create(cate_id=1, cate_name="Stationery", cate_desc="Items for office and school use")
        category2 = Categories.objects.create(cate_id=2, cate_name="Electronics", cate_desc="Electronic gadgets")

        # Seed Items
        Items.objects.create(
            item_id=1, item_name="Notebook", item_desc="A5 lined notebook", cate_id=category1,
            unit_price=5.99, stk_qty=100, reorder_level=20, item_img=None
        )
        Items.objects.create(
            item_id=2, item_name="Pen", item_desc="Black ink ballpoint pen", cate_id=category1,
            unit_price=1.49, stk_qty=200, reorder_level=30, item_img=None
        )
        Items.objects.create(
            item_id=3, item_name="USB Drive", item_desc="16GB USB 3.0 drive", cate_id=category2,
            unit_price=9.99, stk_qty=50, reorder_level=10, item_img=None
        )
        Items.objects.create(
            item_id=4, item_name="Paper", item_desc="Double-AA A4 Paper sheet", cate_id=category1,
            unit_price=2.99, stk_qty=100, reorder_level=5, item_img=None
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))