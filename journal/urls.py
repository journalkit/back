from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from api.models import *
from api.controller import login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('id', 'login', 'token', 'name', 'password', 'surname', 'patronymic', 'role')
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)
            if user.role.users:
                return User.objects.all()
            elif user.role.disciplines:
                teachersOnly = self.request.query_params.get('teachersOnly', False)
                if teachersOnly:
                    return User.objects.all().filter(role=2)
                else:
                    return User.objects.all().filter(token=secure)
            else:
                return User.objects.filter(token=secure)
        except:
            return None

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)
            return Role.objects.filter(id=user.role.id)
        except:
            return None

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'
        # fields = ('id', 'name', 'teacher')
class DisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplineSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.exams_admin or user.role.disciplines or user.role.docs:
                return Discipline.objects.all()
            else:
                return Discipline.objects.filter(teacher=user.id)
        except:
            return None

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
        # fields = ('id', 'name', 'discipline')
class ThemeViewSet(viewsets.ModelViewSet):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.lessons or user.role.disciplines:
                discipline = self.request.query_params.get('discipline', False)
                if discipline:
                    return Theme.objects.filter(discipline=discipline).order_by('name')
                else:
                    return Theme.objects.all()
        except:
            return None

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ('id', 'name')
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = '__all__'
        # fields = ('id', 'date_open', 'date_close', 'discipline', 'group')
class StatementViewSet(viewsets.ModelViewSet):
    serializer_class = StatementSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.lessons:
                notClosed = self.request.query_params.get('notClosed', False)
                if notClosed:
                    return Statement.objects.filter(discipline__teacher=user.id, date_close__isnull=True).order_by('-date_open')
                else:
                    return Statement.objects.filter(discipline__teacher=user.id).order_by('-date_open')
        except:
            return None

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        # fields = ('id', 'date', 'statement', 'theme', 'control1', 'control2')
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.lessons:
                statement = self.request.query_params.get('statement', False)
                if statement:
                    return Lesson.objects.filter(statement=statement).order_by('date')
                else:
                    return Lesson.objects.all()
        except:
            return None

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ('id', 'name', 'surname', 'patronymic', 'group', 'record_book')
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.lessons or user.role.exams or user.role.groups:
                group = self.request.query_params.get('group', False)
                if group:
                    return Student.objects.filter(group=group).order_by('surname','name')
                else:
                    return Student.objects.all()
        except:
            return None

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        # fields = ('id', 'lesson', 'student', 'mark1', 'mark2')
class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.lessons or user.role.exams:
                lessons = self.request.query_params.getlist('lessons[]', [])
                students = self.request.query_params.getlist('students[]', [])
                if lessons and students:
                    return Record.objects.filter(lesson__in=lessons, student__in=students)
                else:
                    return Record.objects.all()
        except:
            return None

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
        # fields = ('id', 'date', 'group', 'discipline', 'closed')
class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.exams_admin:
                return Exam.objects.all()
            elif user.role.docs:
                group = self.request.query_params.get('group', False)
                return Exam.objects.filter(group=group).order_by('date')
            else:
                notClosed = self.request.query_params.get('notClosed', False)
                if notClosed:
                    return Exam.objects.filter(discipline__teacher=user.id, closed=False).order_by('-date')
                else:
                    return Exam.objects.filter(discipline__teacher=user.id).order_by('-date')
        except:
            return None

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamList
        fields = '__all__'
        # fields = ('id', 'exam', 'student', 'ticket', 'mark')
class ExamListViewSet(viewsets.ModelViewSet):
    serializer_class = ExamListSerializer

    def get_queryset(self):
        try:
            if self.request.method == 'GET':
                secure = self.request.query_params.get('secure', False)
            else:
                secure = self.request.data.get('secure', False)
            user = User.objects.get(token=secure)

            if user.role.exams:
                exam = self.request.query_params.get('exam', False)
                if exam:
                    return ExamList.objects.filter(exam__discipline__teacher=user.id,exam=exam)
                else:
                    return ExamList.objects.filter(exam__discipline__teacher=user.id)
            elif user.role.docs:
                group = self.request.query_params.get('group', False)
                return ExamList.objects.filter(student__group=group)
        except:
            return None


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'user')
router.register(r'roles', RoleViewSet, 'role')
router.register(r'disciplines', DisciplineViewSet, 'discipline')
router.register(r'themes', ThemeViewSet, 'theme')
router.register(r'groups', GroupViewSet, 'group')
router.register(r'statements', StatementViewSet, 'statement')
router.register(r'lessons', LessonViewSet, 'lesson')
router.register(r'students', StudentViewSet, 'student')
router.register(r'records', RecordViewSet, 'record')
router.register(r'exams', ExamViewSet, 'exam')
router.register(r'examlists', ExamListViewSet, 'examlist')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/login/', login),
]