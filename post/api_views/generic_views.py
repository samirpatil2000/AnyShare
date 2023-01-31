import json

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.response import Response


class CustomAPIView(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):


    queryset = None
    serializer_class = None
    Model = None

    def get_obj(self, pk):
        try:
            return self.Model.objects.get(pk=pk)
        except self.Model.DoesNotExist:
            return None

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            response = self.retrieve(request, *args, **kwargs)
        else:
            response = self.list(request, *args, **kwargs)
        result = {"status": status.HTTP_200_OK, "message": "Objects", "data": response.data}
        return Response(data=result)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        object_ = self.get_obj(pk)
        try:
            if object_:
                if object_.author_id != request.user.id:
                    result = {'status': status.HTTP_403_FORBIDDEN, "message": "Not Authorised ..!"}
                else:
                    object_.delete()
                    result = {'status': status.HTTP_200_OK, "message": "Successfully deleted"}
            else:
                result = {'status': status.HTTP_404_NOT_FOUND, "message": "Object Does Not Exist"}
        except Exception as e:
            result = {'status': status.HTTP_400_BAD_REQUEST, "message": str(e)}
        return Response(result)