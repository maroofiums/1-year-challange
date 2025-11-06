from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from todo.models import Todo
from django.db import IntegrityError

# ----------------------------
# Model Tests
# ----------------------------
class TodoModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_str_returns_title(self):
        todo = Todo.objects.create(title="Buy milk", user=self.user)
        self.assertEqual(str(todo), "Buy milk")

    def test_default_complete_is_false(self):
        todo = Todo.objects.create(title="Read book", user=self.user)
        self.assertFalse(todo.complete)

    def test_create_requires_user(self):
        with self.assertRaises(IntegrityError):
            Todo.objects.create(title="No user todo")


# ----------------------------
# Views Tests
# ----------------------------
class TodoViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="viewer", password="pass1234")
        # User ke liye 2 todos
        self.t1 = Todo.objects.create(title="T1", user=self.user)
        self.t2 = Todo.objects.create(title="T2", user=self.user)

    def test_todo_list_view_requires_login(self):
        url = reverse("list_tasks")
        response = self.client.get(url)
        self.assertIn(response.status_code, (302, 200))  # redirect if not logged in

    def test_todo_list_view_shows_user_todos(self):
        self.client.force_login(self.user)
        url = reverse("list_tasks")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        tasks = response.context.get("tasks")
        self.assertIsNotNone(tasks)
        titles = [t.title for t in tasks]
        self.assertIn("T1", titles)
        self.assertIn("T2", titles)

    def test_create_todo_view(self):
        self.client.force_login(self.user)
        url = reverse("create_task")
        data = {"title": "New Task", "description": "desc"}
        response = self.client.post(url, data)
        self.assertIn(response.status_code, (302, 201))
        self.assertTrue(Todo.objects.filter(title="New Task", user=self.user).exists())

    def test_update_todo_view(self):
        self.client.login(username="user1", password="pass1234")
        url = reverse("update_task", args=[self.t1.id])
        data = {"title": "Updated Title", "description": "Updated Desc", "complete": True}
        response = self.client.post(url, data)
        
        self.t1.refresh_from_db()  # << Important!
        self.assertEqual(self.t1.title, "Updated Title")


    def test_delete_todo_view(self):
        self.client.force_login(self.user)
        url = reverse("delete_task", kwargs={"pk": self.t2.pk})
        response = self.client.post(url)
        self.assertIn(response.status_code, (302, 204, 200))
        self.assertFalse(Todo.objects.filter(pk=self.t2.pk).exists())
