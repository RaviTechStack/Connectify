def sendSelfDetail(request):
    currentUser = request.user
    dataToSend = {
        "currentUser": currentUser,
    }
    return dataToSend