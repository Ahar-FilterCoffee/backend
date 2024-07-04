from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile,Post,Consumer,Producer
from .serielizers import LoginSerielizer,SignUpSerielizer
from django.forms.models import model_to_dict

# Create your views here.

@api_view(['POST'])
def login(request):
    data=LoginSerielizer(data=request.data)
    if data.is_valid():
        username=data.validated_data['username']
        password=data.validated_data['password']
        try:
            obj=Profile.objects.get(username=username)
            fin={
                "message":"success",
            }
            fin.update(model_to_dict(obj))
            
            return Response(data=fin,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={
                "message":str(e),
                "sentData":{
                    "username":username,
                    "password":password
                }
            },status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(data={
            "message":"failed",
            "data":request.data
        },status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def signup(request):
    data=SignUpSerielizer(data=request.data)
    try:
        if data.is_valid():
            saved_data=data.save()
            if saved_data.userType=="Consumer":
                Consumer(user=saved_data,feedNo=request.data["feedNo"]).save()
            elif saved_data.userType=="Producer":
                Producer(user=saved_data).save()
            return Response(data={
                "message":"success",
                "id":saved_data.id
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(data={
            "error":str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#producer
@api_view(['POST'])
def makePost(request):
    #id -> fromUser, quatity,
    try:
        data=request.data
        
        user=Profile.objects.get(id=data["id"])
        p=Post(fromUser=user,quantity=data["quantity"],status=0,img=data["img"],foodType=data["foodType"],foodQuantity=data["foodQuantity"])
        p.save()
        return Response(data={
            "message":"success"
        },status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(data={
            "message":"failed",
            "exception":str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def getPosts(request):
    try:
        data=request.data
        p=Post.objects.all()
        postData=[]
        statusCheck={
            0:"Not Booked",
            1:"Delivering",
            2:"Delivered"
        }
        for i in p:
            postData.append({
                "id":i.id,
                "name":i.fromUser.orgName,
                "quantity":i.quantity,
                "status":statusCheck[i.status],
                "img":i.img
            })
        return Response(data={
            "message":"success",
            "posts":postData
        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={
            "message":"failed",
            "exeption":str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["POST"])
def acceptPost(request):
    pass
@api_view(["POST"])
def postDetails(request):
    data=request.data 
    try:
        post=Post.objects.get(id=data["id"])
        fin=model_to_dict(post,fields=["id","quantity","img","foodType","foodQuantity"])
        statusCheck={
            0:"Not Booked",
            1:"Delivering",
            2:"Delivered"
        }
        fin["status"]=statusCheck[post.status]
        fin["name"]=post.fromUser.orgName
        fin["message"]="success"
        return Response(fin,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message":"failed",
            "error":str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Best post calculations
def distanceCalc(p1,p2): #p -> [x,y]
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)
def ratingCalc(up,noUp,down,noDown):
    return up*noUp+down*noDown
@api_view(['POST'])
def bestPosts(request): #User id
    #Score dict - postID:score
    try:
        scores={}
        posts=Post.objects.all()
        user=Profile.objects.get(id=request.data["id"])
        print(user)
        cons=user.user_consumer
        for p in posts:
            fromUser=p.fromUser
            prod=fromUser.user_producer
            dist=distanceCalc([fromUser.locx,fromUser.locy],[user.locx,user.locy])
            if  prod.delivered==0 or prod.rating==0:
                s=0.5*dist+0.5* cons.feedNp
            else:
                s=0.3*dist+0.2*cons.rating+0.5*cons.feedNp
            scores[p.id]=s
            return Response(scores,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "error":str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

