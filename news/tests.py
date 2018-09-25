from django.test import TestCase
from .models import Editor,Article,Tags

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


# class ArticleTestClass(TestCase):
#
#     # Set up method
#     def setUp(self):
#         James = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
#         James.save_editor()
#         self.news1 = Article(title = 'Kenya builds SGR', post ='Kenya has built the new SGR that extends from MSA to KSM', editor =James)
#
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.news1,Article))
#
# # Testing Save Method
#     def test_save_method(self):
#         self.news1.save_article()
#         article = Article.objects.all()
#         self.assertTrue(len(article) > 0)



class Tags(TestCase):
    def setUp(self):
        self.new_tag = Tags()

    def test_new_tag_isinstance_of_tags(self):
        self.assertTrue(isinstance(self.new_tag,Tags))



class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        news_of_day = Article.news_of_day()
        self.assertTrue(len(news_of_day) > 0)

    def test_get_news_by_date(self):
        '''
        Test to confirm that we are getting news according to a given date
        '''
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)






