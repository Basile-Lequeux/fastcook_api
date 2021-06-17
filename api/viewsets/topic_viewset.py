from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from service.object.topic import Topic
from service.object.message import Message
from service.object.user import User
from api import serializers


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = serializers.TopicSerializer

    @action(detail=False, methods=['POST'])
    def post_message(self, request):
        request = self.request.data
        topic_id = request['topic_id']
        user_id = request['user_id']
        message = request['message']

        topic = Topic.objects.get(id=topic_id)
        user = User.objects.get(id=user_id)

        new_message = Message.objects.create(text=message, topic_id=topic, author=user)
        topic.message.add(new_message)
        serialize = serializers.TopicSerializer(topic)
        #renvoyer tout les messages comme favoris

        return Response(serialize.data, status=200)

    @action(detail=False, methods=['GET'])
    def display_topic_messages(self, request):
        topic_id = self.request.query_params.get('id', None)

        topic = Topic.objects.get(id=topic_id)
        messages = topic.message.all()

        serializer = serializers.MessageSerializer(messages, many=True)

        return Response(serializer.data, status=200)

    @action(detail=False, methods=['POST'])
    def put_icon(self, request):
        topic_id = self.request.query_params.get('id', None)
        icon_string = self.request.query_params.get('icon', None)

        topic = Topic.objects.get(id=topic_id)
        topic.icon = icon_string
        topic.save()

        return Response(status=200)
