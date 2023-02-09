from django.http import HttpResponse, request
from django.shortcuts import render
# Create your views here.
from .models import Product, Order, Customer
from . forms import OrderForm

def home(request):
    Orders = Order.objects.all()

    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = Orders.count()

    delivered = Orders.filter(status='Delivered').count()

    pending = Orders.filter(status='Pending').count()

    context = {'Orders': Orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders':total_orders,'delivered': delivered, 'pending': pending}

    return render(request, 'api/dashboard.html', context)

def products(request):

    products = Product.objects.all()
    return render(request, 'api/products.html', {'products':products})

def customer(request, pk_test):

    customer = Customer.objects.get(id=pk_test)

    Orders = customer.order_set.all()

    context = {'Orders':Orders, 'customer':customer}

    return render(request, 'api/customer.html', context)


def createOrder(requet):
    form = OrderForm()

    context = {'form':form}

    return render(request, 'api/order_form.html', context)

"""

class CustomCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CutomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class CustomDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CutomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class CourseCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class CourseDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class UsersCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    # registration login 3 buttons mark attendence, mark leave view button  student marks attendence once in day option edit profile user
    # sent leave rekuest

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class UsersDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class adminpanelCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = adminpanel.objects.all()
    serializer_class = adminpanelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class adminpanelDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    # login view student record   admin can crud  should able to sent report of users.  leave approval . count of leaves present absent. .
    # create completesystm report .. add up grading system , 26 day present a grade ten day present a grade.

    queryset = adminpanel.objects.all()
    serializer_class = adminpanelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class subjectCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = subject.objects.all()
    serializer_class = subjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class subjectDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = subject.objects.all()
    serializer_class = subjectSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class attendenceCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = attendence.objects.all()
    serializer_class = attendenceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class attendenceDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = attendence.objects.all()
    serializer_class = attendenceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class attendencedetailCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = attendencedetail.objects.all()
    serializer_class = attendencedetailSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class attendencedetailDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = attendencedetail.objects.all()
    serializer_class = attendencedetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class leavesCP(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = leaves.objects.all()
    serializer_class = leavesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class leavesDU(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = leaves.objects.all()
    serializer_class = leavesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

"""