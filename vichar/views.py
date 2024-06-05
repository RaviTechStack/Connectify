from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import Post, User, Follow, Comment, directMessage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Random
from django.contrib.auth import authenticate, login, logout
from .serializer import postSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class postserial(APIView):
    def get(self, request):
        allPost = Post.objects.all()
        serializer = postSerializer(allPost, many= True)
        return Response(serializer.data)
    def post(self, request):
        dat = request.data
        print(dat)
        seril = postSerializer(data= dat)
        if seril.is_valid():
            seril.save()
            print("correct")
        else:
            print("wrong")
        return Response(seril.data)

# Create your views here.
@login_required(login_url="/login")
def index(request):
    followed_people = Follow.objects.filter(userfollowing=request.user).values('user')
    followed_person_ids = [followed['user'] for followed in followed_people]
    followed_person_post = Post.objects.filter(postUser__in= followed_person_ids).order_by("?")
    recived_msg = directMessage.objects.filter(receiver = request.user)
    print(recived_msg)

    liked = False
    for pst in followed_person_post:
        if request.user in pst.postLike.all():
            liked = True
        else:
            liked = False
    return render(request, "index.html", {'followed_person_post': followed_person_post, "liked" : liked})


def handellogin(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
        else:
            return HttpResponse("invalid values")
        return redirect("/")
    return render(request, "login.html")


@login_required(login_url="/login")
def post(request):
    if request.method == "POST":
        postContent = request.FILES.get("content")
        postCaption = request.POST.get("caption")

        createPost = Post(postContent = postContent, postCaption = postCaption, postUser = request.user)
        createPost.save()
        return redirect("/")
        
    return render(request, "post.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect("/")
    return render(request, "signup.html")


@login_required(login_url="/login")
def handellogout(request):
    logout(request)
    return redirect("/")

def check(value, listItems):
    if value.lower() in listItems.username.lower() or value in listItems.first_name.lower():
        return True
    
@login_required(login_url="/login")
def searchUser(request):
    allUsers = User.objects.all()
    showUser = []
    if request.method == "GET":
        searchValue = request.GET.get("value")
        for userr in allUsers:
            if userr == request.user:
                continue
            if check(searchValue, userr):
                showUser.append(userr)
                 
        return render(request, "searchUser.html", {"users": showUser})

    params = {
        "users" : showUser
    }
    return render(request, "searchUser.html", params)

def showProfile(request, id):

    requestedUser = User.objects.get(id = id)
    allRelatedPost = Post.objects.filter(postUser = requestedUser)
    followUser, created = Follow.objects.get_or_create(user = requestedUser)
    allFollowedUser = followUser.userfollowing.all()
    allFollowing = Follow.objects.filter(userfollowing = requestedUser)
    currentUserFollowers, created = Follow.objects.get_or_create(user = request.user)
    currentUserFollowersList = currentUserFollowers.userfollowing.all()
    posts = []
    for pst in allRelatedPost:
        isliked = request.user in pst.postLike.all()
        posts.append({
            "id" : pst.postId,
            "isliked" : isliked,
            "url" : pst.postContent.url,
            "noOfLike" : pst.postLike.all().count(),

        })

    if request.user in allFollowedUser:
        isfollow = True
    else:
        isfollow = False
    

    params= {
        "userDetail" : requestedUser,
        "allPost" : posts,
        "Followers" : allFollowedUser,
        "Following" : allFollowing,
        "isfollow" : isfollow,
        "userAllFollowers" : currentUserFollowersList
    }
    
    return render(request, "profile.html", params)






def addlike(request):
    if request.method == "POST":
        postId = request.POST.get("postId")
        currentUser = request.user
        currentPost = Post.objects.get(postId = postId)
        if currentUser in currentPost.postLike.all():
            currentPost.postLike.remove(currentUser)
            return JsonResponse({"numberOfLike":currentPost.postLike.all().count(), "liked" : False})
        
        currentPost.postLike.add(currentUser)
        return JsonResponse({"numberOfLike":currentPost.postLike.all().count(), "liked" : True})
    return render(request, "profile.html")
    

def addFollow(request):
    if request.method == "POST":
        userId = request.POST.get("userId")
        userToFollow = User.objects.get(id = userId)
        userFollowing = request.user

        
        startFollow, created = Follow.objects.get_or_create(user = userToFollow)
        if userFollowing in startFollow.userfollowing.all():
            startFollow.userfollowing.remove(userFollowing)
            return JsonResponse({"message" : "Stopped Follwing", "follow" : True, "allfollow" : startFollow.userfollowing.all().count() })
        else:
            startFollow.userfollowing.add(userFollowing)
            return JsonResponse({"message" : "you started following", "follow" : False, "allfollow" : startFollow.userfollowing.all().count()})
    return redirect("/")


def detailPost(request, id):
    comment_open = request.GET.get("comment-open", False) == "true"
    renderPost = Post.objects.get(postId = id)
    likeCount = renderPost.postLike.all().count()
    relatedCmt = Comment.objects.filter(post = renderPost, parent_comment = None)
    if request.user in renderPost.postLike.all():
        isliked = False
    else:
        isliked = True
        
        
    context ={
        "post" : renderPost,
        "isliked" : isliked,
        "likeCount" : likeCount,
        "cmts" : relatedCmt,
        "open_comment" : comment_open
    }
    return render(request, "detailPost.html", context)

def yourPost(request):
    allPost = Post.objects.filter(postUser = request.user)
    return render(request, "yourPost.html", {"allPost" : allPost})


def commentsApi(request):
    if request.method == "POST":
        data = request.POST.get("postId")
        post = Post.objects.get(postId = data)
        commentContent = request.POST.get("content")
        parent = request.POST.get("parent")
        if parent == "":
            parent = None
        else:
            parent = Comment.objects.get(id = parent)
        saveComment = Comment(comment_user = request.user, post = post, comment_content = commentContent, parent_comment = parent )
        saveComment.save()
        
        return redirect(f"/detailPost/{data}")
    return HttpResponse("done")

def editPost(request, id):
    oldPost = Post.objects.get(postId = id)
    context = {
        "oldPost" : oldPost
    }
    if request.method == "POST":
        newImg = request.FILES.get("changedImage")
        newCaption = request.POST.get("caption")
        if newImg:
            oldPost.postContent = newImg
        else:
            oldPost.postContent = oldPost.postContent
        oldPost.postCaption = newCaption
        oldPost.save()
        return redirect("/yourPost")
    return render(request, "postEdit.html", context)

def delPost(request, id):
    requestedPost = Post.objects.get(postId = id)
    requestedPost.delete()
    return redirect("/yourPost")

def showFriends(request, id):
    showfollowing = request.GET.get("following", False) == "true"
    tryUser = User.objects.get(id = 2)
    tryfollow = Follow.objects.all()
    signeduser = Follow.objects.get(user = request.user )
    allFollowers = signeduser.userfollowing.all()
    allFollowings = Follow.objects.filter(userfollowing = request.user)
    flwingList = []
    for each in allFollowings:
        flwingList.append(each.user)
    context = {
        "followers" : allFollowers,
        "followings" : flwingList,
        "showfollowing" : showfollowing
    }

    return render(request, "profileShow.html", context)

def chat(request):
    return render(request, "chat.html")