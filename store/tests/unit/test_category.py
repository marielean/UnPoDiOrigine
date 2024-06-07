from django.test import TestCase
from store.models.category import Category

class TestCategory(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_create_category(self):
        category = Category.objects.create(name="New Category")
        self.assertEqual(category.name, "New Category")

    def test_update_category(self):
        self.category.name = "Updated Category"
        self.category.save()
        self.assertEqual(self.category.name, "Updated Category")

    def test_delete_category(self):
        category = Category.objects.create(name="To Be Deleted")
        category_id = category.id
        category.delete()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=category_id)

    def test_get_category(self):
        fetched_category = Category.objects.get(name="Test Category")
        self.assertEqual(fetched_category.id, self.category.id)

    def test_get_all_categories(self):
        categories = Category.get_all_categories()
        self.assertEqual(categories.count(), 1)
        self.assertEqual(categories.first().name, "Test Category")
        
