from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

# Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)





class ArticleTestClass(TestCase):

    # Set up method
    def setUp(self):
        James = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        James.save_editor()
        self.news1 = Article(title = 'Kenya builds SGR', post ='Kenya has built the new SGR that extends from MSA to KSM', editor =James)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.news1,Article))

# Testing Save Method
    def test_save_method(self):
        self.news1.save_article()
        article = Article.objects.all()
        self.assertTrue(len(article) > 0)



class tags(TestCase):
    def setUp(self):
        self.new_tag = tags()

    def test_new_tag_isinstance_of_tags(self):
        self.assertTrue(isinstance(self.new_tag,tags))






